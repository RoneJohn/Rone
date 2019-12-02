#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello world")


# In[2]:


a=1
print(a)


# In[2]:


# Addition of two numbers

a= input("enter first no")
b=input("enter second no")
c= int(a)+int(b)
print("result is" ,c)


# In[13]:


# if- else
a=input("enter no")
b=input("enter second number")
a=int(a)
b=int(b)
if a>b:
    print(a)
elif b>a:
    print("b is greater")
else:
    print("equal")


# In[17]:


print(pow(3,2))


# In[18]:


print(round(5.6))


# In[21]:


# Strings

p=("giraffe academy")
print(p.upper())
print(p.upper().isupper())


# In[22]:


print(len(p))


# In[25]:


print (p.index("i"))


# In[26]:


print(p[0])


# In[29]:


print(p.replace("giraffe academy","Elephant Academy"))


# In[3]:


p=("giraffe academy")
print(p.index("gir"))


# In[6]:


name=input("enter your name")
age=input("enter your age")
print("hello  " +name+",""you are " +age)


# In[7]:


friends=("kevin","jim","tom")
print(friends[0])


# In[11]:


print(friends[-1])


# In[21]:


friends=["kevin","jim","tom"]
friends.insert(1, "kelly")
print(friends)


# In[18]:


list2 = ['a', 'b', 'c', 'd', 'e']  
  
# insert z at the front of the list 
list2.insert(0, 'z') 
print(list2) 


# In[25]:


friends=["kevin","jim","tom"]
friends.remove("jim")
print(friends)


# In[1]:


#loops

i=1
while i<=10:
    print (i)
    i+=1
print("done")


# In[4]:


a=int(input("enter number"))
if a%2==0:
    print("even")
else:
    print("odd")
    


# In[8]:


for i in range(1,10):
    print (i)


# In[20]:


#factorial

n=int(input("enter no "))
f=1
for i in range(1,n+1):
    f=f*i
print (f)
        


# In[11]:



# to find factors using functions
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
num = int(input("enter no"))
print_factors(num)


# In[2]:


#program to check no is palindrome or not

n=int(input("Enter number:"))
t=n
rev=0
while(n>0):
    p=n%10
    rev=rev*10+p
    n=n//10
if(t==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")


# In[11]:


#program to check string is palindrome or not

n=input("enter string")
s=n
rev=reversed(s)
if list(n)==list(rev):
    print("palindrome")
else:
    print("not palindrome")


# In[15]:


# Program to sort alphabetically the words form a string provided by the user
n=input("enter string")
w=n.split()
w.sort()
print("The sorted words are:")
for i in w:
   print(i)


# In[ ]:


n=int(input("Enter number:"))
t=n
sum=0
while(n>0):
    p=n%10
    sum=
    n=n//10
if(t==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

