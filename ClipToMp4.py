import urllib.request
import requests
import json
import os

def downloadclips(link):
    linkname = link[24:]
    print(linkname)
    r = requests.post('https://gql.twitch.tv/gql', data=json.dumps([
        {
        "operationName":"ClipsDownloadButton",
        "variables":{
            "slug":linkname
        },
        "extensions":{
            "persistedQuery":{
                "version":1,
                "sha256Hash":"6e465bb8446e2391644cf079851c0cb1b96928435a240f07ed4b240f0acc6f1b"
            }
        }
        }
    ]), headers={"Client-Id":"kimne78kx3ncx6brgo4mv6wki5h1ko"})

    list = eval(r.content)
    list = list[0]
    list = list['data']['clip']['videoQualities']
    list = list[0]['sourceURL']
    print(list)
    urllib.request.urlretrieve(list, 'VideoInfo/Videos/'+link[24:]+'.mp4') 
    return(link[24:])