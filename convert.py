#coding:utf-8
import codecs
import xlsxwriter

workbook = xlsxwriter.Workbook('sheet2.xlsx')
worksheet = workbook.add_worksheet()

fo = codecs.getreader('utf-8')(open('sheet2.csv','rb'))

list = []
inlist = []

for i,line in enumerate(fo):
  for k in line.split('\t'):
    inlist.append(k.strip('\n\r'))
  list.append(inlist)
  inlist = []

row = 0
col = 0

for a,b,c,d,e,f in (list):
    worksheet.write(row, col,     a)
    worksheet.write(row, col + 1, b)
    worksheet.write(row, col + 2, c)
    worksheet.write(row, col + 3, d)
    worksheet.write(row, col + 4, e)
    worksheet.write(row, col + 5, f)
    row += 1

workbook.close()
