import pymysql
con=pymysql.connect(host="localhost",user="root",db="pythongui")
mycursor=con.cursor()
print("Connection established")
#mycursor.execute("""create table detail(id int primary key, name varchar(20))""")
print("table created")
#mycursor.execute("insert into detail(id,name) values(1,'ABC');")
#print("data inserted successfully")
#mycursor.execute("update detail set name='ashwani' where id=1;")
#print("data updated successfully")
#mycursor.execute("delete from detail where id=1;")
#print("data deleted successfully")

#to save data in table
con.commit()
# to close the connection
con.close()
