import requests
import json

def FindClips():
    TopicSearch = [{"operationName":"ClipsCards__Game","variables":{"gameName":"Minecraft","limit":5,"criteria":{"languages":["EN"],"filter":"LAST_DAY"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"0d8d0eba9fc7ef77de54a7d933998e21ad7a1274c867ec565ac14ffdce77b1f9"}}}]
    twitchstreamers = ['Foolish__Gamers','Ranboolive','Philza','Tubbolive','tommyinnit','sapnap','CaptainPuffy','quackity','fundy','tubbo','jackmanifoldtv','punz','hbomb94','badboyhalo','tapl','CaptainSparklez','Dreamwastaken','purpled','gamerboy80','astelic','thisisnotgeorgenotfound','tommyinnitalt','ranboobutnot','awesamdude','eret','5upp','georgenotfound']
    finalres = []
    for streamer in twitchstreamers:
        UserSearch = [{"operationName":"ClipsCards__User","variables":{"login": streamer,"limit":5,"criteria":{"filter":"LAST_DAY"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"b73ad2bfaecfd30a9e6c28fada15bd97032c83ec77a0440766a56fe0bd632777"}}}]

        headers={"Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko"}

        r = requests.post(
            'https://gql.twitch.tv/gql', 
            data=json.dumps(UserSearch), 
            headers=headers
        )

        response = json.loads(r.content)
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
    finalres = sorted(finalres, key=lambda a:a[1])
    return finalres