import time
str = "welcome in Python"
time.sleep(2)
print(str)
#to create sentence case
print(str.capitalize())
print(str.count('o'))
print(str.count('Python'))
print(str.count('on'))
print(str.endswith('thon'))
str1="techSrijan Consultancy Services"
print(str1.find('srijan'))
print(str1.find('services'))
print(str1.find('s'))
print(len(str1))
print(str1.split('s'))
print(str1.title())
print(str1.lower())
print(str1.upper())
print(str1.islower())
str2 = "hello"
print(str2.islower())
print(str1.isupper())
print(str1.swapcase())
str3 =" Her name is sonia and sonia is good girl"
print(str3)
print(str3.replace('sonia','tamanna'))
print(str3.replace('i','Z'))
str4 = "9956477677a"
print(str4.isdigit())
str5 = "9956477677"
print(str5.isdigit())
print(str3.isalpha())
print(str2.isalpha())
str6 = "    !!!!HeLLO!!!"
print(str6)
print(str6.strip())
str7 = "!!!!HeLLO!!!"
print(str7.strip('!'))
print(str7.lstrip('!'))
print(str7.rstrip('!'))

