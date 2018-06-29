import pymysql

# Open database connection
db = pymysql.connect("localhost","root","","TESTDB" )
#db = pymysql.connect("localhost","","","TESTDB" )
# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('velentina', 'longjam', 30, 'f', 20000)"""
sel=("select * from EMPLOYEE")
cursor.execute(sel)
res1=cursor.fetchall()
print(res1)

'''try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()'''

# disconnect from server
db.close()