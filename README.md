<h2 align="center"> Smart Steel Technologies Task v0.1 </h2>

<p> The task is to load a csv data into a database and that shall be served as a web application to query the loaded information. The web application leverages information from MySQL database and serve it to the users, as per the request. </p>

<h3> <u> Technology Stack </u> </h3>
<ul>
  <li> Python - As a backend language for scripting. </li>
  <li> Flask - Python's micro framework for creating web applications. </li>
  <li> MySQL - Database. </li>
  <li> HTML, CSS, JavaScript - User Interface / Frontend </li>
  <li> AWS RDS - MySQL resides in AWS </li>
</ul>

<h3> <u> Code Style </u> </h3>
This task has been developed as per the PEP8 standards.

<h3> <u> SetUp and Implementation</u> </h3>
<p> <b> <i> Pre-requisites </i> </b> </p>
<p> To setup and run this application, Python 3+ is required along with the below modules.
<ul>
  <li> Flask </li>
  <li> mysql-connector-python </li>
  <li> pandas </li>
  <li> base64 </li>
</ul>

<p> <b> <i> Steps to run the script that transfers task_data.csv information to database </i> </b> </p>
<ol>
  <li> Download the transfer_to_db.py from this repository. </li>
  <li> Open the file in a IDE, provide the actual file path at Line No. 13 and run the file. </li>
</ol> 
<p> <b> <i> Steps to setup and run the web application to access the data </i> </b> </p>
&nbsp;<p> Once the above pre-requisites are in place, perform the below steps </p>
<ol>
  <li> Download/Clone this task_data repository and open the app.py in an IDLE. </li>
  <li> Run the app.py file, without changing any folder structure. </li>
  <li> Open a web browser and access the application using, <b>YOUR_IP_ADDRESS:8002</b></li>
</ol>

<h3> License </h3>
This project is licensed under GNU General Public License. Copyright (c) 2020 Maheshkrishna A G

