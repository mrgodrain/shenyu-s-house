def save_file(boy, girl, count):#封装
    #文件分别保存
    file_name_boy = 'boy' + str(count) + '.txt'#定义变量
    file_name_girl = 'girl' + str(count) + '.txt'

    boy_file = open(file_name_boy,'w')#打开文件
    girl_file = open(file_name_girl,'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()


#主函数
def split_file(file_name):#封装
    f = open(file_name)

    boy = []#初始化一个列表
    girl =[]
    count = 1#初始化一个计算器

    for each_line in f:
        if each_line[:6] != '======':
            #这里进行字符串分割操作
            (role, line_spoken) = each_line.split(':',1)#先定义一个元祖,从':'右边切,分割一次返回两个字符串
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '客服':
                girl.append(line_spoken)
        else:                        
            save_file(boy, girl ,count)#调用函数

            boy = []
            girl = []
            count += 1
    save_file(boy, girl, count)
    f.close()

split_file('record.txt')
