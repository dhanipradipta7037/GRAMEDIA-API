import requests
import json
import pandas as pd
import time

data = []

for x in range(1, 4):
    url = f'https://www.gramedia.com/api/algolia/search/product/?q=python&page={x}&per_page=20'
    r = requests.get(url).json()
    time.sleep(5)
    
    for i in range(0, len(r)):
        nama = r[i]['name']
        harga = r[i]['basePrice']
        items ={'Nama Buku':nama,
                'Harga Buku':harga
        }
        data.append(items)

df=pd.DataFrame(data)
print(df)


    
    
