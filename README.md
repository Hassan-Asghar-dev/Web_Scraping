# Web_Scraping

```
$ ls Web_Scraping/
web_scraping_rozee_pk_for_se_jobs
data_cleaning
rozee_software_jobs_2025_july_dirty_data.xlsx
rozee_software_jobs_cleaned_data.xlsx
```

Scrapes software engineering job listings from [Rozee.pk](https://www.rozee.pk/) (July 2025) and cleans the collected data into an analysis-ready dataset.

`Python` · `Pandas` · `Excel`

---

### 1. `web_scraping_rozee_pk_for_se_jobs`
Scrapes software engineering job listings from Rozee.pk for July 2025.

### 2. `data_cleaning`
Cleans and normalizes the raw scraped data.

### 3. `rozee_software_jobs_2025_july_dirty_data.xlsx`
Original, uncleaned scraped output.

### 4. `rozee_software_jobs_cleaned_data.xlsx`
Final cleaned dataset.

---

### Pipeline

```
Rozee.pk  →  web_scraping_rozee_pk_for_se_jobs  →  dirty_data.xlsx  →  data_cleaning  →  cleaned_data.xlsx
```

### Usage

```bash
pip install -r requirements.txt
python web_scraping_rozee_pk_for_se_jobs.py
python data_cleaning.py
```

---

> Built for educational/portfolio purposes. Data reflects listings available on Rozee.pk as of July 2025 and may be outdated. Review Rozee.pk's terms of service before reuse.
