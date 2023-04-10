#!/bin/bash
curl -u "x:$(cat /home/pi/sg/pmsd001/.token)" http://splunk.home:8088/services/collector/event -d "$(python3 /home/pi/sg/pmsd001/getdata.py)" | grep Success || python3 /home/pi/sg/pmsd001/getdata.py > /home/pi/sg/pmsd001/backfill/$(date +"%Y%m%dT_%H%M%S").json
