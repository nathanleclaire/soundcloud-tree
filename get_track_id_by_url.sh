#!/bin/bash

URL_USE_HTTP=`echo $1 | sed 's/https/http/g'`
SONGID=`curl -s $URL_USE_HTTP | egrep -o 'data-sc-track="[0-9]+"' | head -n 1 | egrep -o '[0-9]+'`
echo $SONGID
