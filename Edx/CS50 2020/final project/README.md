# Bilibili Danmu Collection
#### Video Demo:  
***
https://www.bilibili.com/video/BV19Z4y1D7rZ?spm_id_from=333.999.0.0
#### Description: 
***
Bilibili is a video website characterized by bullet screen, so called Danmu, which is really popular among young generation in mainland China. In Bilibili Danmu Collection project, by submitting video link, users can view the latest Danmu, the most sent Danmu, or search Danmu of the video. The website will record history of submitted videos.
#### Introduction to file
***
In `/`, four files are `app.py`, `crawl.py`,`helper.py`,`project.db`.
- `app.py`: In `app.py`, website features are achieved by modules such as `Flask`, `Session`, `werkzeug` and so on. And incomprehensible code will be explained.

```
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
```
`generate_password_hash()` can help generate hash string given by password string. And ` check_password_hash()` can help match hash string with password string.
```
if not re.match(r'^https?:/{2}\w.+$', vlink):
    return apology("invalid https link", 403)
```
In `@app.route("/")`,  using `re`, regular expression, to match `htttps://` to video link.
```
# Remember which user has logged in, xml, and title
session["user_id"] = users["id"]
session["xml"] = ''
session["title"] = ''
```
After user logs in, session can store user's id, and xml, title that will be inputted later on.
```
session.clear()
```
In `@app.route("/logout")`, `session.clear()` will clear stored `user_id`, `xml`, and `title`.
```
# When input both danmu and bilibili id to search
if danmu and bid:
  danmus = db.execute("SELECT * FROM danmus WHERE xml = ? AND user_id = ? AND danmu LIKE '%"+danmu+"%' LIMIT 20", session["xml"], bid)
```
In `@app.route("/search")`, using `danmu LIKE '%"+danmu+"%'` can match all the Danmu including inserted `danmu`. 

- `helpers.py`: `helper.py` contains `apology()` and `login_required()` function.  `apology()` is used for reporting error messages with error code. `login_required()` allowes only login users to visit designated website pages.

- `crawl.py`: `crawl.py` is used for Danmu collection of one video and inserting Danmu information into `project.db`. Some code need explaination here.
```
cid_list = re.findall(r'"cid":(.*?),', res.text)
cid = cid_list[0]
url = f'https://comment.bilibili.com/{cid}.xml'
```
Bilibili stores danmu in address like `https://comment.bilibili.com/{cid}.xml`, and cid is identifier for each Danmu xml file. First, we can search and collect list of cid. The first argument is cid of the video, and the rest includes cids of recommended videos. The details about cid list will be explained at the end.

```
seconds, fractions = startTime.split('.')
seconds = int(seconds)
if seconds < 3600:
   m, s = divmod(seconds, 60)
   startTime = "%02d:%02d" % (m, s)
else:
   m, s = divmod(seconds, 60)
   h, m = divmod(m, 60)
   startTime = "%d:%02d:%02d" % (h, m, s)
```
Most of videos in Bilibili will not exceed 1 hour, but we can not ignore them when converting seconds to mins or hours by `divmod()` function. And "startTime" in Danmu xml file is represented in float, fractions can be ignored.

```
# Convert date in seconds to otherStyleDate
timeStamp = date + 28800
timeArray = time.localtime(timeStamp)
otherStyleDate = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
```
The date of Danmu sent by all Bilibili users is recorded in seconds. By adding Jan 1st 1970 00:00:00, date can be obained. Especially, add 28800s (8 hours) when representing local time in China.

```
danmu_count = {}
 if danmu in danmu_count.keys():
     danmu_count[danmu] += 1
 else:
     danmu_count[danmu] = 1
```
Count danmu and store them in a dictionary.

- `project.db`
Database contains four tabels: 
`counts  danmus  users  xmls`
```
CREATE TABLE counts (xml TEXT NOT NULL, danmu TEXT NOT NULL, count INTEGER NOT NULL);
CREATE TABLE danmus (xml TEXT NOT NULL, danmu TEXT NOT NULL, time TEXT NOT NULL, date TEXT NOT NULL, user_id TEXT NOT NULL);
CREATE TABLE users (id INTEGER, username TEXT NOT NULL, hash TEXT NOT NULL, PRIMARY KEY(id));
CREATE UNIQUE INDEX username ON users (username);
CREATE TABLE xmls (id INTEGER, xml TEXT NOT NULL, title TEXT NOT NULL, session INTEGER NOT NULL, PRIMARY KEY(id));
CREATE UNIQUE INDEX id ON xmls (id);
```

In `/templates`, function of each html is listed as the following: 
`login.html`: In Login page, has two texts input for username and password, and one submit button. 

`apology.html`: If user does not provide valid username or password when click "Submit". An apology page will show up, report corresponding error messages and error code. 

`register.html`: Before login, user must register by inputing username, password, and confirmation. If one of three requirements is invalid, similar as above, apology page will show up. 

`index.html`: After login, home page will be shown. User can submit video link to collect Danmu. If user's input is not a "https://" link or "bilibili video" link, apology page will show up with corresponding error messages and error code.

`latest.html`: Click on "Latest",  the 20 latest Danmu will be displayed with their startTime, Date and Bilibili UserID.

`most.html`: Click on "Most", the 20 sent most Danmu will be displayed with their Count which represents sent times.

`search.html`: Click on "Search": a search form will be shown, users can input Danmu or Bilibili ID, or both to search bullet screen in the video.

`history.html`: Click on "history": it will show all the video titles searched by the user.

`changepwd.html`: After logout, the last feature is "Change Password", users can change passwords if needed.

In `/static`, `style.css` designs style of the website.

#### Future work: 
***
As mentioned above, the first cid in `cid_list` cannot reprensent all Danmu files of one video. Especially for some popular videos which have mutiple xml files to store Danmu information. Future work could be collecting all Danmu of one video.
Future work could also be collecting danmu by title or user's history etc.

#### Reference: 
***
[Problem Set 9: Finance](https://cs50.harvard.edu/x/2021/psets/9/finance/)
