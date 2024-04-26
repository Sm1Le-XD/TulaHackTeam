import psycopg2 as psql
import pprint
from config import NAME_DB, NAME_U, PASS, HOST

conn = psql.connect(dbname=NAME_DB, user=NAME_U,
                    password=PASS, host=HOST)
cur = conn.cursor()


def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS "
                "user_table("
                "id SERIAL PRIMARY KEY, "
                "tg_id INTEGER,"
                "telephone VARCHAR(15), "
                "email VARCHAR(25),"
                "password VARCHAR(25)), "
                "token VARCHAR(200),"
                "url_conn VARCHAR(300)")
    conn.commit()


def db_deader():
    cur.execute("CREATE TABLE IF NOT EXISTS "
                "dead_table("
                "id SERIAL PRIMARY KEY, "
                "cr_id INTEGER,"
                "name VARCHAR(35), "
                "surname VARCHAR(35),"
                "fathname VARCHAR(35), "
                "birth date,"
                "dead date,"
                "photo BYTEA)")
    conn.commit()


def add_db(text: str, *args) -> None:
    connect = psql.connect(dbname=NAME_DB, user=NAME_U, password=PASS, host=HOST)
    cursor = connect.cursor()
    cursor.execute(text, args)
    cursor.close()
    connect.commit()
    connect.close()


def answer_bd(text: str, *args) -> list:
    connect = psql.connect(dbname=NAME_DB, user=NAME_U, password=PASS, host=HOST)
    cursor = connect.cursor()
    cursor.execute(text, args)
    answer = cursor.fetchall()
    cursor.close()  # закрываем курсор
    connect.close()
    return answer


def add_user(id_user: int, phone: str, email: str) -> None:
    sql_query = "insert into user_table values (%s, %s, %s, %s)"
    add_db(sql_query, free_user_id(), id_user, phone, email)


def add_deader(*args):
    sql_query = "insert into dead_table values (%s, %s, %s, %s, %s, %s, %s)"
    add_db(sql_query, free_deader_id(), search_id_user(args[0]), *args[1:])


def free_user_id() -> int:
    all_users = answer_bd("SELECT * FROM user_table")
    if all_users:
        return max([i[0] for i in all_users]) + 1
    return 1


def free_deader_id() -> int:
    all_users = answer_bd("SELECT * FROM dead_table")
    if all_users:
        return max([i[0] for i in all_users]) + 1
    return 1


def search_id_user(id_user: int) -> int:
    users = answer_bd("SELECT * FROM user_table WHERE tg_id=%s", id_user)
    if len(users) == 0:
        return 0
    return users[0][0]



def search_id_dead(id_user: int) -> int:
    users = answer_bd("SELECT * FROM dead_table WHERE cr_id=%s", search_id_user(id_user))
    if len(users) == 0:
        return 0
    return users[-1][0]

def ret_data_dead(id: int) -> tuple:
    return answer_bd("select * from dead_table where id=%s", id)


def search_id_user_by_email(email: str) -> tuple:
    return answer_bd("select * from user_table where email=%s", email)[0][0]

# def get_token(id_user: int) -> str: