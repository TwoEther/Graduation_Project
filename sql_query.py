'''
    pip install pymysql
    __main__ 에서의 db 바꾸기
    실행
'''


import pymysql


def dropTable(table_list):
    def exc(tableName):
        global conn
        cur = conn.cursor()
        sql = "drop table "+tableName
        
        try:
            cur.execute(sql)
        except pymysql.err.OperationalError or pymysql.err.InterfaceError:
            pass
        else:
            conn.commit()
    
    for table in table_list: exc(table)
        
    

def createTable():
    def exc(sql):
        global conn
        try:
            with conn.cursor() as cursor: 
                cursor.execute(sql)
                conn.commit()
                
        finally:
            pass
        
    sql = """create table post (  
        PN	integer auto_increment primary key , 
        title varchar(50),  
        created_at date,
        content varchar(1000),
        head_image varchar(250),
        author varchar(20),
        main_category varchar(20)
    );"""
    exc(sql)            
        
    sql = """create table category (
        id integer auto_increment primary key,
        main_category varchar(20)
    );"""
    exc(sql)                   
        
    sql = """create table user (
        id varchar(20) primary key,
        passwd varchar(20),
        nickname varchar(20),
        UNIQUE index (nickname)     
    );"""
    exc(sql) 
                        
    sql = """
        create table photo (
        id integer auto_increment primary key,
        postnum integer,
        image varchar(250)
    );
    """
    exc(sql) 
    
if __name__ == "__main__":
    conn = pymysql.connect(
        user='root', 
        passwd='rootuser',     # 비밀번호 바꾸기
        host='127.0.0.1',             
        db='mydb',             # db 바꾸기 
        charset='utf8'
    )
    table_list = ['post', 'category', 'photo', 'user']
    dropTable(table_list)
    createTable()
