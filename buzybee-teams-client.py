#!/usr/bin/python3

import configparser
import json
import urllib.request
import urllib.parse

config = configparser.ConfigParser()
config.read('buzybee-teams.ini')

teams_presence_url = 'https://graph.microsoft.com/v1.0/me/presence'

teams_presence_req = urllib.request.Request(teams_presence_url, None,
        {"Authorization": f"Bearer {config['teams']['bearer-token']}"})
teams_presence = json.load(urllib.request.urlopen(teams_presence_req))

status_mapping = {
	"Available": 'available',
	"AvailableIdle": 'available',
	"Away": 'away',
	"BeRightBack": 'away',
	"Busy": 'busy',
	"BusyIdle": 'busy',
	"DoNotDisturb": 'busy',
	"Offline": 'unknown',
	"PresenceUnknown": 'unknown'
}

new_status = status_mapping[teams_presence['availability']]
status_post_data = urllib.parse.urlencode({"status": new_status})

status_update_req = urllib.request.Request(config['buzybee']['status-url'],
	data=str.encode(status_post_data), method='POST')
urllib.request.urlopen(status_update_req)

