# Broskies_hubtasks_day3

🔹 What We Built

We built a Python script that:

1. Connects to a news website (e.g., BBC News).


2. Fetches the HTML content of the page using the requests library.


3. Uses BeautifulSoup to parse the HTML and extract news headlines.


4. Stores the extracted headlines in a .txt file for easy access and later analysis.



So the final output is a file like headlines.txt, which contains a neatly formatted list of the latest headlines.


🔹 Why We Built It

Automated Data Collection → Instead of manually checking the website for news, our script fetches the headlines automatically.

Practice with Python Libraries → This task shows practical usage of requests (for fetching web data) and BeautifulSoup (for parsing HTML).

Real-World Relevance → News scraping is a real-world use case in data science, journalism, finance, and research.

Internship Skill Demonstration → It demonstrates core developer skills like automation, file handling, and understanding of HTML structure.



🔹 How We Built It (Step by Step)

1. Choose a Website → Selected BBC News (https://www.bbc.com/news) because it is public and headlines are easy to locate.


2. Fetch the HTML Page → Used requests.get(URL) to download the raw HTML of the webpage.


3. Parse the HTML → Used BeautifulSoup to analyze the structure and extract text from headline tags (<h3> in BBC’s case).


4. Extract Clean Text → Collected only meaningful text (ignoring empty tags or duplicates).


5. Save Output → Wrote the headlines into a text file headlines.txt using Python’s file handling.


🔹 Tools & Libraries Used

Python → Programming language.

Requests → To fetch the HTML content from the website.

BeautifulSoup → To parse and extract specific elements from HTML.

File Handling → To save results in a text file.


🔹 Deliverables

1. Python Script (.py) → Example: news_scraper.py.


2. Text File (.txt) → Example: headlines.txt containing extracted news.


🔹 Outcome

Successfully automated data collection from a public website.

Produced a ready-to-use dataset of news headlines.

Demonstrated practical use of web scraping for real-world tasks.

