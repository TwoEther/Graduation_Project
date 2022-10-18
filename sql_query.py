'''
    pip install pymysql
    __main__ 에서의 db 바꾸기
    실행
'''

import pymysql

def dropTable():
    global conn
    cur = conn.cursor()
    sql = "drop table post"
    
    try:
        cur.execute(sql)
    except pymysql.err.OperationalError or pymysql.err.InterfaceError:
        pass
    else:
        conn.commit()
    
    sql = "drop table category"
    try:
        cur.execute(sql)
    except pymysql.err.OperationalError or pymysql.err.InterfaceError:
        pass
    else:
        conn.commit()

    sql = "drop table user"
    try:
        cur.execute(sql)
    except pymysql.err.OperationalError or pymysql.err.InterfaceError:
        pass
    else:
        conn.commit()

def createTable():
    global conn
    try:
        with conn.cursor() as cursor: 
            sql = """create table post (  
                PN	integer auto_increment primary key , 
                title varchar(50),  
                created_at date,
                content varchar(1000),
                head_image varchar(250),
                author varchar(20),
                category varchar(20)
            );"""
            
            cursor.execute(sql)
            conn.commit()
    finally:
        pass
    
    try:
        with conn.cursor() as cursor: 
            sql = """create table category (
                name varchar(20) primary key
            );"""
                        
            cursor.execute(sql)
            conn.commit()
    finally:
        pass
    
    try:
        with conn.cursor() as cursor: 
            sql = """create table user (
            id varchar(20) primary key,
            passwd varchar(20),
            nickname varchar(20),
            UNIQUE index (nickname)     
        );"""
                        
            cursor.execute(sql)
            conn.commit()
    finally:
        pass

    try:
        with conn.cursor() as cursor: 
            sql = """ALTER TABLE post ADD FOREIGN KEY(author) REFERENCES user(nickname);"""
            cursor.execute(sql)
            conn.commit()
    finally:
        pass
    
    try:
        with conn.cursor() as cursor: 
            sql = """ALTER TABLE post ADD FOREIGN KEY(category) REFERENCES category(name);"""
            cursor.execute(sql)
            conn.commit()
    finally:
        pass

if __name__ == "__main__":
    conn = pymysql.connect(
        user='root', 
        passwd='rootuser',     # 비밀번호 바꾸기
        host='127.0.0.1',             
        db='mydb',             # db 바꾸기 
        charset='utf8'
    )

    dropTable()
    createTable()
