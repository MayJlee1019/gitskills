#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time   : 2019/2/15 16:13
#@Author : Yun
#@File   : excl.py
import xlwt
import os
import datetime

book = xlwt.Workbook(encoding='utf-8', style_compression=0)
print(book)

sheet = book.add_sheet('test', cell_overwrite_ok=False)

sheet.write(0, 0, 'test01')
sheet.write(0, 1, 'test02')

test = 'asdasdads'

sheet.write(0,2, test.encode().decode('utf-8'))

style = xlwt.XFStyle()
font = xlwt.Font()
font.name = 'test'
font.bold = True
font.underline = True
font.italic = True
style.font = font
sheet.write(1, 0, '我是有样式的文字', style)

sheet.col(0).width = 256*20
sheet.row(0).set_style(xlwt.easyxf('font:height 720;'))

style.num_format_str = 'M/D/YY'
sheet.write(1, 1, datetime.datetime.now(), style)


a = os.path.abspath('')
book.save(r'%s\text.xls' % a)














