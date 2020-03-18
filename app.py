from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import datetime
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'

@app.route('/', methods = ['GET', 'POST'])
def index():
    return(render_template('index.html'))

@app.route('/employee_add', methods = ['GET', 'POST'])
def employee_update():
    today = datetime.datetime.now()
    month_num = today.strftime("%m")
    year_num = today.strftime("%y")

    if request.method == "POST":
        details = request.__format__
        firstName = details['fname']
        lastName = details['lname']
        emailAdd = details['email']
        phoneNum = details['phone']
        birthDate = details['birthdate']
        empID = lower(firstName[0]+lastName[0]+month_num+year_num)

        cur = mysql.connection.cursor()
        cur.execute("""INSERT INTO Employees(
                        empID,
                        firstName,
                        lastName,
                        emailAdd,
                        phoneNum,
                        birthDate)
                    VALUES(
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                    )
        );""")

    return(render_template('employee_update.html'))



if __name__ == '__main__':
    app.run()