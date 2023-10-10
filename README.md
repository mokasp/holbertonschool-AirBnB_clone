<img src="https://github.com/michaellgans/holbertonschool-AirBnB_clone/assets/131380667/182c95ff-f86f-4d0e-b90e-8e32e5fce600" alt="Holberton-Logo-v1" width="70%"><img src="https://github.com/michaellgans/holbertonschool-AirBnB_clone/assets/131380667/3fda5c96-065b-44cb-a43c-6b2bfaea5792" alt="airbnb-2-logo-png-transparent" width="25%">

**Hello!** :wave: <br>
&nbsp;&nbsp;&nbsp;&nbsp;Thank you for taking interest in our AirB&B project.  This is the first part of a multi-week partner project where my partner Kasper and I will recreate the layers of a replica of the AirB&B website.  In this ReadMe, we'll review the parts of the project as a whole, then dive into the current project itself. <br>

**Any comments or feedback is greatly appreciated!** <br>
[Contact Us](https://github.com/michaellgans/holbertonschool-AirBnB_clone/blob/main/AUTHORS)

## AirB&B - Looking Ahead
<p align="center">
  <img src="https://github.com/michaellgans/holbertonschool-AirBnB_clone/assets/131380667/3462933e-8dab-49cc-91e9-772892287803" alt="Pic1" width="75%">
</p>

&nbsp;&nbsp;&nbsp;&nbsp;The AirB&B website allows users to either list properties they would like to host on the website, or browse properties they would like to rent for a vacation!  The overarching project is broken down into six layers: <br>

<details><summary>The Console</summary>

&nbsp;&nbsp;&nbsp;&nbsp;The first step is to create a storage engine which will allow us to save and reload objects created. Because of this, multiple objects can be created inside the command interpreter and saved for later use once the RestAPI is created.<br>
- Creates a data model.
- Manages objects by interacting with the console, a command line interpereter.
  - Create objects
  - Update objects
  - Display objects
  - Destroy objects
- Saves objects to a JSON file.</details>

<details><summary>Web Static</summary>

&nbsp;&nbsp;&nbsp;&nbsp;The second step is to create the static website or application.  In this step, we'll learn both HTML and CSS, as well as how to create multiple objects on the webpage.<br>
- Learning Objectvies
  - HTML/CSS
  - Create the HTML of your application.
  - Create the template of each object.</details>

<details><summary>MySQL Storage</summary>

&nbsp;&nbsp;&nbsp;&nbsp;The third step is to upgrade our storage engine by replacing it with a fully functioning database system.<br>
- Learning Objectvies
  - SQL/MySQL
  - Design and create a database for storage.
  - Map our models to a table in the database using Object-Relational Mapping (ORM).</details>

<details><summary>Web Framework - Templating</summary>

&nbsp;&nbsp;&nbsp;&nbsp;The fourth step is to create a webserver using Python and Flask.  This will link the storage engine and the static website.<br>
- Learning Objectvies
  - Understand how to use Flask.
  - Create our first web server in Python.</details>

<details><summary>RESTful API</summary>

&nbsp;&nbsp;&nbsp;&nbsp;The fifth step is to expose the objects stored in a JSON web interface.<br>
- Learning Objectvies
  - What is an API?
  - Link JSON web interface to the database.
  - Manipulate objects via RESTful API and Flask.</details>

<details><summary>Web Dynamic</summary>

&nbsp;&nbsp;&nbsp;&nbsp;The final step is to use Javascript to make the website dynamic!<br>
- Learning Objectvies
  - JQuery/Javascript
  - Load objects from the user via the RESTful API.</details>

## AirB&B - The Console

&nbsp;&nbsp;&nbsp;&nbsp;A command line interpreter is a program that interacts with a file storage engine, which allows the user to create, destroy, modify, and display objects stored in a JSON file.  The console is programmed through a driver file (`console.py`), which accepts interactive and non-interactive commands, meaning that either a machine or a person can manipulate the program.  By using the module `cmd`, we were able to write our own commands, as well as have them display custom help text for easy troubleshooting.

Command | Description | Help Text
--- | --- | ---
`all` | Displays all objects currently stored. | Enter the command "all" to print everything in storage.
`all <class>` | Displays all objects currently stored with indicated class. | Enter the command "all <class>" to print anything created with that class.
`create` | Creates an object and generates a unique ID. | Enter the command "create <class>" to make a new Object.
`destroy` | Destroys an object. | Enter the command "destroy <class> <id>" to remove that specific object
`EOF` | Exits the program and returns to the command line. | Enter the command "EOF" to quit the program
`help` | Displays all commands available to the user. | List available commands with "help" or detailed help with "help cmd".
`help <command>` | Displays the help text about the command. | List available commands with "help" or detailed help with "help cmd".
`quit` | Exits the program and returns to the command line. | Enter the command "quit" to exit the program.
`show` | Displays the object indicated by ID. | Enter the command "show <class> <id>" to display that specific object
`update` | Updates an existing object with a new attribute and value. | Enter the command: update <class> <id> <new attribute> "<new attribute value>" to add a new attribute to an instance of the specific class.

FILESTORAGE: manages serialization and deserialization flow of Python Objects and JSON objects. Also allows for creation and deletion on Objects, while keeping the JSON file updated. 

 

BASEMODEL: the base of all classes that will allow all classes to have a unique ID and the times in which the instances of the classes were created or updated at. Allows for all classes inherited from it to accession function that reformats a dictionary to be JSON serializable, as well as saving new and updated instances to the Storage. 

### How to Start the Console

- how to start it
- 
### How to Use the Console

- how to use it

### examples

- To be added

#### Resources
- [Original Website](https://www.airbnb.com/)
