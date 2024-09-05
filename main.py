from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# estanciando e configurando mysql

mysql = MySQL()

# dados da conexão 

Host = 'localhost'
Port = 3306
User = 'root'
Pass = ''
Database = 'db-crud'

app.config['MYSQL_HOST'] = Host
app.config['MYSQL_PORT'] = Port
app.config['MYSQL_USER'] = User
app.config['MYSQL_PASSWORD'] = Pass
app.config['MYSQL_DB'] = Database

mysql.init_app(app)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clientes')
def index_clientes():

    # Criando consulta p1
    sql = 'SELECT * FROM clientes'

    conexao = mysql.connection
    cursor = conexao.cursor()
    cursor.execute(sql)
    clientes=cursor.fetchall()
    conexao.commit()

    return render_template('modulos/clientes/index.html', clientes_t = clientes)





if __name__ == '__main__':
    app.run(debug=True)