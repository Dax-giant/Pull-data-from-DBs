# Importing MySQL connector from MySQL library
import mysql.connector
# Importing psycopg2 library to connect with Postgresql DB
import psycopg2
# Importing sqlalchemy to us maping classes with pandas
from sqlalchemy import create_engine as ce
# Importing pandas to read tables into dataframes
import pandas as pd
# Importing getpass module to Prompt the user for a password without echoing
import getpass as gp
# Importing MongoClient from pymongo library to make connction with MongoDB
from pymongo import MongoClient

print("Pull the data from Database Management System")
 
# Choosing the type of Database Management System
while True:
	dbms_type = int(input('''Please chose your DBMS:
		1. MySQL
		2. PostgrSQL
		3. MongoDB
		>>> '''))
	if dbms_type == 1 or dbms_type == 2 or dbms_type == 3:
		break

# Taking user inputs
while True:
	choice = int(input('''Choose depending on your credentials
		1. If you have host, user, password
		2. If you have all above and database specific name
		>>> '''))
	if choice == 1 or choice == 2:
		break

# Building a function to handle user logins	
def get_info():
	"""
	get_info function is built to take all the logins informations

	"""
	host = str(input("Input your Host(Defualt is localhost):\n>>> ") or 'localhost')
	user = str(input("Input your User:\n>>> ")) 
	password = str(gp.getpass(prompt="Input your Password:\n>>> "))
	if dbms_type == 1:
		port = int(input("Input your Port(Defualt is 3306):\n>>> ") or 3306)
	if dbms_type == 2:
		port = int(input("Input your Port(Defualt is 5432):\n>>> ") or 5432)
	if dbms_type == 3:
		port = int(input("Input your Port(Defualt is 27017):\n>>> ") or 27017)

	if choice == 1:
		return host, user, password, port
	elif choice == 2:
		database = str(input("Input your database name:\n>>> "))
		return host, user, password, port, database
   




def table_handler(*args):
	"""
	table_handler function is built to handle tables or collections in specific database 

	"""
	print("Do want to get all tables in database or one single table?")
	table_or_tables = int(input('''Choose depending on your credentials
		1. If you want a specific table
		2. If you want all tables in database
		>>> '''))

	# Part of code handling quring Specific table
	if table_or_tables == 1:

		if dbms_type == 1: 
			print("All Tables:")
			cur.execute("SHOW TABLES")
			for i,tb in enumerate(cur):
				print(i+1, ". " + str(tb[0]))
			table_name = str(input("Input the name of table you want:>>> "))
			df = pd.read_sql_query(f"SELECT * FROM {table_name}", mysql_engine)
			cnx.close()	

		if dbms_type == 2:
			print("All Tables:")
			cur.execute("SELECT * FROM pg_catalog.pg_tables;")
			for i,tb in enumerate(cur):
				print(i+1, ". " + str(tb[1]))
			table_name = str(input("Input the name of table you want:>>> "))
			df = pd.read_sql_query(f"SELECT * FROM {table_name}", postgresql_engine)
			cnx.close()

		if dbms_type == 3:
			print("All Collections:")
			collections_list = client[db_name].list_collection_names()
			# Printing all collections names
			for collection in collections_list:
				print(collection)
			collection_name = str(input("Input the name of collection you want:>>> "))
			table_name = collection_name
			collection_name = client[db_name][collection_name]
			df = pd.DataFrame(list(collection_name.find()))
		
		print(df.head())

		while True:
			file_type = int(input('''Choose file type:
			1. csv file
			2. xlsx file
			3. Json file
			>>> '''))

			if file_type == 1 or file_type == 2 or file_type == 3:
				break
				
		if file_type == 1:	
			file_name = table_name + ".csv"
			df.to_csv(file_name, index=False)
		elif file_type == 2:
			file_name = table_name + ".xlsx"
			df.to_excel(file_name, index=False)
		elif file_type == 3:
			file_name = table_name + ".json"
			df.to_json(file_name, orient='split', default_handler=str, index=False)
		print("Done.")

	# Part handling quering all tables in the database
	if table_or_tables == 2:

		while True:
			file_type = int(input('''Choose file type:
			1. csv file
			2. xlsx file
			3. Json file
			>>> '''))

			if file_type == 1 or file_type == 2 or file_type == 3:
				break

		if dbms_type == 1: 
			print("All Tables:")
			cur.execute("SHOW TABLES")
			for i,tb in enumerate(cur):
				print(i+1, ". " + str(tb[0]))
				table_name = str(tb[0])
				df = pd.read_sql_query(f"SELECT * FROM {table_name}", mysql_engine)
				if file_type == 1:	
					file_name = table_name + ".csv"
					df.to_csv(file_name, index=False)
				elif file_type == 2:
					file_name = table_name + ".xlsx"
					df.to_excel(file_name, index=False)
				elif file_type == 3:
					file_name = table_name + ".json"
					df.to_json(file_name, orient='split', default_handler=str, index=False)
			cnx.close()	

		if dbms_type == 2:
			print("All Tables:")
			cur.execute("SELECT * FROM pg_catalog.pg_tables;")
			for i,tb in enumerate(cur):
				print(i+1, ". " + str(tb[1]))
				table_name = str(tb[1])
				df = pd.read_sql_query(f"SELECT * FROM {table_name}", postgresql_engine)
				if file_type == 1:	
					file_name = table_name + ".csv"
					df.to_csv(file_name, index=False)
				elif file_type == 2:
					file_name = table_name + ".xlsx"
					df.to_excel(file_name, index=False)
				elif file_type == 3:
					file_name = table_name + ".json"
					df.to_json(file_name, orient='split', default_handler=str, index=False)
			cnx.close()	

		if dbms_type == 3:
			print("All Collections:")
			collections_list = client[db_name].list_collection_names()
			# Printing all collections names
			for collection in collections_list:
				print(collection)
				table_name = collection_name
				collection_name = client[db_name][collection_name]
				df = pd.DataFrame(list(collection_name.find()))
				if file_type == 1:	
					file_name = table_name + ".csv"
					df.to_csv(file_name, index=False)
				elif file_type == 2:
					file_name = table_name + ".xlsx"
					df.to_excel(file_name, index=False)
				elif file_type == 3:
					file_name = table_name + ".json"
					df.to_json(file_name, orient='split', default_handler=str, index=False)
	print("Done.")

# Part of code handling MySQL:
if dbms_type == 1:
	if choice == 1:
		host, user, password, port = get_info()
		try:
			cnx = mysql.connector.connect(user=user, password=password, host=host)
			cur = cnx.cursor()
			cur.execute("SHOW DATABASES;")
			print("All Databases:")
			for i,db in enumerate(cur):
				print(i+1, ". " + str(db[0]))
			db_name = str(input("Input the name of database you want:>>> "))
			cur.execute("USE " + db_name)
			print("You choosed is " + db_name + " Database")
			# I delayed this step, cuz i need to get database name to creat the engine
			mysql_engine = ce(f"mysql://{user}:{password}@{host}:{port}/{db_name}")
			table_handler(mysql_engine)
			cnx.close()
		except mysql.connector.Error as err:
			print("Failed to continue: {}".format(err))
			exit(1)

	elif choice == 2:
		host, user, password, port, database = get_info()
		mysql_engine = ce(f"mysql://{user}:{password}@{host}:{port}/{database}")
		try:
			cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
			cur = cnx.cursor()
			table_handler(mysql_engine)
			cnx.close()
		except mysql.connector.Error as err:
			print("Failed to continue: {}".format(err))
			exit(1)

# Part handling PosgreSQL:
if dbms_type == 2:
	if choice ==1:
		host, user, password, port = get_info()
		
		try:
			cnx = psycopg2.connect(host=host, user=user, password=password)
			cur = cnx.cursor()
			cur.execute("SELECT datname FROM pg_database;")
			print("All Databases: ")
			for i,db in enumerate(cur):
				print(i+1, ". " + str(db[0]))
			cnx.close()
			db_name = str(input("Input the name of database you want:>>> "))
			cnx = psycopg2.connect(user=user, password=password, host=host, database=db_name)
			cur = cnx.cursor()
			# I delayed this step, cuz i need to get database name to creat the engine
			postgresql_engine = ce(f"postgresql://{user}:{password}@{host}:{port}/{db_name}")
			table_handler(postgresql_engine)
		except psycopg2.Error as err:
			print("Failed to continue: {}".format(err))
			exit(1)
	if choice == 2:
		host, user, password, port, database = get_info()
		postgresql_engine = ce(f"postgresql://{user}:{password}@{host}:{port}/{database}")
		try:
			cnx = psycopg2.connect(user=user, password=password, host=host, database=database)
			cur = cnx.cursor()
			table_handler(postgresql_engine)
		except psycopg2.Error as err:
			print("Failed to continue: {}".format(err))


# Part handling MongoDB:
if dbms_type == 3:
	if choice == 1:
		host, user, password, port = get_info()
		# Creat client to make connction
		#client = MongoClient((f'mongodb://{user}:{password}@{host}:{port}/'))
		client = MongoClient((f'mongodb://{host}:{port}/'))
		# Getting all the names of databases in Mongodb
		dbs_list = client.list_databases()
		# Printing all databases names
		print("All Databases:")
		for db in dbs_list:
			print(db.get('name'))
		db_name = str(input("Input the name of database you want:>>> "))
		# Getting all the names of collections in choosen db
		collections_list = client[db_name].list_collection_names()
		# Printing all collections names
		table_handler()

		
	if choice == 2: 
		host, user, password, port, database = get_info()
		client = MongoClient((f'mongodb://{user}:{password}@{host}:{port}/{database}'))
		# I did change the variable name becuase in the rest of programme is called db_name 
		db_name = database
		# Getting all the names of collections in choosen db
		collections_list = client[db_name].list_collection_names()
		# Printing all collections names
		table_handler()