def han(n,x,y,z):
    if n == 1:
        print(x,'-->',z)
    else:
        han(n-1, x, z, y) #?将前n-1个盘子从x移到y上
        print(x,'-->',z)  #将底下的最后一个盘子从x移到z上
        han(n-1, y, x, z) #将y上的n-1个盘子移到z上

n = int(input('请输入汉诺塔的层数:'))
han(n, 'x', 'y', 'z')
