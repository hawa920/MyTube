import re

cview = '觀看次數：6,335,057'
clike = '12萬'
chate = '1,540'
pubtime = '發佈日期：2018年3月23日'
subscribe = '訂閱 (40萬)'

if '萬' in clike:
    print("GOOD")


temp = re.findall('\d', cview)
temp = ''.join(temp)
print(temp)

temp = clike.replace('萬', '0000')
temp = re.findall('\d', temp)
temp = ''.join(temp)
print(temp)