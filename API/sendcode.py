import requests, base64, urllib.parse

userToken = "webmaster@muniate.gob.pe:Hw2BARCP3fafORkioWjvN83SqFqIP1kn"
credentials = (base64.b64encode(userToken.encode()).decode())

data = {
    'env':'verifApp',
    'sender': 'MyBRAND',
    'phone_number': '51912307990',
    'message':'The code to verify your username is %CODE%'
}

url = "https://api.labsmobile.com/otp/sendCode?"+urllib.parse.urlencode(data, doseq=True)
payload = {}
headers = {
  'Authorization': 'Basic %s' % credentials,
}
#psot request
response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


            