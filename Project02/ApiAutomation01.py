import requests

response = requests.get('http://216.10.245.166/Library/GetBook.php',
             params={'AuthorName':'Rahul Shetty2'},)

print(response.text)
#
# outpt = response.json()
# print(type(outpt))
#
# assert response.status_code == 200
# print(response.headers)
# assert response.headers['Content-Type'] == "application/json;charset=UTF-8"

for book in response.json():
    if book['isbn'] == "bcz533effed":
        print(book)
        break

exBook = {'book_name': 'Learn Appium Automation with Java', 'isbn': 'bcz533effed', 'aisle': '20027'}

assert book == exBook