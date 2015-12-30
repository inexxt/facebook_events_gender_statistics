import requests

accessToken = "SECRET"
# https://graph.facebook.com/oauth/access_token?client_id=YOUR_ID&client_secret=YOUR_SECRET&grant_type=client_credentials
# ID and YOUR_SECRET can be found in the app management page
# alternatively, under the link https://developers.facebook.com/tools/explorer/ one can generate personal token (get token - check "events") 

events = {
  "Czytanie2016" : 1576427339262530, 
  "Czytanie2015" : 315561018642822, 
  "Kiełbasa" : 565147766966013, 
  "500nameza" : 926339064129407, 
  "schudnejakzenek" : 516152078551716, 
  "kinganieoszuka" : 862631100425849, 
  "wodapopierogach" : 1527395404254768,
  "zagadamdodziewczyny" : 532157026939652 }

def process(url, test):

  girls = 0
  boys = 0

  while (url != ""):
    response = requests.get(url)
    if(response.status_code != 200):
      return 1, 1
    data = response.json()
    
    for person in data["data"]:
      name = person["name"].split(" ")[0]
      is_girl = name[-1] == 'a'
      if (is_girl):
        girls += 1
      else:
        boys += 1
    
    if (not test):
      if "next" in data["paging"].keys():
        url = data["paging"]["next"]
      else:
        url = ""
    else:
      url = ""
  return girls, boys

i = 0
for (eventName, eventId) in events.items():
  # i += 1
  # option = "attending" #TODO create list of possible choices
  # limit = 1000
  # url = "https://graph.facebook.com/v2.5/{0}/{1}?access_token={2}&pretty=0&limit={3}".format(eventId, option, accessToken, limit)
  # print("({0}) Event: {1} url: {2})".format(i, eventName, url))
  # girls, boys = process(url, False)
  # total = girls + boys
  # print("Girls {0}% Boys {1}% out of {2}\n".format(round(girls/total*100), round(boys/total*100), total))
  print("https://facebook.com/events/"+str(eventId))

