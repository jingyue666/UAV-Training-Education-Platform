import sqlite3
from datetime import datetime

def init_database():
    """初始化数据库"""
    conn = sqlite3.connect('drone_platform.db')
    cursor = conn.cursor()
    
    # 用户表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        real_name TEXT,
        id_card TEXT,
        phone TEXT,
        role TEXT,  -- 学员/接单员/企业/管理员
        level TEXT,  -- 初级/中级/高级
        points INTEGER DEFAULT 0,
        balance REAL DEFAULT 0,
        status TEXT DEFAULT 'active',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # 课程表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        level TEXT,
        specialty TEXT,
        price REAL,
        duration INTEGER,
        video_url TEXT,
        resources TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # 订单表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        client_id INTEGER,
        pilot_id INTEGER,
        price REAL,
        status TEXT,
        location TEXT,
        deadline DATE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (client_id) REFERENCES users (id),
        FOREIGN KEY (pilot_id) REFERENCES users (id)
    )
    ''')
    
    # 学习记录表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS learning_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        course_id INTEGER,
        progress REAL DEFAULT 0,
        score REAL,
        completed BOOLEAN DEFAULT FALSE,
        completed_date DATE,
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (course_id) REFERENCES courses (id)
    )
    ''')
    
    conn.commit()
    conn.close()
