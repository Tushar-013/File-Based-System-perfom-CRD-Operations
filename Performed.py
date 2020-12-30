# the commands to showing how to access and performed the operation on the main file
import time
import threading
from threading import*

# run the main file and import the main file
#importing the main file as a library
import main as a

# create a key with KeyName and value and without the time-to-live property
a.create("John",99)
a.create("Sam",98)


# create a key with KeyName and value and with time-to-live property( Value in seconds e.g, value = 60 sec means 1 minute)
a.create("Ryan",95,1000)


#to read the value of the respective key in JSON object format "KeyName:value"
a.read("John")
a.read("Sam")


#to read the value of the respective key in JSON object format if the Time-to-live is not expired else it giving an Error
a.read("Ryan")


a.create("John",80)
# it giving an error because the KeyName is already exists in the database
# if you want to change the value of the particular key then use the update operation
# or delete the key and create new key with same name and with correct value


a.update("John",80)
# it update the initial value of the respective key with new value


# to deletes the respective key and there value from the database
a.delete("Sam")


#to access these using multiple threads like
#as per the operation
t1=Thread(target=(create or read or delete),args=(KeyName,value,timeout)) 
t1.start()
t1.join()

#as per the operation
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t2.start()
t2.join()


#the program is also giving some other errors like
#"Invalid KeyName!!!" if length of key is greater than 32 or KeyName contains any numbers or special characters etc.,
#"key does not exist" if KeyName is not exist in database
#"Memory limit exceeded!!!" if file memory exceeds 1GB




