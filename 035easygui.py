import easygui as g
import sys

while 1:
    g.msgbox('hi,欢迎进入第一个界面小游戏~')

    msg = '请问你最近学习到什么知识呢?'
    title = '小游戏互动'
    choices = ['谈恋爱', '编程', 'ooxx', '琴棋书画']

    choice = g.choicebox(msg, title, choices)#选择对话框

    g.msgbox('你的选择是:' + str(choice), '结果')

    msg = '你希望重新开始小游戏吗?'
    tiltle = '请选择'

    if g.ccbox(msg, title):#继续对话框
        pass
    else:
        sys.exit(0)
