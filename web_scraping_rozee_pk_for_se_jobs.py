

pip install selenium pandas  BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

# Setup headless Chrome
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.binary_location = '/tmp/chrome-linux64/chrome'
service = Service('/tmp/chromedriver-linux64/chromedriver')
driver = webdriver.Chrome(service=service, options=options)

# Start URL
url = "https://www.rozee.pk/search/software-engineer-jobs-in-pakistan"
driver.get(url)
time.sleep(5)

all_jobs = []

while True:
    # Parse the current page
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    job_blocks = soup.find_all('div', class_='job')

    for job in job_blocks:
        try:
            title_tag = job.find('h3', class_='s-18')
            title = title_tag.text.strip()
            link = "https://www.rozee.pk" + title_tag.find('a')['href']

            cname_div = job.find('div', class_='cname')
            company = cname_div.find_all('a', class_='display-inline')[0].text.strip()
            city = cname_div.find_all('a', class_='display-inline')[1].text.strip()

            skills_tags = job.find_all('span', class_='label')
            skills = ', '.join([s.text.strip() for s in skills_tags])

            desc_tag = job.find('div', class_='jbody')
            description = desc_tag.text.strip() if desc_tag else ''

            salary_icon = job.find('i', class_='sal')
            salary_span = salary_icon.find_next('span') if salary_icon else None
            salary = salary_span.text.strip() if salary_span else ''

            all_jobs.append({
                'Title': title,
                'Company': company,
                'City': city,
                'Skills': skills,
                'Description': description,
                'Salary': salary,
                'Link': link
            })
        except Exception as e:
            print(" Skipped a job due to error:", e)
            continue

    #click the "Next" button
    try:
        next_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Next')]"))
        )
        driver.execute_script("arguments[0].click();", next_btn)
        time.sleep(5)  # Wait for next page to load
        print(" Moved to next page")
    except:
        print(" No more pages to scrape.")
        break

driver.quit()

# Save
df = pd.DataFrame(all_jobs)
df.to_excel("rozee_software_jobs_all_pages.xlsx", index=False)
print(" Saved all job listings to Excel.")
print(df.head())
