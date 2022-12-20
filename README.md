# Python3 twitter bot 

## Small prerequisites : 

```
sudo apt update 
sudo apt-get install python3-venv python3-bs4
```
## Initialize the project 

```
git clone https://github.com/archidote/twitter_bot_lgds.git
cd twitter_bot_lgds
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```
add credentails into a .env file : 
```
nano .env
```

```
consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""
```
then, you canstart the bot : 
```
python3 twitter_bot_lgds.py
```