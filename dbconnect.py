import pymysql
conn=pymysql.connect(host="localhost",user="root",db="bit")
mycursor=conn.cursor()
'''mycursor.execute(""" create table detail
                     (id int primary key,
                     name varchar(20)
                     )""")'''
mycursor.execute(" insert into detail(id,name)values(5,'Ram');")
print("Data inserted successfully")
#mycursor.execute(" update detail set name='Shyam' where id=2;")
#print("Data updated successfully")
#mycursor.execute(" delete from detail where id=2;")
print("Data deleted successfully")

conn.commit()
conn.close()



