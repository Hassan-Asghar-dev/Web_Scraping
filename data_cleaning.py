
#cleaning the link coloumn (it had duplicate domain in the links)

import pandas as pd
import re

# path
file_path = '/content/sample_data/rozee_software_jobs_all_pages.xlsx'

# loading data file
df = pd.read_excel(file_path)

# Cleaning function
def clean_link(link):
    if pd.isna(link):
        return link
    # Remove duplicate domain if present
    link = re.sub(r'https://www\.rozee\.pk//www\.rozee\.pk', 'https://www.rozee.pk', link)
    # Ensure only one slash after domain
    link = re.sub(r'https://www\.rozee\.pk/+', 'https://www.rozee.pk/', link)
    return link

# Apply the function
df['Link'] = df['Link'].apply(clean_link)

# Save to new file
cleaned_file_path = '/content/sample_data/rozee_software_jobs.xlsx'
df.to_excel(cleaned_file_path, index=False)

print(" Cleaned file saved to:", cleaned_file_path)

# Cleaning City and Company coloumns Cleaned these columns has (,) in every cell after names.
import pandas as pd

# Load the cleaned file
file_path = '/content/sample_data/rozee_software_jobs_all_pages_cleaned.xlsx'
df = pd.read_excel(file_path)

# Function to remove commas and strip whitespace
def clean_text(text):
    if pd.isna(text):
        return text
    return str(text).replace(',', '').strip()

# Apply to both columns
df['Company'] = df['Company'].apply(clean_text)
df['City'] = df['City'].apply(clean_text)

# Save the result to a new file
final_file_path = '/content/sample_data/rozee_software_jobs_all_final.xlsx'
df.to_excel(final_file_path, index=False)

print(" Company and City columns cleaned. Final file saved to:", final_file_path)

#filling missing cells in salary and skills
import pandas as pd

# Load the final cleaned file
file_path = '/content/sample_data/rozee_software_jobs_all_final.xlsx'
df = pd.read_excel(file_path)

# Fill missing or empty 'Skills' with 'Not Described'
df['Skills'] = df['Skills'].fillna('Not Described')
df['Skills'] = df['Skills'].replace('', 'Not Described')

# Fill missing or empty 'Salary' with 'Not Mentioned'
df['Salary'] = df['Salary'].fillna('Not Mentioned')
df['Salary'] = df['Salary'].replace('', 'Not Mentioned')

# Save to a new final file
final_output_path = '/content/sample_data/rozee_software_jobs_final.xlsx'
df.to_excel(final_output_path, index=False)

print(" Skills and Salary columns cleaned. File saved to:", final_output_path)
