import sqlite3
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Initialize a dummy database
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    cursor.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'admin', 'admin123')")
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return '''
        <h2>Secure Coding Review Demo</h2>
        <form action="/login" method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

# VULNERABLE ROUTE: SQL Injection vulnerability
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # UNSAFE: Direct string formatting allows SQL Injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"Executing Query: {query}") # For debugging audit
    
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return f"<h3>Welcome back, {username}! (Login Successful)</h3>"
    else:
        return "<h3>Invalid Credentials!</h3>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
