# coding:utf-8
import pymysql


if __name__ == "__main__":
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='lq86478528', db='test')
    cursor = conn.cursor()
    # 创建user表:
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    # 插入一行记录，注意MySQL的占位符是%s:
    cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
    cursor.executemany('insert into user (id, name) values (%s, %s)', [('11', 'Dog'), ('2', 'Bob')])

    # 提交事务:
    conn.commit()
    cursor.close()
    # 运行查询:
    cursor = conn.cursor()
    cursor.execute('select * from user where id = %s', ('1',))
    values = cursor.fetchall()
    for line in values:
        print(line)
    # 关闭Cursor和Connection:
    cursor.close()
