import numpy as np
import pandas as pd
from datetime import date

def get_chunk_csv(path, chunk_size=100):
    
    data = pd.read_csv(path, chunksize=chunk_size, index_col=0, engine='python')   
    chunk_data = pd.DataFrame(data.get_chunk(chunk_size))   
    df = chunk_data.to_csv('COVID_19_data_100.csv')

    return df  

if __name__ == "__main__":
    
    file = 'COVID-19_Case_Data_Clean.csv'
        
    get_chunk_csv(file)