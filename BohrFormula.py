#!/usr/bin/python

# Script for figuring out the wavelength of a line in the spectrum of hydrogen.
# First calculates the change in two given energy levels using Bohr's formula
# Then finds the wavelength using the relationship between photon energy and wavelength
# Ex: python BohrFormula 4 3
import sys
import math

try:
	level1 = float(sys.argv[1])
	level2 = float(sys.argv[2])
except:
	print "Check your energy level arguments"
	sys.exit(1)

#Plug in formula
energy = abs((-2.17987e-18)/(level2**2) - (-2.17987e-18)/(level1**2))

#Wavelength
wavelength = ((6.62607e-34) * 299792458) / energy

print "Wavelength lamda:"
print " ", wavelength, "m"
print " ", wavelength * 10**9, "nm"
print " ", wavelength * 10**6, "micrometers"