# Generates a finding chart given either an object name and coordinates, or a
# .txt file containing a list of names and coordinates.
#
# It will use astroplan to download a DSS cutout around the target, then add a
# cross at the input coordinates, North/East indicators, and approximate scale.

__version__ = '1.0'
__author__ = 'Ingrid Pelisoli'

# Importing relevant packages:

from astroplan import FixedTarget
from astropy.coordinates import SkyCoord
from astroplan.plots import plot_finder_image
import matplotlib.pyplot as plt
import astropy.units as u
from astropy.io import ascii
import numpy as np
import sys

def make_plot(ra, dec, name):
    '''Creates finding chart plot from input coordinates IN DEGREES and name'''

    # Generate coordinates
    coords = SkyCoord(ra=ra*u.deg, dec=dec*u.deg)
    target = FixedTarget(coord=coords, name=name)

    # Create figure
    fig = plt.figure(figsize=(18,18))
    plt.rcParams.update({'font.size': 15})

    # Download cutout
    ax, hdu = plot_finder_image(target, survey='DSS',
                                fov_radius=2*u.arcmin,reticle='True')

    # Circle around the star
    circle = plt.Circle((150, 150), 8.0, color='b', fill=False)

    # North and East arrows
    arrow = plt.arrow(270, 30, -50, 0, color='r', length_includes_head = 'True',
                      width = 2, head_width = 3)
    arrow2 = plt.arrow(270, 30, 0, 50, color='r', length_includes_head = 'True',
                       width = 2, head_width = 3)

    # Scale
    arrow3 = plt.arrow(30, 30, 100, 0, color='k', length_includes_head = 'False',
                       width = 2, head_width = 0)
    ax.add_artist(arrow)
    ax.add_artist(arrow2)
    plt.text(30,270,'DSS',fontsize=25)
    plt.text(220,32,"E",fontsize=25)
    plt.text(272,80,"N",fontsize=25)
    plt.text(80,34,"40''",fontsize=25)

    # Save figure
    fig.savefig('%s.png'%(name))
    plt.close(fig)

# Read input

if (len(sys.argv) == 2):
    infile = sys.argv[1]
    data = ascii.read(infile, names=['source_id','ra','dec'])
    targets = np.array(data['source_id'])
    ra = np.array(data['ra'])
    dec = np.array(data['dec'])
    for i in range(0,len(ra)):
        make_plot(ra[i], dec[i], targets[i])
elif (len(sys.argv) == 4):
    target = sys.argv[1]
    ra = np.float(sys.argv[2])
    dec = np.float(sys.argv[3])
    make_plot(ra, dec, target)
else:
    print("I don't understand your input.")
    print("It should be either a file, or NAME RA[deg] DEC[deg]")
    sys.exit()
