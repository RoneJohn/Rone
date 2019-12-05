#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = 1

type(a)


# In[3]:


c = "hello"

type(c)


# In[ ]:


# ## break, continue and pass
for i in range(0,10):
   # print(i)
    if i == 3:
        break
    print(i)


# In[9]:


for i in range(0,10):
   # print(i)
    if i == 2:
        continue
    print(i)


# In[ ]:


for i in range(0,5):
    print("before", i)
    if i == 3:
        pass


# In[13]:


#Reverse strings using queue.**<br>

from queue import Queue  
  
# Utility function to print the queue  
def Print(queue): 
    while (not queue.empty()): 
        print(queue.queue[0], end = ", ")  
        queue.get() 
  
# Function to reverse the queue  
def reversequeue(queue): 
    Stack = []  
    while (not queue.empty()):  
        Stack.append(queue.queue[0])  
        queue.get() 
    while (len(Stack) != 0):  
        queue.put(Stack[-1])  
        Stack.pop() 
  
# Driver code  
if __name__ == '__main__': 
    queue = Queue() 
    queue.put("h")  
    queue.put("e")  
    queue.put("l")  
    queue.put("l")  
    queue.put("o")
    
    reversequeue(queue)  
    Print(queue) 


# In[22]:


# compare two lists using set theory.<br>

# initializing lists  
list1 = set([1, 2, 4, 3, 5]) 
list2 = set([1, 2, 4, 3, 5,6]) 
  
print ("The first list is : " + str(list1)) 
print ("The second list is : " + str(list2)) 
  
# sorting both the lists 
#x=list1.sort() 
#y=list2.sort() 
  
if list1 ==list2: 
    print ("The lists are identical") 
else : 
   print ("The lists are not identical") 


# In[34]:


#Find the duplicates elements in the lists

list1 = [1,2,1,3,1,4,1,4,7,5,9]
u = []
count=0
for ele in list1:
    if ele not in u:
        u.append(ele)
    else:
        count=count+1
        print(ele)
print("final list is",u)

print("there are" ,count, "duplicate elements")


# In[46]:


#Print all missing elements in the lists<br>

A=list()
B=list()
n1=int(input("Enter the size of the First List ::"))
n2=int(input("Enter the size of the second List ::"))
print("Enter the Element of first List ::")
for i in range(int(n1)):
   k=int(input(""))
   A.append(k)
print("Enter the Element of second List ::")
for j in range(int(n2)):
   k1=int(input(""))
   B.append(k1)
x= list(set(B).difference(A))   
y=list(set(A).difference(B))
    
#x=print("Missing values in first list:",(set(B).difference(A)))
#y=print("Missing values in second list:",(set(A).difference(B)))

print("Missing values in first list:"+str(x))
print("Missing values in second list:"+str(y))


# In[47]:


test_list = [3, 5, 6, 8, 10] 
  
print("The original list : " + str(test_list)) 
  

res = list(set(range(max(test_list) + 1)) - set(test_list)) 
  
print("The list of missing elements : " + str(res))


# In[11]:


#You need to check the start or end of a string for specific text patterns, such as filename extensions, URL schemes, and so on.

str = 'http://www.python.org'

if str.startswith("http://")and str.endswith("org"):

        print("true")
else:
        print("false")


# In[4]:


#You want to search for and replace a text pattern in a string.

str="hello welcome to bangalore"
r=str.find("bangalore")
print ("Substring 'bangalore' found at index:", r ) 
print(str.replace("bangalore","chennai"))


# In[18]:


#You want to match or search text for a specific pattern.

text = 'yeah, but no, but yeah, but no, but yeah'
s=text.find("yeah")
print ("Substring 'yeah' found at index:", s) 
#print(count(s, beg= 0, end=len(s)))
counts=dict()
words = text.split()

for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

print(counts)
    

print(text.replace('yeah', "yes", 1))


# In[81]:


#You need to search for and possibly replace text in a case-insensitive manner.

text = 'UPPER PYTHON, lower python, Mixed Python'
s=text.find("python")
print ("Substring found at index:", s) 
res= ""
#c=text.split()

#print(c)
for i in text:
            if(i.isupper()):
                print(i.lower())
            else:
                print(i.upper())








# In[96]:


def convertOpposite(str): 
    ln = len(str) 
  
    # Conversion according to ASCII values 
    for i in range(ln): 
        if str[i] >= 'a' and str[i] <= 'z': 
  
            # Convert lowercase to uppercase 
            str[i] = chr(ord(str[i]) - 32) 
  
        elif str[i] >= 'A' and str[i] <= 'Z': 
  
            # Convert lowercase to uppercase 
            str[i] = chr(ord(str[i]) + 32) 
  
# Driver code 
if __name__ == "__main__": 
    str = "'UPPER PYTHON, lower python, Mixed Python'"
    str = list(str) 
  
    # Calling the Function 
    convertOpposite(str) 
  
    str = ''.join(str) 
    print(str) 


# In[99]:


#You want to strip unwanted characters, such as whitespace, from the beginning, end, or middle of a text string.

a=" hello  world "
print(a.lstrip())
print(a.replace(" ",""))


# In[110]:


#You need to format text with some sort of alignment applied

a= "hello"
print (a.center(40, '#')) 
print (a.ljust(40, '-'))
print (a.rjust(50, '-'))
print (a.center(40, " "))


# In[136]:


#You want to combine many small strings together into a larger string.

a = {"name": "John", "country": "Norway"}
res = "TEST"

x = res.join(a)

print(x)


# In[ ]:




