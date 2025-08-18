from bs4 import BeautifulSoup
html_doc = "https://www.python.org/"
soup = BeautifulSoup(html_doc,"lxml")
print("Hello python")
print(soup.h1.text)