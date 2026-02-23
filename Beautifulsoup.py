from bs4 import BeautifulSoup
import requests

url = "http://books.toscrape.com/"
headers = {
    #user agent is making the request and from where
    "User-Agent" : "Chrome/120.0.0.0"
}
response = requests.get(url,headers = headers)
print(response.status_code)
#parse the html
soup = BeautifulSoup(response.text,features="html.parser")
print(soup) #html gets printed

#get the title of the page
print(soup.title.string)
#head
headtag = soup.head()
print(headtag)
#body
bodytag = soup.body()
print(bodytag)

#get the first matching tag
print(soup.find("h1"))

# get the matching paragraph
print(soup.find("p"))
#get the link in the page
links = soup.find_all("a")
for link in links:
    print(link.get("href"))

#extract the books
books = soup.find_all("article",class_="product_pod")

#extract all the titles and prices of books
for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.find("p",class_="price_color").text
    print("Title:",title)
    print("Price:",price)

#extracting the data
html_doc = """
<html>
<head>
  <title>List Example</title>
</head>
<body>
  <ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
  </ul>
</body>
</html>
"""
soup = BeautifulSoup(html_doc,features  ="html.parser")
items = soup.find_all("li")
for item in items:
    print(item.text)

#extracting the data from paragraph
html_doc = """
<html>
<head><title>CSS Selector Example</title></head>
<body>
  <div id="main">
    <p class="info">Info Paragraph 1</p>
    <p class="info">Info Paragraph 2</p>
  </div>
</body>
</html>
"""
soup = BeautifulSoup(html_doc,features  ="html.parser")
items = soup.find_all("p")
for item in items:
    print(item.text)




