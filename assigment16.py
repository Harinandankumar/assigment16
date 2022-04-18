#!/usr/bin/env python
# coding: utf-8

# 1. Create a list called years_list, starting with the year of your birth, and each year thereafter until the year of your fifth birthday. For example, if you were born in 1980. the list would be years_list = [1980, 1981, 1982, 1983, 1984, 1985].
# 
# 
# 
# Ans:-

# In[1]:


years_list = [ele for ele in range(1997,1997+6)]
print(years_list)


# 2. In which year in years_list was your third birthday? Remember, you were 0 years of age for your first year.
# 
# 
# 
# Ans:-

# In[2]:


print(years_list[3])


# 3. In the years list, which year were you the oldest?
# 
# 
# 
# Ans:-

# In[3]:


print(years_list[-1])


# 4. Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".
# 
# 
# 
# 
# Ans:-

# In[4]:


things = [ele+'ella' for ele in ['mozzar','cinder','salmon']]
print(things)


# 5. Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?
# 
# 
# 
# Ans:-

# In[5]:


for ele in range(len(things)):
    if things[ele] == 'cinderella':
        things[ele] = things[ele].capitalize()
print(things)


# 6. Make a surprise list with the elements "Groucho," "Chico," and "Harpo."
# 
# 
# 
# Ans:-

# In[6]:


suprise_list = ['Groucho','Chico','Harpo']
print(suprise_list)


# 7. Lowercase the last element of the surprise list, reverse it, and then capitalize it.
# 
# 
# 
# Ans:-

# In[7]:


print(suprise_list[-1].lower()[::-1].capitalize())


# 8. Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is chien, cat is chat, and walrus is morse.
# 
# 
# 
# Ans:-

# In[8]:


e2f = {'dog':'chien','cat':'chat','walrus':'morse'}
print(e2f)


# 9. Write the French word for walrus in your three-word dictionary e2f.
# 
# 
# Ans:-

# In[9]:


print(e2f.get('walrus'))


# 10. Make a French-to-English dictionary called f2e from e2f. Use the items method.
# 
# 
# 
# Ans:-

# In[10]:


f2e = dict([ele[::-1] for ele in e2f.items()])
print(f2e)


# 11. Print the English version of the French word chien using f2e.
# 
# 
# Ans:-

# In[11]:


print(f2e.get('chien'))


# 12. Make and print a set of English words from the keys in e2f.
# 
# 
# 
# Ans:-

# In[12]:


print(list(e2f.keys()))


# 13. Make a multilevel dictionary called life. Use these strings for the topmost keys: 'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys refer to empty dictionaries.
# 
# 
# 
# Ans:-

# In[13]:


life = {
    'animals':{
        'cats':['Henri','Grumpy','Lucy'],
        'octopi':{},
        'emus':{}
    },
    'plants':{},
    'other':{}
}
print(life)


# 14. Print the top-level keys of life.
# 
# 
# 
# Ans:-

# In[14]:


print(list(life.keys()))


# 15. Print the keys for life['animals'].
# 
# 
# 
# Ans:-

# In[15]:


print(list(life['animals'].keys()))


# 16. Print the values for life['animals']['cats']
# 
# 
# 
# Ans:-

# In[16]:


print(life['animals']['cats'])

