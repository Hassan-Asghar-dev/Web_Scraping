<div align="center">

# 🕷️ Web_Scraping — Rozee.pk Software Jobs

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
<img src="https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white" alt="Excel"/>
<img src="https://img.shields.io/badge/Rozee.pk-00A651?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Rozee.pk"/>

<img src="https://img.shields.io/badge/status-completed-brightgreen?style=flat-square" alt="status"/>
<img src="https://img.shields.io/badge/data-July_2025-orange?style=flat-square" alt="data period"/>
<img src="https://img.shields.io/badge/records-cleaned_%26_raw-blueviolet?style=flat-square" alt="records"/>

</div>

<br>

```
$ ls Web_Scraping/
web_scraping_rozee_pk_for_se_jobs
data_cleaning
rozee_software_jobs_2025_july_dirty_data.xlsx
rozee_software_jobs_cleaned_data.xlsx
```

Scrapes software engineering job listings from [Rozee.pk](https://www.rozee.pk/) (July 2025) and cleans the collected data into an analysis-ready dataset.

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
