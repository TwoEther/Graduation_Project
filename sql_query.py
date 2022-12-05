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
        author integer,
        category1 varchar(20),
        category2 varchar(20)
    );"""
    exc(sql)            
        
    sql = """create table category1 (
        id integer auto_increment primary key,
        category varchar(20)
    );"""
    exc(sql)  
    
    sql = """create table category2 (
        id integer auto_increment primary key,
        category varchar(20)
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
    
    sql = """
        create table comment (
        id integer auto_increment primary key,
        postnum integer,
        author integer,
        content varchar(100),
        created_at datetime
    );
    """
    exc(sql) 
    
def insertTable(table_name, values):
    def exc(table_name, value):
        global conn
        cur = conn.cursor()
        sql = "insert into "+table_name+ "(category) values (%s)"
        ptuple = tuple([value])
        
        try:
            cur.execute(sql, ptuple)
        except pymysql.err.OperationalError or pymysql.err.InterfaceError:
            pass
        else:
            conn.commit()
    for value in values: exc(table_name, value)
    
def select_all_table(table_list):
    def exc(sql, table_name):
        print('--------------{0}--------------'.format(table_name))
        global conn
        cursor = conn.cursor()
        cursor.execute(sql, table_name)
        result = cursor.fetchall()
        print(result)
    
    for table_name in table_list:
        sql = "select column_name from information_schema.columns where table_name=%s"
        exc(sql, table_name)
        
    
if __name__ == "__main__":
    conn = pymysql.connect(
        user='root', 
        passwd='ruddk1380',     # 비밀번호 바꾸기
        host='127.0.0.1',             
        db='mydb',             # db 바꾸기 
        charset='utf8'
    )
    table_list = ['post', 'photo', 'category1', 'category2', 'comment']
    category1_values = ['서울', '대전', '대구', '부산', '강원', '전라', '제주', '인천', '경기', '광주', '충청']
    category2_values = ['맛집', '숙소', '액티비티', '카페']
    
    dropTable(table_list)
    createTable()
    insertTable('category1', category1_values)
    insertTable('category2', category2_values)
    select_all_table(table_list)
    
    