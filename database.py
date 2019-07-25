#!/usr/bin/python3
#
# Title: Database
# Description: This script connect with database
# Author: @kirtanpatel28
#
import pymysql

class Database:



	# Connect to database
	def __init__(self, host, dbUser, dbName):


		print("""====================
 Connect to databse
====================
Host: {0}
User: {1}\n""".format(host,dbUser))


		# Try initialize connection with database
		try:
			# Apply parameters
			self.host = host
			self.dbUser = dbUser
			self.dbName = dbName
			

			# Get password from user for security ¯\_(ツ)_/¯
			dbPassword = input('Password: ')


			# Connect to database
			try:
				self.db = pymysql.connect(host, dbUser, dbPassword, dbName)
				print("\nSuccessful connect to " + dbName + " database on " + host + "\n")


				# Create table if not exisit
				query = """CREATE TABLE IF NOT EXISTS `pydb`.`top100lc` ( `id` INT NOT NULL AUTO_INCREMENT , `title` TEXT NOT NULL , `author` TEXT NOT NULL , 
														`rank` TEXT NOT NULL , `readers` TEXT NOT NULL , `opinions` TEXT NOT NULL , 
														`rate` TEXT NOT NULL , `adddate` CHAR(34) NOT NULL , 
														PRIMARY KEY (`id`)) ENGINE = InnoDB CHARSET=utf8 COLLATE utf8_polish_ci;"""

				self.query(query)

			except:
				print("\n\nOPS! Can't connect to database\n\n")
		except:
			print("\n\nOPS! Please check your input data\n\n")



	# Send query to database
	def query(self, query):
		try:
			self.db.cursor().execute(query)
			self.db.commit()
		except:
			self.query = query
			print("Error with query: {0}\nRollingback!\n".format(query))
			self.db.rollback();




	# Close connect with database
	def close(self):
		self.db.close()
		print("\nConnection between you and " + self.dbName + " database was closed")
