from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--window-size=1920x1080")  # Set a virtual window size
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(), options=chrome_options)
driver.get("https://www.google.com")
search_box = driver.find_element("name", "q")
search_query = "UltraMedical: Building Specialized Generalists in Biomedicine arxiv"
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)
time.sleep(5)

arxiv_link = None
links = driver.find_elements("tag name", "a")
for link in links:
    href = link.get_attribute("href")
    if href and "arxiv.org" in href:
        arxiv_link = href
        break

if arxiv_link:
    print(arxiv_link)
else:
    print("No ArXiv link found.")

driver.quit()
