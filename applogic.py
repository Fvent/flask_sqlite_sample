from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")

@app.route("/")
def formIn():
    return render_template("formin.html")

@app.route("/queryOut")
def queryOut():
    return render_template("queryOut.html")

@app.route('/postform',methods = ['POST', 'GET'])
def postform():
   if (request.method == 'POST'):
      try:
         nm = request.form['nm']
         addr = request.form['addr']
         empid = request.form['idn']
         
         con = sql.connect("appdb.db")
         cur = con.cursor()
         cur.execute("INSERT INTO employee (id, name, address) VALUES (?,?,?)",(empid, nm , addr))
            
         con.commit()
         msg = "Record successfully added"

         con.close()

      except:
        #  con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("queryOut.html",msg = msg)
         

@app.route('/emplist')
def emplist():
   con = sql.connect("appdb.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from employee")
   
   rows = cur.fetchall();
   return render_template("emplist.html",rows = rows)
   
   
if __name__ == "__main__":
    app.run()

