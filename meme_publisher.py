from select_image import * 
from controller import * 


def meme_publisher():
    
    sorted_index_of_by_file_ext()

    media = api.media_upload("tmp_local_meme.jpg")

    tweet = "Bonne journée 😀 #picoftheday"
    api.update_status(status=tweet, media_ids=[media.media_id])


schedule.every(1).minutes.do(lambda: meme_publisher())
while 1:
    schedule.run_pending()
    time.sleep(1)