#!/bin/bash 
if  [  -s ./my.sh.log ] ; then
FROM_EMAIL="123456@qq.com" # 发送
TO_EMAIL="123456@qq.com" # 收件
LOG=./my.sh.log     # 日志路径

echo -e "`date "+%Y-%m-%d %H:%M:%S"` : Please to check the fail log." | mail \
-r "From: alertAdmin <${FROM_EMAIL}>" \
-a ${LOG} \
-s "error" ${TO_EMAIL}
fi