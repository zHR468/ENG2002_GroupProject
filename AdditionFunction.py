#!/usr/bin/env python
# coding: utf-8

# In[85]:


# placeholder, say x and y are the userinputs
x = 12.4321
y = 13.654321
# x and y gets split into integers a--->(x1.x2) can be changed
x1 = 12
x2 = 4321
y1 = 13 
y2 = 654321
def Add(x1, x2, y1, y2):
    c1 = x1 + y1
    print(c1)
    # calculating decimal numbers
    print("Length of x2 is",len(str(x2)))
    print("Length of y2 is",len(str(y2)))
    print("x2-y2 is",len(str(x2))-len(str(y2)))
    # Match the decimal parts for calculating
    if len(str(x2)) < len(str(y2)):
        x2 *= 10**(len(str(y2))-len(str(x2)))
    elif len(str(x2)) > len(str(y2)):
        y2 *= 10**(len(str(x2))-len(str(y2)))
    print("Matched decimal place of x2, y2:",x2,y2)
    ODL = len(str(x2)) # Original Decimal Length, saved for later
    print(ODL)
    c2 = x2 + y2
    PreOutputc2 = str(c2) # turn c2 into a string for slicing
    if len(str(c2)) > ODL: #Carry-over logic, e.g. 0.6 + 0.6 = 1.2 and NOT 0.12
        Fixedc2 = PreOutputc2[1:]
        Fixedc1 = str(c1 + 1)
    else:
        Fixedc2 = PreOutputc2
        Fixedc1 = str(c1)
    return(Fixedc1, Fixedc2)

# Final output of this additive function, *They should be strings)
print(Add(x1, x2, y1, y2))


# In[ ]:





# In[ ]:




