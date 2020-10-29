import requests

headers = {
    'Authorization': 'Bearer {f3afbf82e53c51c95dab8944bddecab753a833cb}',
    'Content-Type': 'application/json',
}


data = '{ "long_url": "https://dev.bitly.com/api-reference#createBitlink", "domain": "bit.ly", "group_guid": "Ba1bc23dE4F" }'

response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

print(response)