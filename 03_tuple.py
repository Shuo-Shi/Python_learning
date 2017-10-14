#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 


classmates = ('Michael', 'Bob', 'Tracy') 
print('classmates =', classmates) 
print('len(classmates) =', len(classmates)) 
print('classmates[0] =', classmates[0]) 
print('classmates[1] =', classmates[1]) 
print('classmates[2] =', classmates[2]) 
# -1表示最后一项，同理-2表示倒数第二项
print('classmates[-1] =', classmates[-1]) 
 

# cannot modify tuple: 
classmates[0] = 'Adam' 
