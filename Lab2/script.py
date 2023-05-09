import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)
import numpy as np
import pandas as pd
import zat.log_to_dataframe
import pathlib
from pathlib import Path
dir_path = pathlib.Path.cwd()
path = Path(dir_path,'Lab2', 'Zeek', 'dns.log')
df = zat.log_to_dataframe.LogToDataFrame()
zeek_df = df.create_dataframe(path)
domain = zeek_df['query']
domain.name='CNAME'
path = Path(dir_path,'Lab2', 'damaged.txt')
df = pd.read_csv(path,sep="\s+",names=['redirect_to','CNAME'])
dmgd = df['CNAME']
edin = pd.merge(domain,dmgd, how='left',indicator='exists', on=['CNAME'],)
edin['exists'] = np.where(edin.exists == 'both',True,False)
nezh_traff = edin['exists'].value_counts(normalize=True)[1]*100
print("Процент нежелательного трафика: ", round(nezh_traff,3))
