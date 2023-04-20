-- Mysql configuration
import mysql.connector
connection = mysql.connector.connect(
		HBNB_ENV = "dev",
		HBNB_MYSQL_USER = "hbnb_dev",
		HBNB_MYSQL_PWD = "hbnb_dev_pwd",
		HBNB_MYSQL_HOST = "localhost",
		HBNB_MYSQL_DB = "hbnb_dev_db",
		HBNB_TYPE_STORAGE = "DBStorage")
cursor = connection.cursor(prepared = true)