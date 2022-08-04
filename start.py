import threading
import schedule
import time
from controller import * 
from meme_publisher import * 
from quote_publisher import * 
from threading import Thread
from reply import detect_twitter_mention

# schedule.every().day.at("07:30").do(lambda: img_publisher())
# schedule.every().day.at("18:00").do(lambda: quote_publisher())

schedule.every(1).minutes.do(lambda: meme_publisher())
schedule.every(2).minutes.do(lambda: quote_publisher())

def send_img_or_quote_auto() : 
    while 1:
        schedule.run_pending()
        time.sleep(1)

x = threading.Thread(target=detect_twitter_mention)
x.start()

y = threading.Thread(target=send_img_or_quote_auto)
y.start()


