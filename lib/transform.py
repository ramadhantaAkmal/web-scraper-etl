import pandas as pd

def clean_result_data(data: dict) -> pd.DataFrame:
    jobs_results_dict = data["jobs_results"]

    df = pd.DataFrame.from_dict(jobs_results_dict)

    df.drop(['share_link','thumbnail','extensions','job_id','via'], axis=1, inplace=True)
    print(df['detected_extensions'])

    df['schedule_type'] = df['detected_extensions'].apply(lambda x: x.get('schedule_type'))
    df.drop('detected_extensions', axis=1, inplace=True)
    return df

