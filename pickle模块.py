#初始化一个列表
my_list = [123, '你好', ['another list']]

#导入泡菜模块
import pickle
pickle_file = open('my_list.pkl', 'wb')
pickle.dump(my_list, pickle_file)#倾倒
pickle_file.close()


#读取
pickle_file = open('my_list.pkl', 'rb')#二进制,open把磁盘中的文件加载到内存中
my_list2 = pickle.load(pickle_file)
print(my_list2)
