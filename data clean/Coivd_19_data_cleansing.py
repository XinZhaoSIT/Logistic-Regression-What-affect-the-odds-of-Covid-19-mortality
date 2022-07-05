import numpy as np
import pandas as pd
from datetime import date

def get_chunk_csv(path, chunk_size=100):
    
    data = pd.read_csv(path, chunksize=chunk_size, index_col=0, engine='python')   
    chunk_data = pd.DataFrame(data.get_chunk(chunk_size))   
    df = chunk_data.to_csv('COVID_19_data_100.csv')

    return df  


if __name__ == "__main__":
    
    file = 'COVID-19_Case_Surveillance_Public_Use_Data.csv'
    
    data = pd.read_csv(file, engine='python')
    
    data = data.replace('Unknown',np.nan)
    data = data.replace('Missing',np.nan)
    data['sex'] = data.sex.replace('Other',np.nan)
    
    data = data.dropna(subset=['hosp_yn','icu_yn','death_yn','medcond_yn','sex'])
    
#    data['current_status'] = data.current_status.replace('Probable Case',0)
#    data['current_status'] = data.current_status.replace('Laboratory-confirmed case',1)
    data.drop('pos_spec_dt', axis=1, inplace=True)
    
    data['Race and ethnicity (combined)'] = data['Race and ethnicity (combined)'].replace(np.nan,'Unknown')
    data['onset_dt'] = data.onset_dt.replace(np.nan,'symptomless')
    
    data['cdc_report_dt'] = pd.to_datetime(data['cdc_report_dt'])
    data['onset_dt'] = pd.to_datetime(data['onset_dt'])
    
    
    for i in data['onset_dt']:
        if i != 'symptomless':
            data['interval_dt'] = data['cdc_report_dt'] - data['onset_dt']
        elif i == 'symptomless':
            data['interval_dt'] = 'symptomless'
    
    data.to_csv('COVID-19_Case_Data_Clean.csv',index=False)
    
    
    


