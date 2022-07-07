from controller import * 
from meme_publisher import * 
from quote_publisher import * 

schedule.every(20).seconds.do(lambda: meme_publisher())
schedule.every(30).seconds.do(lambda: quote_publisher())

while 1:
    schedule.run_pending()
    time.sleep(1)