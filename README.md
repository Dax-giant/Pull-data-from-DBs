# Pull-data-from-DBs

Pull data from Databases is an open source program under GNU GENERAL PUBLIC LICENSE built with python programming language, to help data analysts and Business intelligence(BI) analyst to pull data from different database management system (DBMS).with this program you can pull one specific table from databases or all tables in the specific database and get those tables on CSV, EXCEL, JSON files. The program support the following types of DBMS :

1. SQL : MySQL and PostgreSQL
2. NoSQL : MongoDB 

Let me put you in picture with the simple idea behind this program, Pandas library is the core, How that?the program connect to one of the three DBMS(MySQL, PostgreSQL or MongoDB) you can choose from, than read tables from database and changing them to Dataframe object which is a built-in class in Pandas by the help of SQLAlchemy which is an Object Relational Mapper, then convert the existing dataframe to one the three data files (CSV, EXCEL or JSON). 

Libraries and modules used in project:

1. mysql.connector
Python module to connect with MySQL database management system
2. psycopg2
Python library to connect with PostgreSQL database management system
3. Pandas
Python library to handle tabular data by making them a dataframes object
4. SQLAlchemy
Python library used to map SQL tables with pandas classes
5. getpass
Python module to Prompt the user for a password without echoing
6. Pymongo
Python library to connect with MongoDb database management system.


So what's next? 
You can contribute as developer, to make a GUI (Graphical User Interface), finding bugs and debug them.
