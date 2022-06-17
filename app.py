from flask import Flask, redirect, request, jsonify, render_template, url_for, session, Response

#trend
from pytrends.request import TrendReq

#articl
from itertools import count
import requests
from bs4 import BeautifulSoup 

#instagram
import instaloader
import pandas as pd
from instaloader import Instaloader, Profile
import re
from argparse import ArgumentParser
from sqlite3 import OperationalError, connect
from platform import system
from glob import glob
from os.path import expanduser

insta = instaloader.Instaloader()
loader = Instaloader()

MAX_DAYS = 50 

LIKES_WEIGHT = 1
COMMENTS_WEIGHT = 1
NUM_FOLLOWERS_WEIGHT = 1
NUM_POSTS_WEIGHT = 1
NUM_POSTS = 10

try:
    from instaloader import ConnectionException, Instaloader
except ModuleNotFoundError:
    raise SystemExit("Instaloader not found.\n  pip install [--user] instaloader")

def truncate(num):
    return re.sub(r'^(\d+\.\d{,2})\d*$',r'\1',str(num))

def send_get_request( url, params, extra_headers=None):
        url = build_get_url(url, params)
        did = ''.join(random.choice(string.digits) for num in range(19))
        url = build_get_url(url, {did_key: did}, append=True)
        signature = tiktok_browser.fetch_auth_params(url, language=language)
        url = build_get_url(url, {signature_key: str(signature)}, append=True)
        if extra_headers is None:
            headers = header
        else:
            headers = {}
            for key, val in extra_headers.items():
                headers[key] = val
            for key, val in headers.items():
                headers[key] = val
        data = get_req_json(url, params=None, headers=headers)
        return data



def get_cookiefile():
    default_cookiefile = {
        # "Windows": "~/AppData/Roaming/Mozilla/Firefox/Profiles/*/cookies.sqlite",
        # "Darwin": "~/Library/Application Support/Firefox/Profiles//cookies.sqlite",
        "Windows": "cookies.sqlite",
        "Darwin": "cookies.sqlite",
    }.get(system(), "~/.mozilla/firefox/*/cookies.sqlite")
    print(default_cookiefile)
    cookiefiles = glob(expanduser(default_cookiefile))
    print(cookiefiles)
    if not cookiefiles:
        raise SystemExit("No Firefox cookies.sqlite file found. Use -c COOKIEFILE.")
    return cookiefiles[0]


def import_session(cookiefile, sessionfile):
    print("Using cookies from {}.".format(cookiefile))
    conn = connect(f"file:{cookiefile}?immutable=1", uri=True)
    try:
        cookie_data = conn.execute(
            "SELECT name, value FROM moz_cookies WHERE baseDomain='instagram.com'"
        )
    except OperationalError:
        cookie_data = conn.execute(
            "SELECT name, value FROM moz_cookies WHERE host LIKE '%instagram.com'"
        )
    instaloader = Instaloader(max_connection_attempts=1)
    instaloader.context._session.cookies.update(cookie_data)
    username = instaloader.test_login()
    if not username:
        raise SystemExit("Not logged in. Are you logged in successfully in Firefox?")
    print("Imported session cookie for {}.".format(username))
    instaloader.context.username = username
    instaloader.save_session_to_file(sessionfile)

if __name__ == "__main__":
    p = ArgumentParser()
    p.add_argument("-c", "--cookiefile")
    p.add_argument("-f", "--sessionfile")
    args = p.parse_args()
    try:
        import_session(args.cookiefile or get_cookiefile(), args.sessionfile)
    except (ConnectionException, OperationalError) as e:
        raise SystemExit("Cookie import failed: {}".format(e))

#tiktok

import pandas as pd
from regex import L
from TikTokAPI import TikTokAPI
import re
import requests
from utils import random_key, build_get_url, get_req_json, get_req_content, get_req_text
from tiktok_browser import TikTokBrowser
import random
import string
# import asyncio 
import urllib
from datetime import datetime
import json
# import os
import pprint
import pyautogui

def truncate(num):
    return re.sub(r'^(\d+\.\d{,2})\d*$',r'\1',str(num))

def send_get_request( url, params, extra_headers=None):
        url = build_get_url(url, params)
        did = ''.join(random.choice(string.digits) for num in range(19))
        url = build_get_url(url, {did_key: did}, append=True)
        signature = tiktok_browser.fetch_auth_params(url, language=language)
        url = build_get_url(url, {signature_key: str(signature)}, append=True)
        if extra_headers is None:
            headers = header
        else:
            headers = {}
            for key, val in extra_headers.items():
                headers[key] = val
            for key, val in headers.items():
                headers[key] = val
        data = get_req_json(url, params=None, headers=headers)
        return data

headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 OPR/72.0.3815.378'}
jsn = json.load(open("cookie.json", "r", encoding="utf-8"))
api = TikTokAPI(jsn)
counttiktok = pd.DataFrame(columns = ['Likes', 'Comment', 'Share'])
cookie=None

user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0"
browser_lang = "en-US"
timezone = "Asia/Kolkata"
region='IN'
language='en'
did_key = "did"
tiktok_browser = TikTokBrowser(user_agent)
signature_key = "_signature"

if cookie is None:
    cookie = {}
verifyFp = cookie.get("s_v_web_id", "verify_kjf974fd_y7bupmR0_3uRm_43kF_Awde_8K95qt0GcpBk")
tt_webid = cookie.get("tt_webid", "6913027209393473025")

header= {
            'Host': 't.tiktok.com',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
            'Referer': 'https://www.tiktok.com/',
            'Cookie': 'tt_webid_v2={}; tt_webid={}'.format(tt_webid, tt_webid)
        }

default_params = {
            "aid": "1988",
            "app_name": "tiktok_web",
            "device_platform": "web",
            "referer": "",
            "user_agent": urllib.parse.quote_plus(user_agent),
            "cookie_enabled": "true",
            "screen_width": "1920",
            "screen_height": "1080",
            "browser_language": browser_lang,
            "browser_platform": "Linux+x86_64",
            "browser_name": "Mozilla",
            "browser_version": "5.0+(X11)",
            "browser_online": "true",
            "timezone_name": timezone,
            "page_referer": "https://www.tiktok.com/foryou?lang=en",
            "priority_region": region,

            "appId": "1180",
            "region": region,
            "appType": "t",

            "isAndroid": "false",
            "isMobile": "false",
            "isIOS": "false",
            "OS": "linux",
            "tt-web-region": region,

            "language": language,
            "verifyFp": verifyFp
        }

#camera

#from tkinter import Frame
import numpy as np
import cv2
#import math
import pyttsx3 

import HandTrackingModule as htm
import time
import autopy

# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# import face_recognition
from PIL import Image

engine = pyttsx3.init()
Wcam, Hcam = 640, 480
frameR = 100
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('database/training.xml')
cap = cv2.VideoCapture(0)
cap.set(3, Wcam)
cap.set(4, Hcam)
cap.set(cv2.CAP_PROP_BUFFERSIZE,3)
pTime = 0
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()
smoothening = 5
# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(
#     IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = cast(interface, POINTER(IAudioEndpointVolume))
# volRange = volume.GetVolumeRange()
# volume.SetMasterVolumeLevel(0, None)
# minVol = volRange[0]
# maxVol = volRange[1]
plocX, plocY = 0, 0
clocX, clocY = 0, 0

def gen():
    #global id
    while True:
        global frame, pTime, plocX ,plocY, clocX,clocY
        success, img = cap.read()
        
        img = detector.findHands(img)
        # img =cv2.flip(img,1)
        lmList, bbox = detector.findPosition(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, conf = recognizer.predict(gray[y:y+h, x:x+w])
            if (id == 1) :
                id = "rohim"
            if (id == 2) :
                id = "agis"
            if (id == 3):
                id = "Bebed"
            else:
                id = "unregistered"
            

            say1 = "Hello " + id

            
            # img =cv2.flip(img,1)
            # cv2.putText(img, str(id), (x+40,y-10), cv2.FONT_HERSHEY_DUPLEX,1,(0,255))
            cv2.putText(img, say1, (50, 80),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
           
        if len(lmList)!=0: 
            x0 , y0 = lmList[4][1:]
            x1 , y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]
            fingers = detector.fingersUp()
            if fingers[1] == 1 and fingers [2] == 0 and fingers[0] == 0:
                cv2.rectangle(img,(frameR,frameR), (Wcam-frameR, Hcam - frameR),
                          (255, 0, 255), 2)
                x3 = np.interp(x1, (frameR, Wcam-frameR), (0, wScr))
                y3 = np.interp(y1, (frameR, Hcam-frameR), (0, hScr))
                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening
                #autopy.mouse.move(wScr - clocX, clocY)
                pyautogui.moveTo(wScr - clocX, clocY)
                cv2.circle(img,(x1, y1), 15, (255, 0, 255), cv2.FILLED)
                plocX, plocY = clocX , clocY
            if fingers[1] == 1 and fingers[2] == 1 and fingers[0] == 0 and fingers[3] == 0 and fingers[4] == 0:
                length, img, lineInfo = detector.findDistance(8, 12, img)
                if length < 35.0:
                    cv2.circle(img,(lineInfo[4], lineInfo[5]),
                           15, (0, 255, 255), cv2.FILLED)
                    autopy.mouse.click()
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img,str(int(fps)), (20,50),cv2.FONT_HERSHEY_PLAIN,3,
        (255,0,0), 3)
        if not success:
            break
        else:
            img =cv2.flip(img,1)
            ret,buffer = cv2.imencode('.jpg',img)
            frame = buffer.tobytes()
        yield(b'--frame\r\n'b'Content-Type:  image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        #return id






flask_app = Flask(__name__)
@flask_app.route("/")
def Home():
    #trend
    pytrends = TrendReq(hl='en-US', tz=360)
    trend = []
    search1 = pytrends.trending_searches(pn='indonesia')
    value_trendID = search1[0].values
    for x in range(4):
        trend.append(value_trendID[x])

    #articl
    url_arr = ['https://cretivox.com/home/author/fadhillah-nurlita/','https://cretivox.com/home/author/anastasiajessica/']
    articl = 0
    for url in url_arr:
        print(url)
        response = requests.get(url) 
        soup = BeautifulSoup(response.text, 'lxml')

        page = soup.find_all('a',{'class':'page-numbers'})
        page = page[len(page)-2]
        # print(page.get_text())

        title = soup.find_all('h2')
        del title[0]
        del title[len(title)-1]

        url1 = url
        for x in range(2,int(page.get_text())+1):
            url_next = str(url1) + "page/" + str(x) + '/'
            # print(url_next)
            response = requests.get(url_next) 
            soup = BeautifulSoup(response.text, 'lxml')
            title_next = soup.find_all('h2')
            #print(title_next)
            del title_next[0]
            del title_next[len(title_next)-1]
            

            for i in range(len(title_next)):
                title.append(title_next[i])
            
        articl = articl + int(len(title))
    
    #ig
    target_profile = ['overongaming','condfe','cretivox']
    igram = []
    for x in target_profile:
        profile = instaloader.Profile.from_username(loader.context, x)
        num_followers = profile.followers
        total_num_likes = 0
        total_num_comments = 0
        total_num_posts = 0
        valueA = []
        truncA = 0
        i = 0
        for post in profile.get_posts():
            total_num_likes += post.likes
            total_num_comments += post.comments
            total_num_posts += 1

            engagement = float(total_num_likes + total_num_comments) / (num_followers * total_num_posts)
            valueA.append(engagement * 100)
            if i == 11:
                truncA = sum(valueA)/12
                data_ig = (
                    ("Username:", profile.full_name),
                    ("Verified?:", profile.is_verified),
                    ("Followers:", profile.followers),
                    ("Media count:", profile.mediacount),
                    ("Engagement rate:", ("%.1f" % truncA) + "%"),
                    ("Avg likes per post:", int(total_num_likes / total_num_posts)),
                    ("Bio:", profile.biography),
                    ("External Url:", profile.external_url)
                )
                break
            i += 1
        a = [data_ig[2][1],data_ig[4][1]]
        igram.append(a)
    
    #tiktok
    out = []
    x = ["cretivox","condfe","overon.gaming"]
    for user in x:
        url = "https://t.tiktok.com/node/share/user/@" + user
        params = {
                "uniqueId": user,
                "validUniqueId": user,
            }
        for key, val in default_params.items():
            params[key] = val
        retval = send_get_request(url=url, params=params)
        print(user, " || " , retval,  " || ", retval['statusCode'])
        if retval['statusCode'] == 10000 :
            out = [['maintenance','maintenance','maintenance'],['maintenance','maintenance','maintenance'],['maintenance','maintenance','maintenance']]
        else:    
            user = retval['userInfo']
            param = {
                    "type": 1,
                    "secUid": "",
                    "id": user['user']['id'],
                    "count": int(retval['userInfo']['stats']['videoCount']),
                    "minCursor": 0,
                    "maxCursor": 0,
                    "shareUid": "",
                    "lang": "",
                    "verifyFp": "",
                    }
            # url = 'https://www.tiktok.com/node/video/feed'
            data = requests.get(url, params=param, headers=headers)
            print("data " , data)
            data = data.json()
            print("data " , data )
            filename = 'user.json'
            with open(filename, 'w') as file_object:  #open the file in write mode
                    json.dump(data, file_object)
            file = open('user.json')
            dataTik = json.load(file)
            Like, Comment, Share, Views, Id, dates = [], [], [], [], [], []
            countdata = len(dataTik['body']['itemListData'])
            # print(countdata)
            if countdata <= 28:
                print("less than 28")
            else:
                for i in range(29):
                    Like.append(dataTik['body']['itemListData'][i]['itemInfos']['diggCount'])
                    Comment.append(dataTik['body']['itemListData'][i]['itemInfos']['commentCount'])
                    Share.append(dataTik['body']['itemListData'][i]['itemInfos']['shareCount'])
                    Views.append(dataTik['body']['itemListData'][i]['itemInfos']['playCount'])
                    Id.append("https://www.tiktok.com/@cretivox/video/" + dataTik['body']['itemListData'][i]['itemInfos']['id'])
                    dates.append(datetime.fromtimestamp(int(dataTik['body']['itemListData'][i]['itemInfos']['createTime'])))
                # print(Like,sum(Like))
                # print(Comment,sum(Comment))
                # print(Share,sum(Share))

                # urlTik = dataTik['body']['itemListData'][0]['authorInfos']['coversLarger']
                # urllib.request.urlretrieve(
                # str(urlTik[0]),
                # "G:/CrevHim/Code/software/instagram/analytics/static/pics/TikTok.jpg")

                # print("Analytics for last " + str(i + 1) + " videos")
                # print("Name : " + str(dataTik['body']['itemListData'][0]['authorInfos']['uniqueId']))
                # print("Bio : " + str(dataTik['body']['itemListData'][0]['authorInfos']['signature']))

                # print("Like : " + str(sum(Like)))
                # print("Comment : " + str(sum(Comment)))
                # print("Share : " + str(sum(Share)))
                # print("Views : " + str(sum(Views)))
                # print("Followers : " + str(dataTik['body']['itemListData'][0]['authorStats']['followerCount']))
                # print("Total Post : " + str(dataTik['body']['itemListData'][0]['authorStats']['videoCount']))
                # print("Total Like : " + str(dataTik['body']['itemListData'][0]['authorStats']['heartCount']))
                # print("evg Likes : " + str(
                #     truncate(sum(Views) / dataTik['body']['itemListData'][0]['authorStats']['videoCount'])) + "%")
                # print("evg Comment : " + str(
                #     truncate(sum(Comment) / dataTik['body']['itemListData'][0]['authorStats']['videoCount'])) + "%")

                # Name = str(dataTik['body']['itemListData'][0]['authorInfos']['uniqueId'])
                # Bio = str(dataTik['body']['itemListData'][0]['authorInfos']['signature'])
                # evglike = str(truncate(sum(Views) / dataTik['body']['itemListData'][0]['authorStats']['videoCount'])) + "%"
                # evgCom = str(truncate(sum(Comment) / dataTik['body']['itemListData'][0]['authorStats']['videoCount'])) + "%"
                # engfol = (sum(Like) + sum(Comment) + sum(Share)) / dataTik['body']['itemListData'][0]['authorStats'][
                    # 'followerCount']
                engfol = ((int(dataTik['body']['itemListData'][0]['authorStats']['heartCount']) / int(dataTik['body']['itemListData'][0]['authorStats']['videoCount'])) / int(dataTik['body']['itemListData'][0]['authorStats']['followerCount'])) * 100
                engview = (((sum(Like) + sum(Comment) + sum(Share))) / sum(Views) ) * 100 
                # Total_post = str(dataTik['body']['itemListData'][0]['authorStats']['videoCount'])
                # Total_Like = str(dataTik['body']['itemListData'][0]['authorStats']['heartCount'])
                Total_followers = str(dataTik['body']['itemListData'][0]['authorStats']['followerCount'])
                # print("engfol : " + str(truncate(engfol)) + "%" + " engview : " + str(truncate(engview)) + "%")
                showdata = [Total_followers, str(truncate(engfol)) + "%", str(truncate(engview)) + "%"]
                out.append(showdata)
    # print(out)
    return render_template("index.html",
                    trend1 = trend[0],
                    trend2 = trend[1],
                    trend3 = trend[2],
                    trend4 = trend[3],
                    ogs1 = igram[0][0],
                    ogs2 = igram[0][1],
                    condfe1 = igram[1][0],
                    condfe2 = igram[1][1],
                    cvox1 = igram[2][0],
                    cvox2 = igram[2][1],
                    # tgs1 = igram[3][0],
                    # tgs2 = igram[3][1],
                    voxTik1 = out[0][0],
                    voxTik2 = out[0][1],
                    voxTik3 = out[0][2],
                    cnfTik1 = out[1][0],
                    cnfTik2 = out[1][1],
                    cnfTik3 = out[1][2],
                    ogsTik1 = out[2][0],
                    ogsTik2 = out[2][1],
                    ogsTik3 = out[2][2],
                    total = articl)

#camera
@flask_app.route('/video')
def video(): 
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    flask_app.run(debug=True)