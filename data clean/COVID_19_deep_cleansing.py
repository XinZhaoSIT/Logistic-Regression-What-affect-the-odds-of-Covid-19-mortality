import numpy as np
import pandas as pd
from datetime import date




if __name__ == "__main__":
    
    file = 'COVID-19_Case_Data_Clean.csv'
    
    data = pd.read_csv(file)
          
    data['interval_dt'] = data['interval_dt'].replace('symptomless',np.nan)
    
    data.to_csv('COVID-19_Case_Data_Clean.csv',index=False)
    