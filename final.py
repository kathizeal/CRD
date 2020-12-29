#here are the commands to demonstrate how to access and perform operations on a main file


#run the MODULE of MAIN FILE and import mainfile as a library 
import threading
from threading import*
import CRD
import time
#importing the main file("code" is the name of the file I have used) as a library 



key,value,urtime=CRD.create("SASTRA",25,5000)
#to create a key with key_name,value given and with no time-to-live property


key,value,urtime=CRD.create("SRC",70,3600) 
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)


CRD.read("SASTRA")
#it returns the value of the respective key in Jasonobject format 'key_name:value'


CRD.read("SRC")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


CRD.create("SASTRA",50)
#it returns an ERROR since the key_name already exists in the database
#To overcome this error 
#either use modify operation to change the value of a key
#or use delete operation and recreate it


CRD.modify("SASTRA",55)
#it replaces the initial value of the respective key with new value 

 
CRD.delete("SASTRA")
#it deletes the respective key and its value from the database(memory is also freed)

#we can access these using multiple threads like
t1=Thread(target=(CRD.create or CRD.read or CRD.delete),args=(key,value,urtime)) #as per the operation
t1.start()
time.sleep(5)
t2=Thread(target=(CRD.create or CRD.read or CRD.delete),args=(key,value,urtime)) #as per the operation
t2.start()

#and so on upto tn

#the code also returns other errors like 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB