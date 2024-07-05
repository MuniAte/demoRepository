

import requests, base64, urllib.parse

userToken = "webmaster@muniate.gob.pe:Hw2BARCP3fafORkioWjvN83SqFqIP1kn"
credentials = (base64.b64encode(userToken.encode()).decode())

data = {
    'env':'verifApp',
    'phone_number': '51912307990',
    'code': '543529',

}

url = "https://api.labsmobile.com/otp/validateCode?"+urllib.parse.urlencode(data, doseq=True)
payload = {}
headers = {
  'Authorization': 'Basic %s' % credentials,
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


            