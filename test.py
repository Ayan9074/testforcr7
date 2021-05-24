import requests
import json

def FindClips():
    TopicSearch = [{"operationName":"incrementClipViewCount","variables":{"input":{"slug":"CrispyAgileSandstormDoritosChip-m1XeRwqaC8gpMUOl"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"6b2f169f994f2b93ff68774f6928de66a1e8cdb70a42f4af3a5a1ecc68ee759b"}}}]
    twitchstreamers = ['Foolish__Gamers','Ranboolive','Philza','Tubbolive','tommyinnit','sapnap','CaptainPuffy','quackity','fundy','tubbo','jackmanifoldtv','punz','hbomb94','badboyhalo','tapl','CaptainSparklez']
    finalres = []
    for streamer in twitchstreamers:
        UserSearch = [{"operationName":"ClipsCards__User","variables":{"login": streamer,"limit":5,"criteria":{"filter":"LAST_DAY"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"b73ad2bfaecfd30a9e6c28fada15bd97032c83ec77a0440766a56fe0bd632777"}}}]

        headers={"Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko"}

        r = requests.post(
            'https://gql.twitch.tv/gql', 
            data=json.dumps(TopicSearch), 
            headers=headers
        )

        response = r.content
FindClips()