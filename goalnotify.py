import pynotify
import urllib2
from bs4 import BeautifulSoup
import urllib2
import os

URL=raw_input("Paste the URL of the match: ")
try:
    response=urllib2.urlopen(URL)
    html=response.read()
except urllib2.HTTPError, e:
    print 'HTTP Error, '+e.code
    quit()
except urllib2.URLError, e:
    print 'URL Error '+e.args
    quit()

soup=BeautifulSoup(html)

HomeTeam=soup.find('div',attrs={'class':'home'})
HomeTeamName=HomeTeam.find('h2').text

AwayTeam=soup.find('div',attrs={'class':'away'})
AwayTeamName=AwayTeam.find('h2').text

Initial_Home_Score='-1'
Initial_Away_Score='-1'

title = str(HomeTeamName)+' Vs '+str(AwayTeamName)

icon  = "/usr/share/icons/Humanity/emblems/32/emblem-ohno.png"

while (True):
	response=urllib2.urlopen(URL)
	soup=BeautifulSoup(response)
	
	Home_Score=soup.find('div',attrs={'class':'home-score'}).text
	Away_Score=soup.find('div',attrs={'class':'away-score'}).text
	
	if(int(Home_Score)!=int(Initial_Home_Score)) or(int(Away_Score) != int(Initial_Away_Score)):
		text  = str(Home_Score )+' - '+str(Away_Score)
		pynotify.init('Score Updates')
		notification = pynotify.Notification(title, text, icon)
		notification.set_urgency(pynotify.URGENCY_NORMAL)
		os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 0.5, 3000))
		notification.show()
		Initial_Away_Score=Away_Score
		Initial_Home_Score=Home_Score
