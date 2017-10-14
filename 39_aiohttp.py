#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio

from aiohttp import web

# async 等价于 @asyncio.coroutine; await 等价于 yield from

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>',content_type='text/html')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name'] # request.match_info 指request请求内容中未知的部分 像这个例子就是'/hello/{name}里面的name
    return web.Response(body=text.encode('utf-8'),content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop) # web.Application 是aiohttp web moudle 中的类。看文档说服务器就相当于建立在这个类的实例上面app
    app.router.add_route('GET', '/', index) # router 应该指的是路径关系 app.router.add_route('GET', '/', index) 这个例子应该就是说 把request host+path'/' 放到index 函数中运行
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv
	
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()