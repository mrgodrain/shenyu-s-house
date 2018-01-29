try:
    f = open('why i am a file.txt', 'w')
    int('abc')
    sum = 1 + '1'
    print(f.write('i am exit@_@'))
    
except OSError as reason:
    print('文件出错啦T_T \n 错误的原因是:' + str(reason))
except TypeError as reason:
    print('类型出错啦~' + str (reason))
except ValueError as reason:
    print('值出错啦~' + str (reason))

finally:
    f.close
    print('我爱你!')
