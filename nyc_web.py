import requests  
h = {'User-Agent': 'Mozilla/5.0'}  
r = requests.get("https://en.wikipedia.org/wiki/New_York_City", headers=h)  
print("Status Code:", r.status_code)  
print("Title Snippet:", r.text[:50]) 
