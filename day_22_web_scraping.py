# ================================ What is Web Scrapping ==============================

# The internet is full of huge amount of data which can be used for different purposes. To collect this data we need to know how to scrape data from a website.
# Web scraping is the process of extracting and collecting data from websites and storing it on a local machine or in a database.
# In this section, we will use beautifulsoup and requests package to scrape data. The package version we are using is beautifulsoup 4.

# To start scraping websites you need requests, beautifoulSoup4 and a website.

# pip install requests
# pip install beautifulsoup4

# To scrape data from websites, basic understanding of HTML tags and CSS selectors is needed. 
# We target content from a website using HTML tags, classes or/and ids. Let us import the requests 
# and BeautifulSoup module

import requests
from bs4 import BeautifulSoup

# Let us declare url variable for the website which we are going to scrape.

url = 'https://archive.ics.uci.edu/ml/datasets.php'

headers = {
    "User-Agent": "Mozilla/5.0"
}


# Lets use the requests get method to fetch the data from url

response = requests.get(url, headers=headers)

# lets check the status
status = response.status_code
print(status) # 200 means fetching data successfully

# Using beautifulSoup to parse content from the page

content = response.content # we get all the content from the website using resposnse.content
soup = BeautifulSoup(content, 'html.parser') # beautifulsoup will give
print(soup.title) # <title>UCI Machine Learning Repository</title>
print(soup.title.get_text()) # UCI Machine Learning Repository
# print(soup.body) # give whole the page on website
print(response.status_code) # 200

tables = soup.find_all('table', {'cellpadding':'3'})
print(len(tables))
# table = tables[0]
# for td in table.find('tr').find_all('td'):
#     print(td.text)


# ================================ Questions ===================

# 1. Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').

# Required libraries import kar rahe hain
import requests                     # website se data fetch karne ke liye
from bs4 import BeautifulSoup      # HTML parse karne ke liye
import json                         # data ko JSON format me save karne ke liye


# 2. Target website URL (jahan se data scrape karna hai)
url = 'https://www.bu.edu/president/boston-university-facts-stats/'


# 3. Headers add kar rahe hain (taaki website hume bot na samjhe)
headers = {
    "User-Agent": "Mozilla/5.0"
}


# 4. Website ko request bhejna (data fetch karna)
res = requests.get(url, headers=headers)

# Status code print (200 = success)
print("Status:", res.status_code)


# 5. HTML content ko parse karna (tree structure me convert)
soup = BeautifulSoup(res.text, 'html.parser')


# 6. Empty dictionary bana rahe hain jisme final data store hoga
data = {}


# 7. Website me jitne bhi <ul> (unordered list) hain unko loop kar rahe hain
for ul in soup.find_all('ul'):
    
    # Har <ul> ke andar ke sab <li> (list items) nikal rahe hain
    items = ul.find_all('li')
    
    # Agar list me items hain tabhi aage process kare
    if items:
        
        # Har <li> ka text clean karke list me store kar rahe hain
        values = [li.get_text(strip=True) for li in items]
        
        # Us <ul> ke upar jo nearest heading (h1/h2/h3) hai use find kar rahe hain
        heading = ul.find_previous(['h1','h2','h3'])
        
        # Agar heading mil jaye to usko title bana ke data me store karo
        if heading:
            title = heading.get_text(strip=True)
            
            # Dictionary me store: {heading: list of items}
            data[title] = values


# 8. Extracted data ko JSON file me save karna
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)


# 9. Console me JSON data print karna (pretty format me)
print(json.dumps(data, indent=4, ensure_ascii=False))


# 2. Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file

# 1. Required libraries import kar rahe hain
import requests   # API call karne ke liye (internet se data lana)
import json       # data ko JSON format me handle/save karne ke liye


# 2. UCI ka official API endpoint (yahan se dataset list milegi)
url = "https://archive.ics.uci.edu/api/datasets/list"


# 3. API ko request bhejna (GET request)
response = requests.get(url)

# Status code print (200 = success, 404 = error, etc.)
print("Status:", response.status_code)


# 4. API response ko JSON me convert karna (Python dictionary ban jata hai)
data = response.json()


# 5. Clean aur structured data store karne ke liye empty list
datasets = []


# 6. API ke andar "data" key me actual dataset list hoti hai
for d in data["data"]:
    
    # Har dataset se required fields nikal rahe hain
    datasets.append({
        "Name": d.get("name"),          # dataset ka naam
        "Task": d.get("task"),          # ML task (Regression, Classification, etc.)
        "Instances": d.get("instances"),# total rows / data points
        "Features": d.get("features"),  # number of columns/features
        "Type": d.get("type")           # dataset type (Multivariate, etc.)
    })


# 7. Extracted data ko JSON file me save karna
with open("uci_datasets.json", "w", encoding="utf-8") as f:
    json.dump(datasets, f, indent=4)


# 8. Console me output check karna
print("Saved:", len(datasets))  # total datasets kitne save hue

# Sirf first 5 datasets pretty format me print (testing ke liye)
print(json.dumps(datasets[:5], indent=4))


# Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). 
# The table is not very structured and the scrapping may take very long time.


# 1. Required libraries import kar rahe hain
import requests                      # website se data fetch karne ke liye
from bs4 import BeautifulSoup       # HTML ko parse (read) karne ke liye
import json                          # data ko JSON format me save/print karne ke liye


# 2. Target URL (Wikipedia page jahan presidents ka data hai)
url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"


# 3. Headers add kar rahe hain (taaki request browser jaisa lage, block na ho)
headers = {
    "User-Agent": "Mozilla/5.0"
}


# 4. Website ko request bhejna
response = requests.get(url, headers=headers)


# 5. HTML content ko parse karna (tree structure me convert)
# 'html.parser' correct parser hai
soup = BeautifulSoup(response.text, 'html.parser')


# 6. Page me sabhi 'wikitable' tables find karna
tables = soup.find_all("table", {"class": "wikitable"})

# Pehla table select kar rahe hain (ye main presidents table hota hai)
table = tables[0]


# 7. Final data store karne ke liye empty list
data = []


# 8. Table ke sab rows (tr = table row) nikal rahe hain
rows = table.find_all('tr')


# 9. Text clean karne ke liye helper function
def clean(text):
    return text.replace("\n", " ").strip()   # newline hata ke clean text return


# 10. Har row ko process kar rahe hain (first row header hota hai, isliye skip)
for row in rows[1:]:
    
    # Har row ke columns (td + th) nikal rahe hain
    cols = row.find_all(["td", "th"])

    # Check kar rahe hain ki row valid hai (minimum columns hone chahiye)
    if len(cols) >= 5:
        
        # Required fields extract kar rahe hain
        president = {
            "No": clean(cols[0].get_text()),     # president number
            "Name": clean(cols[1].get_text()),   # president name
            "Term": clean(cols[2].get_text()),   # term duration
            "Party": clean(cols[3].get_text()),  # political party
        }

        # List me add kar rahe hain
        data.append(president)


# 11. Extracted data ko JSON file me save karna
with open("presidents.json", "w", encoding='utf-8') as f:
    json.dump(data, f, indent=4)


# 12. Console me output check karna
print("Saved:", len(data))  # total presidents count

# Sirf first 5 records pretty format me print
print(json.dumps(data[:5], indent=4))


# 1. Libraries import
import requests
from bs4 import BeautifulSoup


# 2. Function: country → current president
def get_current_president(country):
    
    # 3. Country mapping
    country_map = {
        "India": "President_of_India",
        "USA": "President_of_the_United_States"
    }

    if country not in country_map:
        return "Country not supported"

    # 4. URL create
    url = f"https://en.wikipedia.org/wiki/{country_map[country]}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # 5. Request bhejna
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        return "Error fetching data"

    # 6. Parse HTML
    soup = BeautifulSoup(res.text, "html.parser")

    # 7. Infobox find karo
    infobox = soup.find("table", class_="infobox")

    if not infobox:
        return "Infobox not found"

    # 🔥 "Incumbent" text directly search karo (better approach)
    incumbent = infobox.find(string=lambda text: text and "Incumbent" in text)

    if incumbent:
        # parent row → next td me name hota hai
        parent_row = incumbent.find_parent("tr")
        if parent_row:
            td = parent_row.find("td")
            if td:
                return td.get_text(strip=True)

    return "President not found"



# 🔥 TEST
print("India:", get_current_president("India"))
print("USA:", get_current_president("USA"))