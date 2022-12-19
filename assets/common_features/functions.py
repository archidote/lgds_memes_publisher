from assets.controller import * 
from assets.bot_actions.bot_rewteet import *
def check_file_extension (path) : 
    
    response = requests.get(path)
    content_type = response.headers['content-type']
    extension = mimetypes.guess_extension(content_type)
    return extension

def iterate_over_a_the_first_case_of_a_double_list(_list) :
    
    _return = ""
    
    for l in _list: 
        if l[0] == "/hello" : 
            break
        _return += ""+l[0]+"\n"
        
    return _return
    
def every_1st_day_of_the_month_or_not():
    
    day_of_month = datetime.now().day
    
    if (day_of_month == 1) :
        most_retweeted_tweet_of_the_previous_month()
    elif (day_of_month == 2) :
        print 
        # most_fav_tweet_of_the_previous_month()
    else : 
        logging.info("Today we are not the first day of the month ("+str(day_of_month)+"), so actions planned for 1st day will not be executed.")
