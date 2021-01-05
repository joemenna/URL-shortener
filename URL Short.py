import requests


#Access to API
username = 'o_1vqlrrr35p'
password = 'Chichi30!'

#Get access token
auth_res = requests.post('https://api-ssl.bitly.com/oauth/access_token', auth=(username,password))
if auth_res.status_code == 200:
    # if response is ok get the token
    access_token = auth_res.content.decode()
    #print('[!] Got access token:', access_token)
else:
    print('[!] Cannot get access token, exiting...')
    exit()

# construct request header
headers = {'Authorization': f'Bearer {access_token}'}

#get the group UID associated with account
groups_res = requests.get('https://api-ssl.bitly.com/v4/groups', headers=headers)
if groups_res.status_code == 200:
    # if response is OK, get the GUID
    groups_data = groups_res.json()['groups'][0]
    guid = groups_data['guid']
else:
    print('[!] Cannot get GUID, exiting...')
    exit()
x = input('URL:')
url = f"{x}"
# make the POST request to get shortened URL for `url`
shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid, "long_url": url}, headers=headers)
if shorten_res.status_code == 200:
    # if response is OK, get the shortened URL
    link = shorten_res.json().get("link")
    print("Shortened URL:", link)
   