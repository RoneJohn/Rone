#!/usr/bin/env python
# coding: utf-8

# In[2]:


c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))


# In[26]:


#print prime no within range


s=int(input("enter start value"))
e=int(input("enter end value"))
for k in range(s,e):
    b=0
    for i in range(2,k):
        if k % i==0:
            b+=1
        else:
            print("\t")
    if b>=1:
        print(k,"not prime")
    else:
        print(k," prime")
        
        
        
        
        
        
        


# In[28]:


#fibnocci series
a=0
b=1
n=int(input("enter limit"))
for i in range(n):
    c=a+b
    a=b
    b=c
    print("The series is", c)


# In[59]:


# check  no is perfect or not

n = int(input("Enter any number: "))
sum = 0
for i in range(1, n):
    if(n % i == 0):
        sum = sum + i
if (sum == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")


# In[37]:


#Display perfect no within range

a = int(input("Enter start number: "))
b = int(input("Enter end number: "))
for j in range(a,b):
        s=0
        for i in range(1, j):
            if(j % i == 0):
                s=s+ i
            else:
                print(" ")
        if (s == j):
            print("The number is a Perfect number" ,j)
        else:
            print("The number is not a Perfect number",j)


# In[ ]:


A compiler or an interpreter is a program that converts program written in high-level language into machine code understood by the computer
.


# In[3]:


#strings try all buit-in functions;

ord("a")


# In[4]:


ord('#')


# In[5]:


chr(97)


# In[6]:


chr(55)


# In[7]:


str(49.2)


# In[8]:


str("f")


# In[9]:


s="anniversary"
print(len(s))


# In[10]:


a=s[1]
print(a)


# In[12]:


print(s.index("v"))


# In[13]:


print(s.index("ver"))


# In[14]:


print(s[-1])


# In[16]:


b=s[0:4]
print(b)


# In[21]:



s="anniversary"
s=s.replace("y","i")
print(s)


# In[22]:


print(s.upper())


# In[23]:


print(s.lower())


# In[24]:


print(s.title())


# In[25]:


print(s.rfind("anni"))


# In[26]:


print(s.rfind("gra"))


# In[27]:


print(s.startswith("anni"))


# In[28]:


print(s.endswith("sari"))


# In[30]:


print(s.isalnum())


# In[31]:


print(s.isalpha())


# In[32]:


print(s.isdigit())


# In[33]:


print(s.isspace())


# In[34]:


print(s.lstrip())


# In[35]:


print(s.lstrip())


# In[36]:


s="anni sary"
print(s.strip())


# In[11]:


a="program"
b="python_program"
print(b.split('_'))


# In[ ]:




