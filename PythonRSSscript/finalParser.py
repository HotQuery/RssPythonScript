import feedparser
import datetime
from time import localtime



feed1 = feedparser.parse('https://www.reddit.com/r/science/.rss')
feed2 = feedparser.parse('https://www.reddit.com/r/Minecraft/.rss')
today = datetime.datetime.now()
 
print(feed1.feed.title)
print("is the science feed")
print(today)
print("is todays date")
print(feed1['feed']['updated'])
print("is when this feed was last updated")

print(feed2.feed.title)
print("is the minecraft feed")
print(today)
print("is todays date")
print(feed2['feed']['updated'])
print("is when this feed was last updated")

now = localtime()
#print(now[0],now[1],now[2]) # the current YEAR MONTH DAY

pub_today = 0
for entry in feed1['entries']:
  #print(entry.published_parsed[0],entry.published_parsed[1],entry.published_parsed[2]) # print entry YEAR MONTH DAY for debugging
  if (entry.updated[0],entry.updated[1],entry.updated[2]) == (now[0],now[1],now[2]):
    pub_today += 1


#print("There were %d entries published today!" % pub_today)

#the line below will print the title in r/science
#for entry in feed1['entries']:
    #print(entry.title)
    #print(entry.updated)
    #timeStore = entry.updated

feedTitle1 = feed1.feed.title
print("the number of posts on %s is " %feedTitle1)
print(len(feed1['entries']))

feedTitle2 = feed2.feed.title
print("the number posts on %s  is " %feedTitle2)
print(len(feed2['entries']))

if (len(feed1['entries'])) > (len(feed2['entries'])):
  print("There were more posts on %s" %feedTitle1)
else:
  print("There were more posts on %s today" %feedTitle2)


  
    
