import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://chicagorealtor.com/realtor-search/'
f = csv.writer(open('Chicago-Realtors.csv', 'w', newline='', encoding="utf-8"))
f.writerow(['First Name', 'Last Name', 'Company Name', 'City', 'Zip', 'Email'])

for page in range(1, 1086):
    print(page)

    req = requests.get(URL + '?listpage=' + str(page))
    soup = BeautifulSoup(req.text, 'html.parser')

    table = soup.find("table")
    rows = table.find_all("tr")
    
    for row in rows:
        cells = row.find_all("td")
        
        first_name = cells[1:2]
        last_name = cells[2:3]
        company = cells[3:4]
        city = cells[4:5]
        zip_code = cells[5:6]

        for name in first_name:
            first_name = name.text.strip()
        for name in last_name:
            last_name = name.text.strip()
        for name in company:
            company = name.text.strip()
        for name in city:
            city = name.text.strip()
        for name in zip_code:
            zip_code = name.text.strip()
        email = row.find_all("a")[1]["href"][7:].strip()
        
        if email.startswith('[]') or email.startswith('/') or first_name == [] or last_name == [] or company == [] or city == [] or zip_code == []:
            continue 
        f.writerow([first_name, last_name, company, city, zip_code, email])
    