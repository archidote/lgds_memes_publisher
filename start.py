import schedule
import time
from assets.controller import * 
from assets.meme_publisher import * 
from assets.quote_publisher import * 
from assets.bot_rewteet import * 
from assets.bot_reply import detect_twitter_mention


schedule.every().days.at("07:30").do(lambda: meme_source_selectore_and_publish())
schedule.every(2).days.at("18:00").do(lambda: quote_publisher())
schedule.every(15).seconds.do(lambda: detect_twitter_mention())
schedule.every(12).hours.do(lambda: bot_retweet())

# schedule.every(5).seconds.do(lambda: meme_source_selectore_and_publish())
# schedule.every(5).seconds.do(lambda: quote_publisher())
# schedule.every(5).seconds.do(lambda: detect_twitter_mention())
# schedule.every(twitter_api_random_fetch_in_secondes).seconds.do(lambda: detect_twitter_mention())

def start() : 
    while 1:
        schedule.run_pending()
        time.sleep(1)
        
# ################################################################# Main ###############################################################

if __name__ == "__main__":
    start()




