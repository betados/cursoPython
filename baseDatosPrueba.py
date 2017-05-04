import sqlite3
def creaTabla():
    try:
        conn = sqlite3.connect('baseDatos.db')
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
        sql = """CREATE TABLE EMPLOYEE(
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT )"""
        cursor.execute(sql)
        conn.commit()
        print("tabla creada")

    except Exception as er:
        conn.rollback()
        print(er)
    finally:
        conn.close()

def meteDato():
    try:
        conn = sqlite3.connect('baseDatos.db')
        cursor = conn.cursor()
        # cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
        sql = """INSERT INTO EMPLOYEE(
        FIRST_NAME,
        LAST_NAME,
        AGE,
        SEX,
        INCOME)
        VALUES ('Alvaro','Torres',29,'v',2000)"""
        cursor.execute(sql)
        conn.commit()
        print("dato metido")

    except Exception as er:
        conn.rollback()
        print(er)
    finally:
        conn.close()

meteDato()

