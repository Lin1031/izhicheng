#!/bin/bash
. /etc/profile
. ~/.bash_profile
while read xh sheng shi qu
do
    /usr/bin/python3 /root/tianbiaos.py $xh $sheng $shi $qu
done < snos.txt