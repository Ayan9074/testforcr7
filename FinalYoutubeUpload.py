from ClipToMp4 import downloadclips
from YoutubeUploader.__init__ import YouTubeUploader
from TwitchClipFinder.Newmethodthroughdb import FindClips
import json
import datetime
from datetime import timedelta
from ClipToMp4 import downloadclips
import random
import shutil
import os, glob

def clipchooser():
    top_clips = FindClips()
    top_clips.reverse()
    with open('VideoInfo/uploaded.json', 'r+') as json_file:
        maindata = json.load(json_file)
        data = maindata["uploaded"]
        for clip in top_clips:
            indonceclip = False
            for doneclip in data:
                if clip[0] == doneclip[0]:
                    indonceclip = True
                else:
                    pass
            if indonceclip == False:
                to_upload = clip
                break
        print(to_upload)
        for doneclip in data:
            change =  datetime.datetime.now() - datetime.datetime.strptime(doneclip[1], '%Y-%m-%d %H:%M:%S.%f')
            if str(change)[:5] == '1 day':
                data.remove(doneclip)
        data.append([to_upload[0],datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')])
        data = {"uploaded":data}
        print(data)
    with open('VideoInfo/uploaded.json','w') as outfile:
        json.dump(data, outfile)
    return to_upload
 
dir = 'VideoInfo/Videos'
for file in os.scandir(dir):
    os.remove(file.path)


chosenclip = clipchooser()
filename = 'VideoInfo/Videos/' + downloadclips(chosenclip[2]) + '.mp4'

def edit_metadata(details):
    clip_name = details[0]
    clip_streamer = details[3]
    with open('VideoInfo/MetaData/metadata.json', 'r+') as detailfile:
        maindata = json.load(detailfile)
    num = random.randint(0,10)
    if num == 10:
        maindata['title'] = clip_name + '  ( ' + clip_streamer + ' )'
    elif num == 9:
        maindata['title'] = clip_name + '  !!! ' + clip_streamer
    elif num == 8:
        maindata['title'] = clip_name + '  ||| ' + clip_streamer + ' |||'
    elif num == 7:
        maindata['title'] = clip_name + '  ----  ' + clip_streamer + '  ----  '
    elif num == 6:
        maindata['title'] = clip_name + '  ( ' + clip_streamer + ' )'
    elif num == 5:
        maindata['title'] = clip_name + '  !!!  ' + clip_streamer
    elif num == 4:
        maindata['title'] = clip_name + '  ||| ' + clip_streamer + ' |||'
    elif num == 3:
        maindata['title'] = clip_name + '  ----  ' + clip_streamer + '  ----  '
    else:
        maindata['title'] = clip_name + '  :D  (' + clip_streamer +     ')'
    maindata['description'] = "Follow " + clip_streamer + " on Twitch: " + 'https://www.twitch.tv/' + clip_streamer + ". If you are a streamer and want your clip removed please let me know on my discord: Name: Fendir Number:3154, or by email.                    Hashtags: #minecraft #Gaming #Clip"
    maindata['tags'] = ["Twitch","Minecraft", "Gaming", "Compilation","clip","clip_twitch","pog","pogclip","dreamplays","highiq","gamer","gamers","mc","dacraft",clip_streamer,clip_name]
    with open('VideoInfo/MetaData/metadata.json', 'w') as detailfile:
        json.dump(maindata, detailfile)

edit_metadata(chosenclip)
try:
    video_path = filename
    metadata_path = 'VideoInfo/MetaData/metadata.json'

    uploader = YouTubeUploader(video_path, metadata_path)
    was_video_uploaded, video_id = uploader.upload()
    assert was_video_uploaded
except:
    with open('VideoInfo/uploaded.json', 'r+') as detailfile:
        data = json.load(detailfile)
    data['uploaded'] = data['uploaded'][:-1]
    with open('VideoInfo/uploaded.json', 'w') as detailfile:
        json.dump(data, detailfile)