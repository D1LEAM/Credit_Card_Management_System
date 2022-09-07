# 导入界面模块
from tkinter import *

from tkinter import messagebox
# 导入弹框
from tkinter.simpledialog import *
# 导入表格模具
from tkinter.ttk import Treeview

from pojo import Book
# 导入dao层
from dao import BookDao

# 导入提示框

bd = BookDao()
# 新建界面
window = Tk()
window.title('银行信用卡客户管理系统')
# 调整页面的大小 widthxheight+x+y
window.geometry('800x500')

# 新建一个表格
table = Treeview(columns=('RowNumber', 'CustomerId', 'Surname', 'CreditScore', 'Geography', 'Gender', 'Age', 'Tenure',
                          'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 'Exited'),
                 show="headings")

table.column('RowNumber', width=20)
table.column('CustomerId', width=50)
table.column('Surname', width=35)
table.column('CreditScore', width=30)
table.column('Geography', width=30)
table.column('Gender', width=40)
table.column('Age', width=25)
table.column('Tenure', width=25)
table.column('Balance', width=60)
table.column('NumOfProducts', width=60)
table.column('HasCrCard', width=70)
table.column('IsActiveMember', width=50)
table.column('EstimatedSalary', width=50)
table.column('Exited', width=50)

table.heading('RowNumber', text='编号')
table.heading('CustomerId', text='客户ID')
table.heading('Surname', text='姓名')
table.heading('CreditScore', text='信用分')
table.heading('Geography', text='国家')
table.heading('Gender', text='性别')
table.heading('Age', text='年龄')
table.heading('Tenure', text='卡龄')
table.heading('Balance', text='存贷款情况')
table.heading('NumOfProducts', text='使用产品数')
table.heading('HasCrCard', text='是否为本行卡')
table.heading('IsActiveMember', text='是否活跃')
table.heading('EstimatedSalary', text='预估收入')
table.heading('Exited', text='是否流失')
# 放置控件，rel*表示使用相对定位，相对于父容器的定位
# table.place(relx=0.004, rely=0.028, relwidth=0.964, relheight=0.95)
"""
定义滚动条控件
orient为滚动条的方向，vertical--纵向，horizontal--横向
command=self.tree.yview 将滚动条绑定到treeview控件的Y轴
"""
table.VScroll1 = Scrollbar(orient='vertical', command=table.yview)
table.VScroll1.place(relx=0.981, rely=0.035, relwidth=0.018, relheight=0.758)
# 给treeview添加配置
table.configure(yscrollcommand=table.VScroll1.set)


def load():
    # 清除表格的数据
    for i in table.get_children():
        table.delete(i)
    # 先读出数据库的数据
    for i in bd.list_book():
        # 将数据加入到表格中
        table.insert('', END, value=i)


def add():
    # RowNumber = askinteger('提示', '请输入编号')
    CustomerId = askinteger('提示', '请输入客户ID')
    Surname = askstring('提示', '请输入姓名')
    CreditScore = askinteger('提示', '请输入信用分')
    Geography = askstring('提示', '请输入国家')
    Gender = askstring('提示', '请输入性别')
    Age = askinteger('提示', '请输入年龄')
    Tenure = askinteger('提示', '请输入卡龄')
    Balance = askinteger('提示', '请输入存贷款情况')
    NumOfProducts = askinteger('提示', '请输入产品数量')
    HasCrCard = askinteger('提示', '是否为本行信用卡')
    IsActiveMember = askinteger('提示', '是否为活跃用户')
    EstimatedSalary = askfloat('提示', '估计收入')
    Exited = askinteger('提示', '是否流失')
    if CustomerId is not None:
        r = bd.add_book(
            Book(CustomerId=CustomerId, Surname=Surname, CreditScore=CreditScore,
                 Geography=Geography, Gender=Gender,
                 Age=Age, Tenure=Tenure, Balance=Balance, NumOfProducts=NumOfProducts, HasCrCard=HasCrCard,
                 IsActiveMember=IsActiveMember, EstimatedSalary=EstimatedSalary, Exited=Exited))
        messagebox.showinfo(r)
    else:
        r = bd.add_book(Book(CustomerId=CustomerId, Surname=Surname, CreditScore=CreditScore,
                             Geography=Geography, Gender=Gender,
                             Age=Age, Tenure=Tenure, Balance=Balance, NumOfProducts=NumOfProducts, HasCrCard=HasCrCard,
                             IsActiveMember=IsActiveMember, EstimatedSalary=EstimatedSalary, Exited=Exited))
        messagebox.showerror(r)
    load()


def delete():
    global ids
    if messagebox.askyesno('提示', '是否删除'):
        ids = []
    # 制作多选删除
    for i in table.selection():
        # i是元素的id
        # item 根据id拿对应的数据
        ids.append(table.item(i)['values'][0])
    if len(table.selection()) == 0:
        CustomerId = askinteger('提示', '请输入客户ID')
        ids.append(CustomerId)
    for i in ids:
        bd.del_book(Book(CustomerId=i))
        load()


Button(text='加 载', command=load).place(x=200, y=430)
Button(text='增 加', command=add).place(x=400, y=430)
Button(text='删 除', command=delete).place(x=600, y=430)

# 让表格显示
table.place(width=800, height=400)
# 让界面显示
window.mainloop()
