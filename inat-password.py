import requests

site = "https://www.inaturalist.org"
app_id = 'YOUR APP ID'
app_secret = 'YOUR APP SECRET'
username = 'YOUR USERNAME'
password = 'YOUR PASSWORD'

# Send a POST request to /oauth/token with the username and password
payload = {
  'client_id': app_id,
  'client_secret': app_secret,
  'grant_type': "password",
  'username': username,
  'password': password
}
print "POST %s/oauth/token, payload: %s" % (site, payload)
response = requests.post(("%s/oauth/token" % site), payload)
print "RESPONSE"
print response.content
print
# response will be a chunk of JSON looking like
# {
#   "access_token":"xxx",
#   "token_type":"bearer",
#   "expires_in":null,
#   "refresh_token":null,
#   "scope":"write"
# }
 
# Store the token (access_token) in your app. You can now use it to make authorized
# requests on behalf of the user, like retrieving profile data:
token = response.json()["access_token"]
headers = {"Authorization": "Bearer %s" % token}
print "GET %s/users/edit.json, headers: %s" % (site, headers)
print "RESPONSE"
print requests.get(("%s/users/edit.json" % site), headers=headers).content
print