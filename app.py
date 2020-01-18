"""
Name: Task_Data Assignment
Author: Maheshkrishna A G
Description: This is Python Flask application main file, where, all the backend operations are handled.
Database: MySQL 8.0.16 in AWS RDS
Date: 19-Jan-2020
"""

from flask import Flask, render_template, request
import mysql.connector as mysql
from datetime import datetime
import base64

app = Flask(__name__)


@app.route('/')
def home():
    """
    home function '/' will be called when the application is accessed via localhost/URL. This functions do not perform
    any operation, however, delivers the home page of the web application to the end users.
    :return: renders the homepage.html to the User Interface.
    """

    return render_template("homepage.html")


@app.route('/result', methods=['POST', 'GET'])
def return_result():
    """
    return_result function (/result) will be called only when the form is submitted with the necessary details from the
    homepage.html. Since the form is submitted as a POST method, the function receives all its information and create a
    database entry for the search in PYTHON_TEST.LOG_MASTER table. Also, it fetches the information for the queried
    period from PYTHON_TEST.TASK_DATA table and delivers the information, if available, as result.html.
    In case of any exception or unable to connect to the database, this functions throws a different template,
    highlighting the error.

    :return: renders result.html with the desired information or renders exception.html in case of any exception being
                raised.
    """

    if request.method == 'POST':
        first_name = request.form['fname']
        last_name = request.form['lname']
        # start_date = datetime.strptime(request.form['start_time'], '%m/%d/%Y %I:%M %p').strftime("%Y-%m-%d %H:%M")
        # end_date = datetime.strptime(request.form['end_time'], '%m/%d/%Y %I:%M %p').strftime("%Y-%m-%d %H:%M")
        start_date = request.form['start_time']
        end_date = request.form['end_time']

        # Database Connectivity and Operations
        try:
            db = mysql.connect(host="python-db.cxxjqwuxxbfj.eu-west-1.rds.amazonaws.com", user="user_one",
                               passwd=base64.b64decode(b'TWFzdGVyIzEyMw=='.decode("utf-8")).decode("utf-8"),
                               db="python_test")
            curs = db.cursor()
            curs.execute("INSERT INTO LOG_MASTER (FIRST_NAME, LAST_NAME, QUERY_START_TIME, QUERY_END_TIME, "
                         "QUERIED_TIME) VALUES (%s,%s,%s,%s,%s)", (first_name, last_name, start_date, end_date,
                                                                   datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            curs.execute("SELECT * FROM TASK_DATA WHERE TIMESTAMP BETWEEN %s and %s", (start_date, end_date))
            records = curs.fetchall()
            db.commit()
            db.close()

        except Exception as e:
            return render_template("exception.html", msg=e)

    return render_template("result.html", data=records, start_date=start_date, end_date=end_date)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8002)
