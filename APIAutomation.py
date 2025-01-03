import requests
url="http://192.168.0.162:8080/api/Contractor/CheckMobileNumber"
payload={
    "Mobile":"8087333794"
}
response=requests.get(url,json=payload)
if response.status_code==200:
    try:
     data=response.json()
     print("Repsonse Data: ",data)
    except requests.exceptions.JSONDecodeError:
        print("Reponse not in JSON")
    except requests.exceptions.HTTPError:
        print("HTTP Error Code")
else:
        print("Response code",response.status_code)
        print(response.text)

