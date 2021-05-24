import requests
import json

def FindClips():
    # list of streamers to check for top clips
    twitchstreamers = ['Foolish__Gamers','Ranboolive','Philza','Tubbolive','tommyinnit','sapnap','CaptainPuffy','quackity','fundy','tubbo','jackmanifoldtv','punz','hbomb94','badboyhalo','tapl','CaptainSparklez','Dreamwastaken','purpled','gamerboy80','astelic','thisisnotgeorgenotfound','tommyinnitalt','ranboobutnot','awesamdude','eret','5upp','georgenotfound']
    #preset variable which stores all the clips
    finalres = []
    #loops through streamers and finds top clips
    for streamer in twitchstreamers:
        #this is the data thats sent, like the stuff that says the gql request on twitch, the streamer is the streamer name
        UserSearch = [{"operationName":"ClipsCards__User","variables":{"login": streamer,"limit":5,"criteria":{"filter":"LAST_DAY"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"b73ad2bfaecfd30a9e6c28fada15bd97032c83ec77a0440766a56fe0bd632777"}}}]

        # this is an authentication header which needs to be used
        headers={"Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko"}

        # this is the post request sent
        r = requests.post(
            'https://gql.twitch.tv/gql',  # request sent to this link
            data=json.dumps(UserSearch),  # this is the request payload
            headers=headers  # these are the request headers
        )

        response = json.loads(r.content)  # this line  of code loads the response i get

        # the rest of the code just formats the response that you got from the request so that you have a list of about 35 clips
        response = response[0] 
        response = response['data']
        #response = response['game']   use for twitchgoup
        response = response['user']       #use for twitch streamer
        response = response['clips']
        response = response['edges']
        for user in response:
            finalres.append(
                [
                    user['node']['title'],
                    user['node']['viewCount'],
                    user['node']['url'],
                    user['node']['broadcaster']['displayName'],
                    user['node']['thumbnailURL'],
                ]
            )
        print('User Done: ',streamer)
    finalres = sorted(finalres, key=lambda a:a[1])  # this line sorts it by views, so we have a list of most popular to least popular clip
    return finalres
