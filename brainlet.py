import requests, os, time, configparser
from termcolor import colored

os.system("title" + " Brainlet BETA - maki")
thisfolder = os.path.dirname(os.path.realpath(__file__))
cfgfile = os.path.join(thisfolder, 'Config.cfg')
#Change title and config file stuff

config = configparser.RawConfigParser() 
config.read(cfgfile)
noc = 0
colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
true = 'true'

subject = input('Enter subject:' + '\n')
prehtml = config.get('Config', 'Content')
delay = int(config.get('Config', 'Delay'))
img = config.get('Config', 'Attachment')
debug = int(config.get('Config', 'DebugMode'))
token = config.get('Config', 'Token')
scookie = config.get('Config', 'SCookie')
wallid = int(input('Enter the Wall ID (1 for cfg wallid):' + '\n'))

#Dumb variable stuff

if wallid == 1:
	wallid = config.get('Config', 'WallID') 

if prehtml.endswith('.txt'):
	f = open(prehtml, 'r')
	prehtml = f.read()
	f.close()
else:
	prehtml = input('Enter content:' + '\n')

content = '<div>{}</div>'.format(prehtml)

cookies = {'cookie': scookie}
url = 'https://padlet.com/api/3/wishes'
myobj = {
    "attachment": img,
    "author": {
        "avatar": "https://padlet.net/avatars/alien1.png",
        "quota": {
            "can_make": true,
            "walls_limit": 0,
            "walls_used": 0
        },
    },
    "body": content,
    "subject": subject,
    "wall_id": wallid,
    "width": 1000
}

headers = {
	'x-csrf-token': token


}

os.system('cls')

while null == 'null':
	if noc >= 6:
		noc = 0 
	x = requests.post(url, data = myobj, cookies = cookies, headers=headers)
	if debug == 1:
		print(x.text)
	else:
		print(colored('Made a new post!', colors[noc], attrs=['bold']))
	time.sleep(delay)
	noc += 1
#Post loop