import mysql.connector

db_ini = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'user_student',
    'password' : 'pass_221',
    'database' : 'server_221',
    'charset' : 'utf8mb4',
    'use_unicode' : True,
}


db_connection = None

def connect_db() :
    global db_connection
    try:
        db_connection = mysql.connector.connect( **db_ini)
    except mysql.connector.Error as err :
        print(err)
    else :
        print("Connection OK")


def close_connection() :
    db_connection.close()


def show_uuid():
    sql = """select uuid(), uuid() 
    union all 
    select uuid(), uuid() 
    union all 
    select uuid(), uuid()"""
    global db_connection                         
    if db_connection is None : return             
    try :                                        
        cursor = db_connection.cursor()                     
        cursor.execute(sql)
        rows = cursor.fetchall()   
        cols = [desc[0] for desc in cursor.description]
        print(f"{cols[0]:<40} | {cols[1]:<40}")
        print("-"*83)
        for row in rows :
            print(f"{row[0]:<40} | {row[1]:<40}")

    except mysql.connector.Error as err :        
        print(err)                                
        print(sql)
    else :                                       
        for row in cursor :                      
            print(row)                           
    finally :                                    
        cursor.close()   


def main() :
    connect_db()
    show_uuid()
   
    close_connection()


if __name__ == '__main__' :
    main()