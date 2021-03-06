# Script for figuring out the deBroglie wavelength.
# Useful for Aleks questions (Objective 8) in chemistry, instead of constantly recalculating the same stuff.
# Pass in the weight units distance units speed units plank's constant
# Ex: python deBroglie.py 1 kg 2 m 3 m__s 6.6207e-8
# Look up http://python-measurement.readthedocs.org/en/latest/ for more units

import sys
import math
import argparse
from measurement.measures import *
from measurement.utils import *

#Validate input
if len(sys.argv) != 8:
	print "Usage: python deBroglie.py weight units distance units speed units plank"
	sys.exit(1)
else:
	#Using measurements library for units
	try: 
		m = float(sys.argv[1])
		mUnit = sys.argv[2]

		w = float(sys.argv[3])
		wUnit = sys.argv[4]

		v = float(sys.argv[5])
		vUnit = sys.argv[6]

		plank = float(sys.argv[7])

	except:
		print "Check your input:", sys.argv[1: 8]
		sys.exit(1)

	print "Obtained: ", m,mUnit, w, wUnit, v, vUnit, "plank's: ", plank

	#Convert this nonsense first
	try:
		mass = guess(m, mUnit, measures=[Weight])
		width = guess(w, wUnit, measures=[Distance])
		velocity = guess(v, vUnit, measures=[Speed])
	except ValueError:
		print "Check your units:", mUnit, wUnit, vUnit
		sys.exit(1)

	#We want it in kg, m, m/s
	print "Converted:", mass.kg, "kg,", width.m, "m,", velocity.m__sec, "m/s"

	#Reassign these numbers
	m = mass.kg
	w = width.m
	v = velocity.m__sec

	#Calculate deBroglie
	deBroglie = plank / float(m * v)

	if(deBroglie >= w):
		print "Quantum: ", deBroglie
	else:
		print "Classical: ", deBroglie
