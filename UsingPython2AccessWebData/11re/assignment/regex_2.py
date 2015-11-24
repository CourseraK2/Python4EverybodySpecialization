import re
reg = '[0-9]+'
#fh = open("regex_sum_42.txt",'r')

with open('regex_sum_182074.txt', 'r') as content_file:
    content = content_file.read()

list = re.findall(reg, content)

sum = 0;
for item in list:
    sum += int(item)

print sum
