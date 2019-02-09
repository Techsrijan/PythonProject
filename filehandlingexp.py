fp=open("tech.txt","r")

print(fp.read())

fp2=open("techsrijan.txt","r")
#fp2.write("hi welcome")
#fp2.write("File ka content kaha gaya")
#fp2.write("ab last mein likhega kyoki mode ab aappend hi")
#print(fp2.readLine(),end="")
f=open("srijan","w")
for data in fp2:
    print(data)
    f.write(data)
    print("file copiesd successfully")

img=open("2.jpg","rb")
img2=open("new.jpg","wb")
for data in img:
    print(data)
    img2.write(data)
    print("Image copied suceesfully")
