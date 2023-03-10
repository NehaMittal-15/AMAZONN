from bs4 import BeautifulSoup
import requests
import csv

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3029.110 Safari/537.3'}

source = requests.get('https://www.amazon.in/s?k=Laptops&ref=nb_sb_noss_2', headers = headers).text
soup = BeautifulSoup(source, 'lxml')

print(soup)
# print(soup.prettify())

Names = []
Prices = []
Ratings = []
ListofProd = []
Products = {}

# for loop

for i in soup.find_all('a', class_='a-link-normal a-text-normal'):
    string = i.attrs['href']
    Names.append('https://www.amazon.in'+ string)

#
# for i in soup.find_all('span', class_='a-price-whole'):
#     Prices.append(i.text)
#
# for i in soup.find_all('span', class_='a-icon-alt'):
#     Ratings.append(i.text)

for i in Names:
    source2 = requests.get(i, headers=headers).text
    soup2 = BeautifulSoup(source2, 'lxml')
    print(i)
    Title = soup2.find('span', id='productTitle').text
    Title = Title.strip()

    try:
        Price = soup2.find('td', class_='a-span12').text
        Price = Price.strip()
        Price.replace("â‚¹Â","Rs")
    except:
        Price = "Not Given"

    try:
        Rating = soup2.find('span', class_='a-icon-alt').text
        Rating.strip()
    except:
        Rating = "Not Given"
    ListofProd.append(
        {
            "Title": Title,
            "Price": Price,
            "Rating": Rating,
            "Link": i
        }
    )
    # print(ListofProd)

for i in ListofProd:
    print(i)

#
file_name = 'Laptops.csv'

with open(file_name, 'w', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['Sr.No', 'Laptop Name', 'Prices', 'Rating', 'Product Link'])

    for i in range(len(ListofProd)):
        print(ListofProd[i]["Title"])
        writer.writerow([i, ListofProd[i]["Title"], ListofProd[i]["Price"], ListofProd[i]["Rating"], ListofProd[i]["Link"]])