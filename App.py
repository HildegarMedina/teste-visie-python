#Modules
from flask import Flask, render_template, request, flash, redirect, url_for
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

#START: ROUTER

#Home
@app.route("/")
def index():

    #Cursor
    cur = mysql.connection.cursor()
    cur.execute("SELECT id_pessoa, nome , data_admissao FROM pessoas") #id_pessoa = id
    data = cur.fetchall()
    
    #Render
    return render_template("index.html", persons = data)

#Add person
@app.route("/add", methods = ["POST"])
def addPerson(): 
    if request.method == "POST":
        name = request.form["name"]
        date = request.form["date"]

        #Verify datas
        if name == "" or date == "":
            #Send message
            flash("Você precisa preencher todos os dados")
        else: 
            
            #Format date
            datatemp = date.split("-")
            
            #Cursor
            cur = mysql.connection.cursor()
            cur.execute("INSERT into pessoas (nome, data_admissao) VALUES(%s, %s)", (name, date))
            mysql.connection.commit()

            #Send message
            flash("Pessoa adicionada com sucesso")

        #Redirect
        return redirect(url_for("index"))

#Delete person
@app.route("/delete/<id>")
def deletePerson(id):

    #Cursor
    cur = mysql.connection.cursor()
    cur.execute("DELETE from pessoas WHERE id_pessoa = {0}".format(id))
    cur.connection.commit()

    #Send message
    flash("Pessoa eliminada com sucesso ")
    return redirect(url_for("index"))

#END: ROUTER

#Run server
if __name__ == '__main__':
    app.run(port = 3000, debug = True)