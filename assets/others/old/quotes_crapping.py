# from bs4 import BeautifulSoup
# import requests

# response = requests.get("https://www.commentcoder.com/citations-informatique/")
# soup = BeautifulSoup(response.text, 'html.parser')


# rows = soup.findAll('ol')


# for row in rows :
#     for subrow in row.findAll('li') :
#         quote = subrow.text.replace("(source)", " source : ")
#         for subsubrow in subrow.findAll('a',href=True): 
#             print (quote,", "+subsubrow["href"])
            
            
