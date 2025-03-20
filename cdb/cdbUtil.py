import sqlite3

def init_db():
    conn = sqlite3.connect("live_chat.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            voice TEXT
        )
    ''')
    conn.commit()
    conn.close()


def insert_chat(question, answer):
    conn = sqlite3.connect("live_chat.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chats (question, answer) VALUES (?, ?)", (question, answer))
    conn.commit()
    conn.close()


def get_answer(question):
    conn = sqlite3.connect("live_chat.db")
    cursor = conn.cursor()
    cursor.execute("SELECT answer FROM chats WHERE question = ?", (question,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "未找到匹配答案"

def get_answer_voice(question):
    conn = sqlite3.connect("live_chat.db")
    cursor = conn.cursor()
    cursor.execute("SELECT voice FROM chats WHERE question = ?", (question,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "未找到匹配答案"