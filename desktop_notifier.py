# Python program to illustrate 
# desktop news notifier 
import feedparser 
from topnews import topStories 
import notify2 
import os 
import time 
def parseFeed(): 
	f = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
	ICON_PATH = os.getcwd() + "/icon.ico"
	notify2.init('News Notify')
	for newsitem in f['items']: 
		n = notify2.Notification(newsitem['title'], 
								newsitem['summary'], 
								icon=ICON_PATH 
								) 
	n.set_urgency(notify2.URGENCY_NORMAL) 
	n.show() 
	n.set_timeout(15000) 
	time.sleep(5)


def get_topStories():
    # path to notification window icon 
    ICON_PATH = os.getcwd() + "/icon.ico"

    # fetch news items 
    newsitems = topStories() 

    # initialise the d-bus connection 
    notify2.init("News Notifier") 

    # create Notification object 
    n = notify2.Notification(newsitems, icon = ICON_PATH) 

    # set urgency level 
    n.set_urgency(notify2.URGENCY_NORMAL) 

    # set timeout for a notification 
    n.set_timeout(10000) 

    for newsitem in newsitems: 

        # update notification data for Notification object 
        n.update(newsitem['title'], newsitem['description']) 

        # show notification on screen 
        n.show() 

        # short delay between notifications 
        time.sleep(15) 


def run():
    print("First: ")
    parseFeed()
    print("Second: ")
    get_topStories()

if __name__ == '__main__': 
	run()
