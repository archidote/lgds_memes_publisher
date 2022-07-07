import praw
r = praw.Reddit(client_id='',
                client_secret='',
                user_agent='Linux')

page = r.subreddit('ProgrammerHumor')
top_posts = page.hot(limit=None)
for post in top_posts:
    print(post.url)
