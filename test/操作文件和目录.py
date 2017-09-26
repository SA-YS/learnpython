import os
import shutil

print(os.name)
# print(os.uname())
print(os.environ)
# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
os.path.join('D:/PyWorkspace/UtilDemo/test', 'testdir')
# 然后创建一个目录
os.mkdir('D:/PyWorkspace/UtilDemo/test/testdir3')
# 删掉一个目录
os.rmdir('D:/PyWorkspace/UtilDemo/test/testdir3')

print(os.path.split('D:/PyWorkspace/UtilDemo/test/abc.txt'))
print(os.path.splitext('D:/PyWorkspace/UtilDemo/test/abc.txt'))

# os.rename('test.txt', 'test.js')
os.remove('test.js')

# 复制文件os没有，使用shutil模块的copyfile()方法
