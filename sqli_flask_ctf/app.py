from flask import Flask, request, render_template_string, redirect, url_for,render_template
import sqlite3

app = Flask(__name__)


DATABASE = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, flag TEXT)')
    conn.execute("INSERT OR REPLACE INTO users VALUES (1, 'jnikcdmkcweidfj', 'sygdweudjsaxsl@2152417', 'LakshyaCTF{SQLi_m@st3ry}')")
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        cur = conn.cursor()
        
        
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        cur.execute(query)
        user = cur.fetchone()
        
        if user:
            return f"Logged in successfully! Here is the flag: {user['flag']}"
        else:
            msg = 'Incorrect username or password!'
        
        conn.close()
    return render_template('login.html', msg=msg)

if __name__ == '__main__':
    init_db()
    app.run()
