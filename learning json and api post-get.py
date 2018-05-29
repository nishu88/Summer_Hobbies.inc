#Python VERSION:::: 3.6

#Author

#From Github account : nishu88

#REFER ------ https://www.youtube.com/watch?reload=9&v=0yn7_YuIBdo ------

#Command on CMD =  "pip install requests"


import requests
import urllib.parse

main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'
address = 'lhr'
url = main_api + urllib.parse.urlencode({'address':address})

print(url)

json_data = requests.get(url).json()
print(json_data)

#USE a JSON formatter to figure out which result u need to pick from the json_datas

json_status = json_data['status']
print('API status: '+ json_status)

formatted_address = json_data['results'][0]['formatted_address']
print(formatted_address)
