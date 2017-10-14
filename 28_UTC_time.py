# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta #从datetime模块导入datetime类

def to_timestamp(dt_str, tz_str):
    utc_split = re.split(r'[\C\:]+',tz_str) # 通过re自带的split函数，按照C和：将字符串分成3组
    # utc_hour = re.match(r'^UTC(.\d+):00',tz_str).group(1)
	# utc_hour = int(re.match(r'UTC([+|-][0-9]{1,2}):00',tz_str).group(1))
	
    utc_hour = int(utc_split[1]) # 将分组后中间那个包含UTC时区信息（+7或-09）的字段转换为数字后存储
    tz = timezone(timedelta(hours=utc_hour)) #根据之前存储的时区信息创建时区（datetime模块中timezone类的一个实例）
    
	cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S') # 将输入的日期和时间字符串转换为datetime，调用了datetime类的方法strptime()
    utc_time = cday.replace(tzinfo=tz) # 上面cday的时区属性tzinfo为默认的None，此时给cday设置新的时区信息，之后存储为utc_time
	
    return utc_time.timestamp() # 通过调用timestamp()方法把datetime类型转换为timestamp
	
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('t1=%s' % t1)
print('t2=%s\n' % t2)

print('Pass')
