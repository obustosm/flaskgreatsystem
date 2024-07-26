from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_object('config.Config')

mysql = MySQL(app)

@app.route('/')
def index():
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM some_table")  # Usa el nombre correcto de la tabla aquí
    results = cursor.fetchall()
    cursor.close()
    return str(results)

if __name__ == '__main__':
    app.run(debug=True)
