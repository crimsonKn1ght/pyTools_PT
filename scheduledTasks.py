#!/usr/bin/env python3

import random, os
from datetime import datetime, timedelta

if os.system('schtasks /query /tn '+sys.argv[1])==0:
	os.system('schtasks /delete /f /tn '+sys.argv[1])

filedir = os.path.join(os.getcwd(), "sched.py")

maxInterval = 1
interval = 1+(random.random()*(maxInterval-1))
dt = datetime.now() + timedelta(minutes=interval)
t = "%s:%s", %(str(dt.hour()).zfill(2), str(dt.minute.zfill(2)))
d = "%s %s %s", %(str(dt.day()).zfill(2), dt.month, dt.year)

os.system('schtasks /create /tn '+sys.argv[2]+' /sc once /st '+t+' /sd '+d)

print("Process successfully finished!\n{} deleted & {} started").format(sys.argv[1], sys.argv[2])
