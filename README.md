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
  <li> mysql-connector </li>
  <li> pandas </li>
  <li> base64 </li>
</ul>

<p> <b> <i> Steps to run the script that transfers task_data.csv information to database </i> </b> </p>
<ol>
  <li> Download the transfer_to_db.py from this repository. </li>
  <li> Place the task_data.csv file in the same folder, where transfer_to_db.py resides. </li>
  <li> Open transfer_to_db.py in an IDE, and run the file. </li>
</ol> 
<p> <b> <i> Steps to setup and run the web application to access the data </i> </b> </p>
<t><p> Once the above pre-requisites are in place, perform the below steps </p>
<ol>
  <li> Download/Clone this task_data repository and open the app.py in an IDLE. </li>
  <li> Run the app.py file, without changing any folder structure. </li>
  <li> Open a web browser and access the application using, <b>YOUR_IP_ADDRESS:8002</b></li>
</ol>

<h3> <u> Easy of Access</u> </h3>
<p> For easy of access to the application, without implementation, please go to https://www.maheshkrishnagopal.com/smart_steel_task


<h3> <u> Reference for User Interface </u> </h3>
<p> Since I am not an expert in UI design, I have referred the template from SoloDev as per link below, https://www.solodev.com/blog/web-design/adding-a-datetime-picker-to-your-forms.stml. However, the modification of the template as per the requirement are taken care as part of the assignment by me, as it is an open source code available on GitHub. Thanks to SoloDev.</p>

<h3> License </h3>
This project is licensed under GNU General Public License. Copyright (c) 2020 Maheshkrishna A G

