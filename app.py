# importing required libraries
from flask import *
from flask_mysqldb import MySQL
import MySQLdb.cursors

# instant of app 
app = Flask(__name__)


# connecting to MySQL engine and accessing database
app.config["MYSQL_HOST"]='localhost'
app.config["MYSQL_USER"]='rohit'
app.config["MYSQL_PASSWORD"]=''
app.config["MYSQL_DB"]='college'

mysql = MySQL(app)
app.secret_key = "andsoonthelifegoes"



##################################### THIS IS TESTING GROUND ###########################################
@app.route("/tabletest", methods=["GET", "POST"])
def tabletest():

     
    if request.method == "GET":
       cursor = mysql.connection.cursor()
       cursor.execute("SELECT * FROM faculty")
       faculty = cursor.fetchall()
    return render_template("tabletest.html", faculty=faculty)
    



########################################################################################################
######################################### DEFINING ROUTES ##############################################
########################################################################################################

# ADMIN PANEL
@app.route("/admin", methods=['GET'])
def admin():
    return "<html><h2>ADMIN PANEL<h2>""	<p>for performing day to day administrative task simply CRUD operation.</p>"
    
    
   
@app.route("/admin/faculty", methods=["GET"])
def adminfaculty():
    if request.method == "GET":
       cursor = mysql.connection.cursor()
       cursor.execute("SELECT * FROM faculty")
       faculty = cursor.fetchall()
    return render_template("adminfaculty.html", faculty=faculty)
    
@app.route("/admin/student", methods=["GET"])
def adminstudent():
    if request.method == "GET":
       cursor = mysql.connection.cursor()
       cursor.execute("SELECT * FROM first_year")
       student = cursor.fetchall()
    return render_template("adminstudent.html", student=student)
    
@app.route("/admin/course", methods=["GET"])
def admincourse():
    if request.method == "GET":
       cursor = mysql.connection.cursor()
       cursor.execute("SELECT * FROM course")
       course = cursor.fetchall()
    return render_template("admincourse.html", course=course)
    
    #if request.method == "POST":
    #   year = request.form["year"]
    #return render_template("admin.html")
 
# FACULTY PANEL

# STUDENT PANEL
       
# calling the function for starting app
if __name__ == '__main__':
   app.run
       
