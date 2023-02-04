import pandas as pd 
import numpy as no 
import openpyxl as opx
from datetime import datetime as dt

import files
from files import *

nss = pd.read_csv(nss_file)
sf = pd.read_csv(sf_file)

nss['signup_timestamp'] = pd.to_datetime(nss['signup_timestamp'])
sf['signup_timestamp'] = pd.to_datetime(sf['signup_created_date'])


sf = sf.rename(mapper={'effort_name': 'effort_nm','campaign_name': 'campaign_nm','signup_creatd_date':'signup_timestamp'},axis = 'columns').drop('signup_created_date',axis=1,inplace=False) 
nss = nss.drop('affiliate',axis='columns',inplace=False)


print(sf)
print (nss)