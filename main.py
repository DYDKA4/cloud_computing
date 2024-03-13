from flask import Flask
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mysql_db'
app.config['MYSQL_USER'] = 'example'
app.config['MYSQL_PASSWORD'] = 'secret2'
app.config['MYSQL_DB'] = 'cloud_computing'

mysql = MySQL(app)  # this is the instantiation
@app.route('/')
def hello_world():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT name FROM example_table''')
    rv = cur.fetchall()
    return str(rv)
# @app.route('/user/<username>')
# def username():

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)