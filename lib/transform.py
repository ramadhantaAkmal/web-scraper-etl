import pandas as pd

def clean_result_data(data: dict) -> pd.DataFrame:
    jobs_results_dict = data["jobs_results"]

    #Convert dict data into DataFrame
    df = pd.DataFrame.from_dict(jobs_results_dict)

    #Removing unnecessary data
    df.drop(['share_link','thumbnail','extensions','job_id','via'], axis=1, inplace=True)

    #Extracting schedule type data from detected extensions column and create new schedule_type column
    df['schedule_type'] = df['detected_extensions'].apply(lambda x: x.get('schedule_type'))
    
    #Drop detected extension column because its unused
    df.drop('detected_extensions', axis=1, inplace=True)
    return df

