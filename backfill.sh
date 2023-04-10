#!/bin/bash
for i in $(find /home/pi/sg/pmsd001/backfill -name '*.json'); do curl -u "x:$(cat /home/pi/sg/pmsd001/.token)" http://splunk.home:8088/services/collector/event -d "$(cat $i)" | grep Success && rm $i; done;
