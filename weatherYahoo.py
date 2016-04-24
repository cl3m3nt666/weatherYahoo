#!/usr/bin/env python
# encoding: utf-8

"""
 Search weather from Yahoo ! Sample weather script

 || MAINTAINER : cl3m3nt - http://github.com/cl3m3nt666
"""

#Example Json read
#{u'channel': {u'lastBuildDate': u'Sun, 24 Apr 2016 04:14 PM CEST', u'atmosphere': {u'pressure': u'1009.0', u'rising': u'0', u'visibility': u'16.1', u'humidity': u'79'}, u'description': u'Yahoo! Weather for Paris, Ile-de-France, FR', u'language': u'en-us', u'title': u'Yahoo! Weather - Paris, Ile-de-France, FR', u'image': {u'url': u'http://l.yimg.com/a/i/brand/purplelogo//uh/us/news-wea.gif', u'width': u'142', u'height': u'18', u'link': u'http://weather.yahoo.com', u'title': u'Yahoo! Weather'}, u'item': {u'description': u'<![CDATA[<img src="http://l.yimg.com/a/i/us/we/52/39.gif"/>\n<BR />\n<b>Current Conditions:</b>\n<BR />Scattered Showers\n<BR />\n<BR />\n<b>Forecast:</b>\n<BR /> Sun - Scattered Showers. High: 52Low: 38\n<BR /> Mon - Cloudy. High: 53Low: 38\n<BR /> Tue - Partly Cloudy. High: 49Low: 41\n<BR /> Wed - Rain. High: 51Low: 37\n<BR /> Thu - Partly Cloudy. High: 53Low: 37\n<BR />\n<BR />\n<a href="http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-615702/">Full Forecast at Yahoo! Weather</a>\n<BR />\n<BR />\n(provided by <a href="http://www.weather.com" >The Weather Channel</a>)\n<BR />\n]]>', u'pubDate': u'Sun, 24 Apr 2016 03:00 PM CEST', u'title': u'Conditions for Paris, Ile-de-France, FR at 03:00 PM CEST', u'long': u'2.3412', u'forecast': [{u'code': u'39', u'text': u'Scattered Showers', u'high': u'52', u'low': u'38', u'date': u'24 Apr 2016', u'day': u'Sun'}, {u'code': u'26', u'text': u'Cloudy', u'high': u'53', u'low': u'38', u'date': u'25 Apr 2016', u'day': u'Mon'}, {u'code': u'30', u'text': u'Partly Cloudy', u'high': u'49', u'low': u'41', u'date': u'26 Apr 2016', u'day': u'Tue'}, {u'code': u'12', u'text': u'Rain', u'high': u'51', u'low': u'37', u'date': u'27 Apr 2016', u'day': u'Wed'}, {u'code': u'30', u'text': u'Partly Cloudy', u'high': u'53', u'low': u'37', u'date': u'28 Apr 2016', u'day': u'Thu'}, {u'code': u'30', u'text': u'Partly Cloudy', u'high': u'55', u'low': u'38', u'date': u'29 Apr 2016', u'day': u'Fri'}, {u'code': u'28', u'text': u'Mostly Cloudy', u'high': u'55', u'low': u'40', u'date': u'30 Apr 2016', u'day': u'Sat'}, {u'code': u'12', u'text': u'Rain', u'high': u'56', u'low': u'41', u'date': u'01 May 2016', u'day': u'Sun'}, {u'code': u'47', u'text': u'Scattered Thunderstorms', u'high': u'55', u'low': u'44', u'date': u'02 May 2016', u'day': u'Mon'}, {u'code': u'47', u'text': u'Scattered Thunderstorms', u'high': u'56', u'low': u'44', u'date': u'03 May 2016', u'day': u'Tue'}], u'link': u'http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-615702/', u'lat': u'48.85693', u'guid': {u'isPermaLink': u'false'}, u'condition': {u'date': u'Sun, 24 Apr 2016 03:00 PM CEST', u'text': u'Scattered Showers', u'code': u'39', u'temp': u'42'}}, u'link': u'http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-615702/', u'location': {u'city': u'Paris', u'region': u' Ile-de-France', u'country': u'France'}, u'ttl': u'60', u'units': {u'distance': u'mi', u'speed': u'mph', u'temperature': u'F', u'pressure': u'in'}, u'astronomy': {u'sunset': u'8:58 pm', u'sunrise': u'6:40 am'}, u'wind': {u'direction': u'0', u'speed': u'0', u'chill': u'43'}}}

import urllib2, urllib, json
from argparse import ArgumentParser
import sys

#Fonc for argv
def create_cli_parser():
    """
    Creates a command line interface parser.
    """
    cli_parser = ArgumentParser(description=__doc__)

    cli_parser.add_argument('location_code',
        help="[Format woeid] The location code for the region you want to retrieve weather. Example : Paris - 615702. for. See http://woeid.rosselliot.co.nz/lookup/paris  ")

    return cli_parser

def main(argv):

    # Create the command line parser.
    cli_parser = create_cli_parser()

    # Get the options and arguments.
    args = cli_parser.parse_args(argv)


    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    #Requete yql_query
    yql_query = "select * from weather.forecast where woeid="
    yql_query += args.location_code
    yql_query += " and u='c'"

    yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json&u=c"

    try:
        result = urllib2.urlopen(yql_url).read()


        data = json.loads(result)

        print "---------------------------------"
        print "Weather from Yahoo for " + data['query']['results']['channel']['location']['city'] + data['query']['results']['channel']['location']['region'] + ", " + data['query']['results']['channel']['location']['country']
        print "---------------------------------"
        print "Actually"
        print "---------------------------------"
        print data['query']['results']['channel']['item']['forecast'][0]['day'] + " " + data['query']['results']['channel']['item']['forecast'][0]['date']
        print "Temp : " + data['query']['results']['channel']['item']['condition']['temp'] + " C |-| " + data['query']['results']['channel']['item']['condition']['text']
        print "Temp low : " + data['query']['results']['channel']['item']['forecast'][0]['low'] + " C"
        print "Temp high : " + data['query']['results']['channel']['item']['forecast'][0]['high'] + " C"
        print "---------------------------------"
        print "Forecast 2 Day"
        print "---------------------------------"
        print data['query']['results']['channel']['item']['forecast'][1]['day'] + " " + data['query']['results']['channel']['item']['forecast'][1]['date']
        print data['query']['results']['channel']['item']['forecast'][1]['text']
        print "Temp low : " + data['query']['results']['channel']['item']['forecast'][1]['low'] + " C"
        print "Temp high : " + data['query']['results']['channel']['item']['forecast'][1]['high'] + " C"
        print "---------------------------------"
        print data['query']['results']['channel']['item']['forecast'][2]['day'] + " " + data['query']['results']['channel']['item']['forecast'][1]['date']
        print data['query']['results']['channel']['item']['forecast'][2]['text']
        print "Temp low : " + data['query']['results']['channel']['item']['forecast'][2]['low'] + " C"
        print "Temp high : " + data['query']['results']['channel']['item']['forecast'][2]['high'] + " C"
        print "---------------------------------"

    except urllib2.HTTPError:
        print "404 HTTPError - Problem URL - location_code"




if __name__ == "__main__":
    main(sys.argv[1:])
