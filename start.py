import threading
import schedule
import time
from controller import * 
from meme_publisher import * 
from quote_publisher import * 
from bot_reply import detect_twitter_mention

# schedule.every().days.at("07:30").do(lambda: meme_source_selectore_and_publish())
# schedule.every(2).days.at("18:00").do(lambda: quote_publisher())

schedule.every(1).minutes.do(lambda: meme_source_selectore_and_publish())
schedule.every(2).minutes.do(lambda: quote_publisher())

def send_img_or_quote_auto() : 
    while 1:
        schedule.run_pending()
        time.sleep(1)
        
schedule.every(30).seconds.do(lambda: detect_twitter_mention())

def twitter_bot_fetch_new_mentions() :
    while 1:
        schedule.run_pending()
        time.sleep(1)

x = threading.Thread(target=detect_twitter_mention)
x.start()

y = threading.Thread(target=send_img_or_quote_auto)
y.start()
