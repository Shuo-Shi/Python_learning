# -*- coding:utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('starttag<%s>' % tag)

    def handle_endtag(self, tag):
        print('endtag</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('startendtag<%s/>' % tag)

    def handle_data(self, data):
        print(data.replace(u'\xa0', u' ')) 
        # unicode中的‘\xa0’字符在转换成gbk编码时会出现问题，gbk无法转换'\xa0'字符。
        # 所以，在转换的时候必需进行一些前置动作：string.replace(u'\xa0', u' '), 将'\xa0‘替换成u' '空格。
        # Unix系统下不需要如此，直接print(data)即可

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

# feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。
# 特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。	
# 			字符					十进制	转义字符
# 			 "						&#34;	&quot;
# 			 &						&#38;	&amp;
# 			 <						&#60;	&lt;
# 			 >						&#62;	&gt;
# 不断开空格(non-breaking space)	&#160;	&nbsp;

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')