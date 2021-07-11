import sqlite3
#create a connection to a db and cursor
con = sqlite3.connect("Company.db")
c = con.cursor()

#create a table
c.execute("""CREATE TABLE Employees(
First_Name text,
Last_Name text,
Email text,
Branch text,
Role text,
Salary real)""")

#Insert the mutiple records in Employees table
many_records = [('Sam','Akkie','sam1@email.com','UK','Senior Developer',80000.0),
                             ('Johan','Smith','smith20@johan.com','US','Senior Tester',75000.0),
                             ('Thomas','Edesin','edesin@gmail.com','US','Director',150000.0),
                             ('Graham','Bell','bell@email.com','Swiss','HR',55000.0),
                             ('Kajol','Shetty','kajol404@gmail.com','India','Programe Analyst',30000.0)]
c.executemany("INSERT INTO Employees VALUES(?,?,?,?,?,?)",many_records)

#Update the records values.
c.execute("""UPDATE Employees SET
First_Name = 'John'
WHERE rowid = 2""")

#Retrive/select the records from the table.
#rowid is primary key generate automatically for each record in the table
c.execute("SELECT rowid, * FROM Employees")

#using WHERE ,AND Clauses LIKE
c.execute("SELECT rowid, * FROM Employees WHERE Salary <=80000.0 AND Email LIKE '%email.com' ")

#Retriving the records using ORDER BY,LIMIT Clause
c.execute("SELECT rowid, * FROM Employees ORDER BY Salary DESC LIMIT 3")

#fetching the records in format using loop
records = c.fetchall()
for i in records:
    print(i)

#Commiting the transactions or updates
con.commit()
#Closing the database
con.close()