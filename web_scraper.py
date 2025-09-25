import requests
from bs4 import BeautifulSoup

# Step 1: Choose a news website (example: BBC News)
URL = "https://www.bbc.com/news"

# Step 2: Fetch HTML content
response = requests.get(URL)
if response.status_code != 200:
    print("Failed to retrieve webpage")
    exit()

# Step 3: Parse HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Find headlines (BBC uses <h3> for headlines)
headlines = soup.find_all("h3")

# Step 5: Extract and clean text
news_list = []
for h in headlines:
    title = h.get_text(strip=True)
    if title and title not in news_list:
        news_list.append(title)

# Step 6: Save headlines to a text file
with open("headlines.txt", "w", encoding="utf-8") as f:
    for i, news in enumerate(news_list, start=1):
        f.write(f"{i}. {news}\n")

print("✅ Headlines saved to headlines.txt successfully!")
