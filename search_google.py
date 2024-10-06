from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def get_search_results(query, num_links):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    driver.get("https://www.google.com")

    search_box = driver.find_element("name", "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    time.sleep(5)

    links = driver.find_elements("tag name", "a")

    result_links = []
    arxiv_link = None

    for link in links:
        href = link.get_attribute("href")
        if href and (href.startswith("http") or href.startswith("https")) and "google" not in href:
            if "arxiv.org" in href and not arxiv_link:
                arxiv_link = href
            if len(result_links) < num_links:
                result_links.append(href)

    print(f"First {num_links} links:")
    for i, link in enumerate(result_links):
        print(f"{i+1}: {link}")

    if arxiv_link:
        print("\nArXiv link found:")
        print(arxiv_link)
    else:
        print("\nNo ArXiv link found.")

    driver.quit()

get_search_results("UltraMedical: Building Specialized Generalists in Biomedicine arxiv", 5)
