# UbuntuGoalNotification
Fetches score updates from goal.com and displays notification when score updates.

Usages: python goalnotify.py

Needs Beautiful Soup and pynotify to run, if not already installed:

apt-get install python-bs4
or
easy_install beautifulsoup4

sudo apt-get install python-notify

For getting sms notifications, run the goalnotify_smsnotification.py file by using the command 

python goalnotify_smsnotification.py

for the FREE SMS notifications to work twilio moodule is required.To install twilio module type the following commands:

pip install twilio

or 

easy_install twilio

Signup at https://www.twilio.com/try-twilio
Verify your mobile number
Get your SID and AUTH_TOKEN from https://www.twilio.com/user/account/settings
Get your twilio Number from https://www.twilio.com/user/account/phone-numbers/incoming


![alt tag](https://raw.githubusercontent.com/williamanaryan/UbuntuGoalNotification/master/Screenshot.png)
![alt tag](https://github.com/williamanaryan/UbuntuGoalNotification/blob/master/sms.png)
