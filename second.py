
from bs4 import BeautifulSoup
import requests
URL= "https://www.geeksforgeeks.org/java/java/"
r = requests.get(URL)


soup = BeautifulSoup(r.content,'html.parser')

# All html content
# print(soup.prettify())    


# all links 
# for link in soup.find_all('a'):
#     print(link.get('href'))                   


# with open("index.html") as fp:
#     soup = BeautifulSoup(fp,'html.parser')

# print(soup)


# Tags contain lot of attributes and methods and two important features of a tag are its name and attributes.
tag = soup.html
print(type(tag))



# Name (tag.name)
# Every tag contains a name and can be accessed through '.name' as suffix. tag.name will return the type of tag it is.
print(tag.name)



# Attributes (tag.attrs)
# A tag object can have any number of attributes. In the above example, the tag <b class="boldest"> has an attribute 'class' whose value is "boldest". Anything that is NOT tag, is basically an attribute and must contain a value. A dictionary of attributes and their values is returned by "attrs". You can access the attributes either through accessing the keys too.

# In the example below, the string argument for Beautifulsoup() constructor contains HTML input tag. The attributes of input tag are returned by "attr".
tag = soup.input
print(tag.attrs)

# Output : {'class': ['gcse-search-input__wrapper'], 'id': 'gcse-search-input', 'aria-expanded': 'true', 'placeholder': 'Search...', 'autocomplete': 'off'}


# We can do all kind of modifications to our tag's attributes (add/remove/modify), using dictionary operators or methods.
# In the following example, the value tag is updated. The updated HTML string shows changes.
tag['autocomplete'] = 'on'
print(tag.attrs)
