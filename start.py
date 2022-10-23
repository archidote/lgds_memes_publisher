from assets.controller import * 
from assets.publisher.meme_publisher import * 
from assets.publisher.quote_publisher import * 
from assets.bot_actions.bot_rewteet import * 
from assets.bot_actions.bot_reply import *


schedule.every().days.at("07:00").do(lambda: meme_source_and_publish())
schedule.every(2).days.at("18:00").do(lambda: quote_publisher())
schedule.every(15).to(59).seconds.do(lambda: detect_twitter_mention())
schedule.every(12).hours.do(lambda: bot_retweet())

# schedule.every(5).seconds.do(lambda: meme_source_and_publish())
# schedule.every(5).seconds.do(lambda: quote_publisher())
# schedule.every(5).seconds.do(lambda: detect_twitter_mention())

def start() : 
    while 1:
        schedule.run_pending()
        time.sleep(1)
        
# def end() :
#     tweet = "🔨 Maintenance du bot en cours... Je reviens vite 🤖"
#     api.update_status(status=tweet)
# ################################################################# Main ###############################################################

if __name__ == "__main__":
    start()