#!/usr/bin/env python
# coding: utf-8

# In[5]:


punc_marks = ['.',',','"','{','}',';',':','-','?','!','$',"'",'*','%','&','^','#','@','(',')','_','+','=']
input_text = "Hello, *^$ World! Let's remove punctuation: shall we?"
output=""
for char in input_text:
    if char not in punc_marks:
        output+=char
print(output)


# In[13]:


def remove_punc(str):
    punc_marks = ['.',',','"','{','}',';',':','-','?','!','$',"'",'*','%','&','^','#','@','(',')','_','+','=']
    input_text = "Hello, *^$ World! Let's remove punctuation: shall we?"
    output=""
    for char in input_text:
        if char not in punc_marks:
            output+=char
    return output
output = remove_punc(input_text)
print(output)


# In[21]:


def remove_stop(input_text):
    stop_marks = ['is', 'the', 'a', 'of', 'this', 'an', 'about', 'any', 'and', 'again']
    words = input_text.split()
    output = [word for word in words if word.lower() not in stop_marks]
    return ' '.join(output)
input_text = "Hello, This is a state of flowers"
output = remove_stop(input_text)
print(output)


# In[31]:


def remove_stop(input_text):
    stop_marks = ['is', 'the', 'a', 'of', 'this', 'an', 'about', 'any', 'and', 'again']
    words = input_text.split()
    filtered_words = []
    for word in words:
        if word.lower() not in stop_words:
            filetered_words.append(word)
    input_text = "Hello, This is a state of flowers"
    output = ' '.join(filtered_words)
    print(output)


# In[35]:


def remove_stop(input_text):
    stop_marks = ['is', 'the', 'a', 'of', 'this', 'an', 'about', 'any', 'and', 'again']
    words = input_text.split()
    filtered_words = []
    for word in words:
        if word.lower() not in stop_marks:
            filtered_words.append(word)
    output = ' '.join(filtered_words)
    print(output)
input_text = "Hello, This is a state of flowers"
remove_stop(input_text)


# In[ ]:




