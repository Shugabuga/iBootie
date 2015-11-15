# iBootie
The basis of the Tech Support bot /u/iBootie on /r/jailbreak

##Setting Up the Bot
This guide assumes you have **Linux**, but you can still use this script on Mac OS X or Windows

1) Download this project, using Git or otherwise.

2) Create a new Reddit account for your bot and earn more than 10 Link Karma. **Directly asking for Karma is against Reddit rules**, so just post something intresting on /r/FreeKarma, such as a picture of Vault-Boy.

3) Run this in Terminal: `sudo apt-get install python && sudo apt-get install python-pip && pip install praw`. It will install everthing you need. If you are prompted to put in your password, do so.

4) Replace the text in 'singlequotes' to edit your settings, such as subreddits to run in, message to search for, and message to be replied.

5) Run `sudo crontab -e` in Terminal

6) Add this on a seperate line: `* * * * * cd /iBootie && python bot.py`. Replace "iBootie" to where you have your bot.py file. 

7) Keep your computer running, and your bot will check for new posts every minute!

##License
This code is free-to-use, but the code is provided as-is without warantee.
