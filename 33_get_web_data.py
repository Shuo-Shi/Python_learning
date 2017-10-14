# -*- coding:utf-8 -*-

import urllib.request
from html.parser import HTMLParser
import re

url = "https://www.python.org/events/python-events/"

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
web_data = response.read()
web_data = web_data.decode('utf-8')
web_data = web_data.replace(u'\xf6', u' ')

# print(type(response))
# print(response.geturl())
# print(response.info())
# print(response.getcode())

class MyHTMLParser(HTMLParser):
    print_flag = False

    def handle_starttag(self, tag, attrs):
        if (tag == 'a') and (len(attrs) > 0):
            if re.match(r'.*python-events.*', attrs[0][1]) and len(attrs[0][1]) == 26:
                print('event name:')
                self.print_flag = True
        elif tag == 'time':
            print('event time:')
            self.print_flag = True
        elif (tag == 'span') and (len(attrs) > 0):
            if re.match(r'.*event-location.*', attrs[0][1]):
                print('event location:')
                self.print_flag = True
        else:
            self.print_flag = False
        pass

    def handle_data(self, data):
        if self.print_flag:
            print(data)

parser = MyHTMLParser()
parser.feed(web_data)