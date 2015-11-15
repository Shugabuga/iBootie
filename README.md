# iBootie
The basis of the Tech Support bot /u/iBootie on /r/jailbreak

##Setting Up the Bot
iBootie is a simple bot in regards to configuration!

1) Create a new Reddit account for your bot and earn more than 10 Link Karma. **Directly asking for Karma is against Reddit rules**, so just post something intresting on /r/FreeKarma, such as a picture of Vault-Boy.

2) Run this in Terminal: `sudo apt-get install python && sudo apt-get install python-pip && pip install praw`. It will install everthing you need. If you are prompted to put in your password, do so.

3) Replace the text in 'singlequotes' to edit your settings, such as subreddits to run in, message to search for, and message to be replied.

4) Run `sudo crontab -e` in Terminal

5) Add this on a seperate line: `* * * * * cd /iBootie && python bot.py`. Replace "iBootie" to where you have your bot.py file. 

6) Keep your computer running, and your bot will check for new posts every minute!

##License
This code is free-to-use, but the code is provided as-is without warantee.
