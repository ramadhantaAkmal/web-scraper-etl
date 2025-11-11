import pandas as pd
import datetime
from jobs_scrape import scrape_jobs

def clean_result_data(data: dict) -> pd.DataFrame:
    jobs_results_dict = data["jobs_results"]

    df = pd.DataFrame.from_dict(jobs_results_dict)

    df.drop(['share_link','thumbnail','extensions','job_id','via'], axis=1, inplace=True)
    print(df['detected_extensions'])

    df['schedule_type'] = df['detected_extensions'].apply(lambda x: x.get('schedule_type'))
    df.drop('detected_extensions', axis=1, inplace=True)
    return df

i=0
next_page_token=""
df=pd.DataFrame()
while i <= 3:
    data = scrape_jobs(next_page_token)
    next_page_token=data["serpapi_pagination"]["next_page_token"]
    clean_data = clean_result_data(data)
    df = pd.concat([df, clean_data], axis=0, ignore_index=True)
    i += 1

current_date = datetime.date.today()
df.to_json(f'jobs-result-weekly/jobs-result-{current_date}.json', orient='records', indent=4)