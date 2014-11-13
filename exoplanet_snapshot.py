# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 15:27:01 2014

@author: choog_000
"""
##import required packages##
import urllib2
import re

dataURL = "https://raw.githubusercontent.com/OpenExoplanetCatalogue/oec_tables/master/comma_separated/open_exoplanet_catalogue.txt"

##query OpenExoplanetCatalogue URL to pull down csv file##

data = urllib2.urlopen(dataURL)
readData = data.read()

myFile = open("C:\\Users\\choog_000\\Documents\\Github\\Exoplanet-Snapshot\\data_output.txt",'w')



