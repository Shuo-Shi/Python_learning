#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
print('\n')

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [(s.lower() if isinstance(s, str) else s) for s in L1]
L3 = [s.lower() for s in L1 if isinstance(s, str)]

print ('Original list is:')
print (L1,'\n')
print ('[(s.lower() if isinstance(s, str) else s) for s in L1]')
print (L2,'\n')
print ('[s.lower() for s in L1 if isinstance(s, str)]')
print (L3,'\n')