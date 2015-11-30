#!/usr/bin/env python
#coding:utf-8

#此脚本用于发送纯文本内容的邮件

import smtplib
import string

HOST="smtp.163.com"
FROM="j99e99@163.com"
TO="704952527@qq.com"
PASSWORD="xxxxx"
SUBJECT="This is a test mail"
image="just test"

msg=string.join((
"From: %s" % FROM,
"To: %s" % TO,
"Subject: %s" % SUBJECT,
"",
image
),"\r\n")

smtp=smtplib.SMTP()
smtp.connect(HOST,25)
smtp.login(FROM,PASSWORD)
smtp.sendmail(FROM,TO,msg)
smtp.close()
