import requests

api_key="pGYXyj1o.dMMOV2q6u6STtCdkHCwuBcFMF2uK5joC"
query="what is an large language model?"


headers={
    'Content-Type': 'application/json',
    'Apikey': f'Api-Key {api_key}' 
}

data={
    'payload':query
}

url='https://payload.vextapp.com/hook/49MY7BKDLV/catch/$(kans)'

response=requests.post(url, json=data, headers=headers)

print(response.text)