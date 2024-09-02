from pypresence import Presence
import time
import sys
import random
import datetime
import rpyc
import json
import os

client_id = '1278718443113414717'
RPC = Presence(client_id)
RPC.connect()



epoch = int(time.time())
nine_am_today = datetime.datetime.now()
epoch_nine_am_today = int(nine_am_today.timestamp())

while True:
    try:
        script_path = os.path.dirname(os.path.abspath(__file__))
        types_file = os.path.join(script_path, 'types.json')

        with open(types_file) as f:
            types = json.load(f)

        c = rpyc.classic.connect("localhost", 9900)
        hou = c.modules.hou
        activity_name = "Tweaking parameters"
        activity_type = "sop"
        activity_icon = "hou_icon"
        try:
            node = hou.selectedItems()[0] or None
            node_name = node.type().name()
        except:
            node_name = "Idling"

        for t in types:
            if t in node_name.lower():
                print(t)
                activity_type = t
                activity_name = types[activity_type]["prompt"]
                activity_icon = types[activity_type]["icon"]
                break

        RPC.update(details=activity_name, large_image=activity_icon, start=epoch_nine_am_today) # Set the presence
        time.sleep(15)
    except Exception as e:
        print(e)
        exit()
