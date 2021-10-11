import requests
  
def line_message(msg):
    token2 = "ApqUpLV5MqHE2UQlne5Zauqvw2ndTJpWea3jmYLAgko"
    headers2 =  {
        "Authorization": "Bearer " + token2, 
        "Content-Type" : "application/x-www-form-urlencoded"
   }
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers2, params = payload)
    return r.status_code

def send_pic(msg, pic):
    token2 = "ApqUpLV5MqHE2UQlne5Zauqvw2ndTJpWea3jmYLAgko"
    headers =  {
        "Authorization": "Bearer " + token2
    }
    payload = {'message': msg}
    files = {'imageFile': open(pic, 'rb')}
    #r = requests.post("https://notify-api.line.me/api/notify", headers = headers2, params = payload, files = files)
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload, files = files)
    return r.status_code