# BuzyBee Teams: Microsoft Teams client for the BuzyBee office status indicator

This is a real quick and dirty way to build a status indicator using stuff I
had laying around.

## Setup

1. Copy `buzybee-teams.ini.sample` to `buzybee-teams.ini`
2. Edit `buzybee-teams.ini`, and set a Bearer token (as you can get from
   [Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer)),
   and the URL of your [BuzyBee](https://github.com/pioto/buzybee)
   server.
3. Run the script periodically via cron, e.g.:

```
# Update my status indicator
* * * * * cd ~/git/buzybee-teams ; python3 buzybee-teams-client.py
```
