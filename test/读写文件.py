# try:
#     f = open('test.txt', 'r')
#     str = f.read()
#     print(str)
# finally:
#     if f:
#         f.close()

with open('test.txt', 'r') as f:
    print(f.read())

f = open('D:/test.png', 'rb')
print(f.read())

f = open('D:/test.txt', 'a')
f.write('nihao\n')
f.close()
