import sqlite3

db_name = 'post.sqlite'
conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.cursor()

def do(query):
    cursor.execute(query)
    conn.commit()

def clear_db():
    ''' удаляет все таблицы '''
    open()
    query = '''DROP TABLE IF EXISTS posts'''
    do(query)
    close()


def make_db():
    open()
    posts_db = """CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY,
    head VARCHAR,
    describe VARCHAR,
    topic VARCHAR);"""
    
    do(posts_db)

    # start_post = [('Привет', 'это пост о там то то та тока тока', 'Криптовалюта')]
    # cursor.executemany("""INSERT INTO posts
    #                    (head, describe, topic)
    #                    VALUES (?, ?, ?)""", start_post)
    # do(posts_db)
    close()

#Все функции для фильтров бд

def filter_all():
    open()
    cursor.execute("SELECT * FROM posts ORDER BY id")
    posts_list = cursor.fetchall()
    close()
    return posts_list


def filter_crypto():
    open()
    cursor.execute("SELECT * FROM posts WHERE posts.topic == 'Криптовалюта'")
    posts_list = cursor.fetchall()
    close()
    return posts_list

def filter_sport():
    open()
    cursor.execute("SELECT * FROM posts WHERE posts.topic == 'Спорт'")
    posts_list = cursor.fetchall()
    close()
    return posts_list

def filter_streamers():
    open()
    cursor.execute("SELECT * FROM posts WHERE posts.topic == 'Стримеры'")
    posts_list = cursor.fetchall()
    close()
    return posts_list

def filter_music():
    open()
    cursor.execute("SELECT * FROM posts WHERE posts.topic == 'Музыка'")
    posts_list = cursor.fetchall()
    close()
    return posts_list

def filter_cybersport():
    open()
    cursor.execute("SELECT * FROM posts WHERE posts.topic == 'Киберспорт'")
    posts_list = cursor.fetchall()
    close()
    return posts_list

def filter_politic():
    open()
    cursor.execute("SELECT * FROM posts WHERE posts.topic == 'Политика'")
    posts_list = cursor.fetchall()
    close()
    return posts_list

#Конец всех функция для фильтров бд

def get_post():
    open()
    cursor.execute("SELECT * FROM posts ORDER BY id")
    posts_list = cursor.fetchall()
    close()
    return posts_list

def put_post(head, body, topic):
    open()
    put_list = [(head, body, topic)]
    cursor.executemany("""INSERT INTO posts
                       (head, describe, topic)
                       VALUES (?, ?, ?)""", put_list)
    conn.commit()
    close()


def main():
    #clear_db()
    make_db()