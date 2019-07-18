"""
    模拟登录注册
"""
import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')
cur = db.cursor()


def login():
    user = input("请输入账号:")
    password = input("请输入密码:")
    sql = "select password from user where name =%s"
    cur.execute(sql, [user])
    if password == cur.fetchone()[0]:
        return True
    return False


def register():
    user = input("请输入账号:")
    password = input("请输入密码:")

    sql = "select * from user where name =%s"
    cur.execute(sql,[user])
    result=cur.fetchone()
    if result:
        return False
    try:
        sql = "insert into user (name,password) value(%s,%s)"
        cur.execute(sql, [user, password])
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        print(e)
        return False


def main():
    while True:
        choise = input("请选择序号:1.注册 2.登录")
        if choise == '1':
            if register():
                print("注册成功")
            else:
                print("注册失败")
        elif choise == '2':
            if login():
                print("登录成功")
            else:
                print("登录失败")
        else:
            print("请选择正确的选项")


if __name__ == '__main__':
    main()
    print("修改内容")
    print("测试代码")
