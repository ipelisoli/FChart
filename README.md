# FChart
Generates DSS finding chart from coordinates.

Usage: python FChart.py [INPUT]

The input can be in two formats:
1. A file containing three columns: a target name (no spaces), ra in degrees, dec in degrees.
2. One line input with target name (no spaces), ra in degrees, dec in degrees.

Note that proper motions are not taken into account (yet), therefore the target can be slightly off centre.
