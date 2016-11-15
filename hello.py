#!/usr/bin/python
#-*- coding:utf-8 -*-

usr_name = input('Please input your name! \n')
print('Hello',usr_name,'!')

print('中文测试')

print ('Hi, %s, you have $%d.' % (usr_name, 1000000))
s1=72
s2=85
r=(s2-s1)/s1*100
print('小明成绩提升%.1f%%' %r)

mirai=b'\x44\x57\x41\x49\x0C\x56\x4A\x47\x0C\x52\x4D\x4E\x4B\x41\x47\x0C\x41\x4D\x4F\x22'.decode('unicode')
print(mirai)