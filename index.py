from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"


conn = sqlite3.connect('databased.db')
cursor.execute('CREATE TABLE IF NOT EXISTS example(id INTERGER PRIMARY KEY, name TEXT)')
conn.commit()
conn.close()

if __name__ == "__main__":
    app.run(debug = True)