from assets.controller import * 
from assets.publisher.meme_publisher import * 
from assets.publisher.quote_publisher import * 
from assets.bot_actions.retweet import * 
from assets.bot_actions.reply import *

################################################################## Scheduler ###############################################################


schedule.every().days.at("07:00").do(lambda: meme_source_and_publish())
schedule.every().days.at("17:30").do(lambda: every_1st_day_of_the_month_or_not())
schedule.every(2).days.at("18:00").do(lambda: quote_publisher())
schedule.every(15).to(59).seconds.do(lambda: detect_twitter_mention())
schedule.every(12).hours.do(lambda: bot_retweet())

# schedule.every(5).seconds.do(lambda: meme_source_and_publish())
# schedule.every(5).seconds.do(lambda: quote_publisher())
# schedule.every(5).seconds.do(lambda: detect_twitter_mention())

def start() : 
    logging.info("The bot is starting...")   
    while 1:
        schedule.run_pending()
        time.sleep(1)
        
################################################################## Main ###############################################################

if __name__ == "__main__":
    try:
        start()
    except Exception as e :
        logging.error('Fatal error : '+str(e)+"")
    
    