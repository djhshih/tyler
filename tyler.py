#!/usr/bin/env python3

import argparse
import cairo


class DataFrame:
	
	def __init__(self):
		self.features = []
		self.observations = None
		# array of array
		self.data = []
	
	def read(self, fname, delim='\t'):

		# format: rows are observations and columns are features
		# header column contain feature names
		# header row contain observation names

		with open(fname, 'r') as inf:
			# read header, exclude first item
			self.observations = inf.readline().rstrip().split(delim)[1:]
			
			for line in inf:
				items = line.rstrip().split(delim)
				self.features.append(items[0])
				self.data.append(items[1:])


class Tiler:

	def __init__(self, context, dataFrame):
		self.cr = context
		self.df = dataFrame
	
	def draw():
		for i in range(len(dataFrame.features)):
			for j in range(len(dataFrame.observations)):
				#TODO
				pass


	def __rounded_box(cr, area, radius):
			""" Draws rectangles with rounded (circular arc) corners """
			from math import pi

			a, c, b, d = area
			cr.arc(a + radius, c + radius, radius, 2*(pi/2), 3*(pi/2))
			cr.arc(b - radius, c + radius, radius, 3*(pi/2), 4*(pi/2))
			cr.arc(b - radius, d - radius, radius, 0*(pi/2), 1*(pi/2))  # ;o)
			cr.arc(a + radius, d - radius, radius, 1*(pi/2), 2*(pi/2))
			cr.close_path()



w, h = 100, 100
corner_radius = 5

area = (0, 0, w, h)

surface = cairo.SVGSurface('example.svg', w, h)
cr = cairo.Context(surface)
cr.set_source_rgb(0, 0, 1)

rounded_box(cr, area, corner_radius)
cr.fill()

surface.finish()

