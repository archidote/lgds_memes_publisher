from assets.controller import * 
from assets.publisher.meme_publisher import * 
from assets.publisher.quote_publisher import * 
from assets.bot_actions.retweet import * 
from assets.bot_actions.reply import *

################################################################## Scheduler ###############################################################


schedule.every().days.at("07:00").do(lambda: meme_source_and_publish())
schedule.every().days.at("17:45").do(lambda: every_x_day_of_the_month_or_not())
schedule.every(2).days.at("18:15").do(lambda: bot_retweet())
schedule.every(2).days.at("18:00").do(lambda: quote_publisher())
schedule.every(60).seconds.do(lambda: detect_twitter_mention())

# schedule.every(5).seconds.do(lambda: meme_source_and_publish())
# schedule.every(5).seconds.do(lambda: quote_publisher())
# schedule.every(5).seconds.do(lambda: detect_twitter_mention())

################################################################## Main ###############################################################

if __name__ == "__main__":
    try:
        while 1:
            schedule.run_pending()
            time.sleep(1)
            signal.signal(signal.SIGINT, detect_control_c_signal_handler)
    except (RuntimeError, TypeError, NameError, Exception) as e :
        logging.error("Fatal error : "+e+"")    
    