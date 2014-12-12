#!/usr/bin/env python3

import argparse
import cairo
import yaml

class Data:
    
    def __init__(self):
        self.features = []
        self.observations = None
        # array of array
        self.data = []
        self.config = None

    def read(self, config_fname, data_fname, delim='\t'):

        with open(config_fname, 'r') as inf:
            self.config = yaml.load(inf.read())

        # format: rows are observations and columns are features
        # header column contain feature names
        # header row contain observation names

        features = []
        data = []
        with open(data_fname, 'r') as inf:
            # read header, exclude first item
            self.observations = inf.readline().rstrip().split(delim)[1:]
            
            for line in inf:
                items = line.rstrip().split(delim)
                features.append(items[0])
                data.append(items[1:])

        # remove un-annotated features
        annotated = self.config['features']
        j = 0
        for feature in features:
            if feature in annotated:
                self.features.append(feature)
                self.data.append(data[j])
            j += 1
    


class Tiler:

    def __init__(self, context, data):
        self.cr = context
        self.d = data
    
    def draw(self):

        w, h = 3, 15
        hspacing, vspacing = 1, 2
        corner_radius = 2

        for i in range(len(self.d.features)):
            for j in range(len(self.d.observations)):

                feature = self.d.config['features'][self.d.features[i]]
                    
                x = j * (w + hspacing)
                y = i * (h + vspacing)
                self.rounded_box((x, y, x+w, y+h), corner_radius)
                draw_type = feature['type']
                try:
                    value = feature[draw_type][self.d.data[i][j]]
                    colour = self.d.config['colours'][value]
                except:
                    colour = (1, 1, 1)

                self.cr.set_source_rgb(*colour)
                self.cr.fill()


    def rounded_box(self, area, radius):
        """ Draws rectangles with rounded (circular arc) corners """
        from math import pi

        a, c, b, d = area
        self.cr.arc(a + radius, c + radius, radius, 2*(pi/2), 3*(pi/2))
        self.cr.arc(b - radius, c + radius, radius, 3*(pi/2), 4*(pi/2))
        self.cr.arc(b - radius, d - radius, radius, 0*(pi/2), 1*(pi/2))
        self.cr.arc(a + radius, d - radius, radius, 1*(pi/2), 2*(pi/2))
        self.cr.close_path()


def draw_events_plot(data_fname, config_fname, output_fname):
    w, h = 1000, 150

    surface = cairo.SVGSurface(output_fname, w, h)
    cr = cairo.Context(surface)

    d = Data();
    d.read(config_fname, data_fname)

    tiler = Tiler(cr, d)

    tiler.draw()

    surface.finish()


if __name__ == '__main__':

    data_fname = 'surv_group3_riskg.mtx'
    config_fname = 'surv_group3_riskg.features'
    output_fname = 'surv_group3_riskg_events.svg'
    draw_events_plot(data_fname, config_fname, output_fname)

    data_fname = 'surv_group4_riskg.mtx'
    config_fname = 'surv_group4_riskg.features'
    output_fname = 'surv_group4_riskg_events.svg'
    draw_events_plot(data_fname, config_fname, output_fname)

    data_fname = 'surv_shh_riskg.mtx'
    config_fname = 'surv_shh_riskg.features'
    output_fname = 'surv_shh_riskg_events.svg'
    draw_events_plot(data_fname, config_fname, output_fname)

