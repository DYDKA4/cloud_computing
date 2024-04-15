import json

from flask import Flask
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mysql_db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'example'
app.config['MYSQL_DB'] = 'stage'

mysql = MySQL(app)  # this is the instantiation
@app.route('/')
def hello_world():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT id, name FROM example_table''')
    rv = cur.fetchall()
    return str(rv)
# @app.route('/user/<username>')
# def username():

@app.route('/add/<username>')
def add_user(username):
    # name = request.args.get('name', type = str)
    cur = mysql.connection.cursor()
    print(f'''INSERT INTO example_table (name) VALUES ('{username}');''')
    cur.execute(f'''INSERT INTO example_table (name) VALUES ('{username}');''')
    mysql.connection.commit()
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/delete/<id>')
def del_user(id):
    cur = mysql.connection.cursor()
    cur.execute(f'''DELETE FROM example_table WHERE id = {int(id)}''')
    mysql.connection.commit()
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)