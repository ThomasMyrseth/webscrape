from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
page = requests.get(url)
soup = BeautifulSoup(page.text, features="html.parser")

table = soup.find_all("table")[1]

headers = table.find_all("th")
headers_list = []
for line in headers:
    #headers_list.append(line.text) #alternativ metode
    #headers_list.append(header)
    a = line.text[:-1]
    headers_list.append(a)

rows = table.find_all("tr")
matrice = []  # 2d liste
for row in rows:
    row_data = row.find_all("td")  # dette er en liste
    row_populated = []
    for data in row_data:
        text = data.text[:-1]
        row_populated.append(text)
    matrice.append(row_populated)


def saveToText():
    f = open("top100companies.txt", "a") #append mode
    for row in matrice:
        text = ""
        for data in row:
            text += data + "\t"
        f.write(text + "\n")
    f.close()


def deleteFile():
    f = open("top100companies.txt", "w")
    f.write("")
    f.close()


deleteFile()
saveToText()
