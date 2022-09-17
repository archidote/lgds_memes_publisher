from assets.controller import * 
schedule.every(5).to(10).seconds.do(lambda: print("hello"))

def start() : 
    while 1:
        schedule.run_pending()
        time.sleep(1)
        
start()