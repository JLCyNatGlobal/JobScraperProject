# -*- coding: utf-8 -*-
"""*WebscraperDemo3api.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OGRSCbF_9GXA5l36X7ZcXZmz48sXbYx-
"""

import requests
import json
import csv

# API URL and parameters
url = "https://indeed12.p.rapidapi.com/jobs/search"

querystring = {"query":"cybersecurity","location":"chicago","page_id":["1, 2"],"locality":"us","fromage":"1","radius":"50","sort":"date"}



# Headers for the API request
headers = {
	"x-rapidapi-key": "1234/",
	"x-rapidapi-host": "indeed12.p.rapidapi.com"
}

# API request
response = requests.get(url, headers=headers, params=querystring)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Extract the JSON data

    # Pretty print the JSON structure to understand its format
    formatted_json = json.dumps(data, indent=4)
    print(formatted_json)  # Print to console

    # Specify the CSV file name
    csv_file = 'cyberjobsindeed_data.csv'

    # Open CSV file for writing
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(["company_name", "formatted_relative_time", "id", "link", "locality",
                         "location", "pub_date_ts_milli", "salary"])

        # Write data rows
        if 'hits' in data:
            for job in data['hits']:
                # Validate job fields
                if all(key in job for key in ['company_name', 'formatted_relative_time', 'id', 'link', 'locality', 'location', 'pub_date_ts_milli']):
                    salary_info = job.get('salary', {})
                    salary_str = f"{salary_info.get('min', '')}-{salary_info.get('max', '')} {salary_info.get('type', '')}"
                    writer.writerow([
                        job['company_name'],
                        job['formatted_relative_time'],
                        job['id'],
                        job['link'],
                        job['locality'],
                        job['location'],
                        job['pub_date_ts_milli'],
                        salary_str
                    ])
                else:
                    print(f"Error: Missing job fields for job ID {job.get('id', '')}")

    print(f"Data successfully written to {csv_file}")

else:
    print(f"Error: Unable to fetch data (Status code: {response.status_code})")
