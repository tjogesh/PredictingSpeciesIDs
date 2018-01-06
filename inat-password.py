import requests

site = "https://www.inaturalist.org"
app_id = '5951a7fb08e97a1cb33f59362fd71aad49aa0dcc294f19e59729039103c1d3f6'
app_secret = '75cf928d7d1c468abb9f800c754658e4feb729c486388731d3b2f6ecae230533'
username = 'taniajogesh'
password = 'i<3J0hnny'

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