#Modules
from flask import Flask, render_template
from flask_mysqldb import MySQL

#Initializations
app = Flask(__name__)

#Config
app.config["MYSQL_HOST"] = "db4free.net"
app.config["MYSQL_USER"] = "visie_user"
app.config["MYSQL_PASSWORD"] = "visie_pass"
app.config["MYSQL_DB"] = "visie_db"
app.secret_key = "mysecretkey"

#Connect with database
mysql = MySQL(app)

#ROUTER
#Home
@app.route("/")
def index():

    #Cursor
    cur = mysql.connection.cursor()
    cur.execute("SELECT nome , data_admissao FROM pessoas") #id_pessoa = id
    data = cur.fetchall()
    
    #Render
    return render_template("index.html", persons = data)

#Run server
if __name__ == '__main__':
    app.run(port = 3000, debug = True)