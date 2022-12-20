from assets.controller import * 
from assets.bot_actions.most_famous_tweet import *
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
        logging.info("First day of the month - Calling most_famous_tweet_of_the_previous_month(\"favorite\")...")
        most_famous_tweet_of_the_previous_month("favorite")    
    elif (day_of_month == 2) :
        logging.info("First day of the month - Calling most_famous_tweet_of_the_previous_month(\"retweet\")...")
        most_famous_tweet_of_the_previous_month("retweet")
    else : 
        logging.info("Today we are not the 1st || 2st day of the month ("+str(day_of_month)+"), so no scheduled actions will be executed.")
