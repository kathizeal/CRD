import threading 
from threading import*
import time

dic={}
def create(key,value,urtime=0):
    if key in dic:
        print("key is used already")
    else:
        if(key.isalpha()):
            if(len(dic)<(1024*1024*1024) and value<=(16*1024*1024) and len(key)<=32):
                if(time==0):
                    lis=[value,urtime]
                    dic[key]=lis
                    return key,value,urtime
                    
                else:
                    lis=[value,time.time()+urtime]
                    dic[key]=lis
                    return key,value,urtime
            else:
                print("error: Memory limit exceeded!!!")
        else:
            print("error: Invalid keyName!! and keyName must contain only alphabets and no special characters or numbers and less than 32 char")


def read(key):
    if key not in dic:
        print("error: given key does not exist in database. Please enter a valid key")
    else:
        val=dic[key]
        if val[1]!=0:
            if time.time()<val[1]:
                string=str(key)+":"+str(val[0])
                print(string)
                return string
            else:
                print("error: time-to-live of",key,"has expired")
        else:
            string=str(key)+":"+str(val[0])
            print(string)
            return string
def delete(key):
    if key not in dic:
        print("error: given key does not exist in database. Please enter a valid key")
    else:
        val=dic[key]
        if val[1]!=0:
            if time.time()<val[1]:
                del dic[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired")
        else:
            del dic[key]
            print("key is successfully deleted")
def modify(key,value):
    val=dic[key]
    if val[1]!=0:
        if time.time()<val[1]:
            if key not in dic:
                print("error: given key does not exist in database. Please enter a valid key") 
            else:
                l=[]
                l.append(value)
                l.append(val[1])
                dic[key]=l
        else:
            print("error: time-to-live of",key,"has expired") 
    else:
        if key not in dic:
            print("error: given key does not exist in database. Please enter a valid key")
        else:
            l=[]
            l.append(value)
            l.append(val[1])
            dic[key]=l






