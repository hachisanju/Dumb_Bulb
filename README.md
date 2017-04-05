# TP-Link Smart Bulb Controller for Python

This is a controller to turn on and off TP-Link Smart Bulbs, specifically the LB-120. It's based on Lubomir Stroetmann's work [here](https://github.com/softScheck/tplink-smartplug). 

If you're interested in the full article, that's also here: [Reverse Engineering the TP-Link HS110](https://www.softscheck.com/en/reverse-engineering-tp-link-hs110/)

I won't get elaborate with the usage. It's the same as the tplink-smartplug.py program.
Invoke like this:

`./tplink-smartbulb.py -t <ip> [-c <cmd> || -j <json>]`

The available commands are on, off and info. Anything else you'll have to send as JSON. If you want more in depth commands just go visit Lubomir's github, seriously. It's a good resource.
