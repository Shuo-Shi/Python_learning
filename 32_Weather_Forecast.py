# -*- coding:utf-8 -*-

from xml.parsers.expat import ParserCreate
# import requests
import pprint

class WeatherSaxHandler(object):
    def __init__(self):
        self.result = dict() # 定义一个用来存储结果的result字典
        self.count = 0
        self.result['forecast'] = dict() # 在result字典中，定义一个用来存储forecast的字典
    def StartElementHandler(self,name,attrs):
        if name == 'yweather:location':
            self.result['location'] = attrs
        if name == 'yweather:forecast':
            self.count += 1
            if self.count <= 2:
                self.result['forecast'][str(self.count)] = attrs
            else:
                pass

def parse_weather(data):
    # data = requests.get(my_url).text
    handler = WeatherSaxHandler() # 创建一个WeatherSaxHandler类的实例handler
    parser = ParserCreate() # 创建一个ParserCreate类的实例parser
    parser.StartElementHandler = handler.StartElementHandler 
    parser.Parse(data)
    weather = dict()
    loc = handler.result['location']
    foc = handler.result['forecast']
    weather['city'] = loc['city']
    weather['country'] = loc['country']
    weather['today'] = dict([('text', foc['1']['text']), ('low', foc['1']['low']), ('high', foc['1']['high'])])
    weather['tomorrow'] = dict([('text', foc['2']['text']), ('low', foc['2']['low']), ('high', foc['2']['high'])])
    weather = pprint.pformat(weather)
    return weather


# 测试:
data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
</rss>
'''

if __name__ == '__main__':
    result = parse_weather(data)
    print(result)