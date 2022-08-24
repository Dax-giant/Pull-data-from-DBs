# Pull-data-from-DBs

Pull data from Databases is an open source program under GNU GENERAL PUBLIC LICENSE built with python programming language, to help data analysts and Business intelligence(BI) analyst to pull data from different database management system (DBMS).with this program you can pull one specific table from databases or all tables in the specific database and get those tables on CSV, EXCEL, JSON files. The program support the following types of DBMS :

1 - SQL : MySQL and PostgreSQL
2 - NoSQL : MongoDB 

Let me put you in picture with the simple idea behind this program, Pandas library is the core, How that?the program connect to one of the three DBMS(MySQL, PostgreSQL or MongoDB) you can choose from, than read tables from database and changing them to Dataframe object which is a built-in class in Pandas by the help of SQLAlchemy which is an Object Relational Mapper, then convert the existing dataframe to one the three data files (CSV, EXCEL or JSON). 

So what's next? 
You can contribute as developer, to make a GUI (Graphical User Interface), finding bugs and debug them.
