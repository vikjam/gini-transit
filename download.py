#!/usr/bin/env python
"""
Download MBTA data
Tested on Python 3.4
"""
import urllib.request
import yaml
import requests
import json
import io
import csv

# # Pull down the YAML file
# urllib.request.urlretrieve('http://erikdemaine.org/maps/mbta/mbta.yaml', 'mbta.yaml')

# Parse the YAML file
with open('mbta.yaml', 'r') as stream:
    mbta_data = yaml.load(stream)

# Export to CSV with FIPS
with open('mbta.csv', 'w', newline = "") as csvfile:
    writer = csv.writer(csvfile, delimiter = ',') 
    for line in mbta_data:
        color      = line['color']
        line_title = line['title']
        for station in line['stations']:
            try:
                lines         = station['lines']
                station_title = station['title']
                longitude     = station['longitude']
                latitude      = station['latitude']
                url           = 'http://data.fcc.gov/api/block/find?format=json&latitude={0}&longitude={1}&showall=false'.format(latitude, longitude)
                rsp           = requests.get(url)
                inpo          = io.StringIO(rsp.text)
                jsn           = json.load(inpo)
                fips          = jsn['Block']['FIPS'] 
            except:
                continue

            print([color, line_title, station_title, longitude, latitude, fips])
            writer.writerow([color, line_title, station_title, longitude, latitude, fips])


# End of the script
