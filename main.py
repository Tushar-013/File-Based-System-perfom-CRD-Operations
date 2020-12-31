
# for python 3.0 we use import threading and for older version(python 2.0) we use import thread
import threading
from threading import*
import time
import json

dict={} # "dict" is a dictionary in which data is store

# for create operation
# create function "create(key,value,time_to_live)" time_to_live is optional you can also continue by passing only two arguments without giving the value of time_to_live
def create(key,value,time_to_live=0):

    if key in dict:
        # printing error message1 "key is already exist"
        print("Error: The",key,"key is already exist")

    else:
        if key.isalpha():

            # condition for size of file is less than 1GB and JSON object value is also less than 16KB
            if (len(dict)<(1024**3)) and (value<=16*1024*1024):

                if time_to_live==0:
                    s=[value,time_to_live]

                else:
                    s=[value,time.time()+time_to_live]

                # condition for input key name capped at 32chars
                if len(key)<=32:
                    dict[key]=s

            else:
                # printing error message2 "Memory limit exceeded"
                print("Error: Memory limit exceeded!!!")

        else:
            # printing error message3 "Invalid KeyName"
            print("Error: Invalid KeyName!!! KeyName only contain alphabets and no special characters or numbers")


# for read operation
# create function "read(KeyName)"
def read(key):

    if key not in dict:
        # printing error message4 " key does not exist in database"
        print("Error: The",key,"key does not exist in database. Please enter a valid Key")

    else:
        l=dict[key]
        if l[1]!=0:

            # compares expire time with present time
            if l[1]>time.time():
                res=str(key)+":"+str(l[0])
                # to return the value in the JSON object format i.e., "KeyName:value"
                res=json.dumps(res)
                #printing the result in JSON object format
                print(res)

            else:
                # printing error message5 " time_to_live of key is expire"
                print("Error: time-to-live of",key,"has been expired")

        else:
            res = str(key)+":"+str(l[0])
            # to return the value in the JSON object format i.e., "KeyName:value"
            res = json.dumps(res)
            #printing the result in JSON object format
            print(res)



#for delete operation
# create function "delete(KeyName)"
def delete(key):

    if key not in dict:
        # printing error message6 " key does not exist in database"
        print("Error: The",key,"key does not exist in database. Please enter a valid Key")

    else:
        l=dict[key]
        if l[1]!=0:
            # compares expire time with present time
            if l[1]>time.time():
                dict.pop(key)
                print(key,"key is successfully deleted")

            else:
                # printing error message7 "time_to_live of key is expire"
                print("Error: time-to-live of",key,"has been expired")

        else:
            dict.pop(key)
            print(key,"key is successfully deleted")



#I also add additional operation to update or modify in order to change the value of key before its expiry time if provided

#for update operation
# create function "modify(KeyName,NewValue)"
def update(key,value):
    if key not in dict:
        # printing error message8 " key does not exist in database"
        print("Error: The", key, "key does not exist in database. Please enter a valid Key")

    l=dict[key]
    if l[1]!=0:
        # compares expire time with present time
        if l[1]>time.time():
            s=[]
            s.append(value)
            s.append(l[1])
            dict[key] = s
            print(key, "key is successfully updated")

        else:
            # printing error message9 "time_to_live of key is expire"
            print("Error: time-to-live of", key, "has been expired")

    else:
        s = []
        s.append(value)
        s.append(l[1])
        dict[key] = s
        print(key, "key is successfully updated")















