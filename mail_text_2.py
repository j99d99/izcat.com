#!/usr/bin/env python
#coding:utf-8

#此脚本用于发送纯文本内容的邮件

import smtplib,sys,os
import string


if len(sys.argv)>3:
	FROM=sys.argv[1]
	TO=sys.argv[2]
	PASSWORD=sys.argv[3]
else:
	print "USAGE:python sys.argv[0] FROM TO　PASSEORD"
	os.sys.exit()

HOST="smtp.163.com"
#FROM="j99e99@163.com"
#TO="704952527@qq.com"
SUBJECT="This is a test mail"
image="just test"

msg=string.join((
"From: %s" % FROM,
"To: %s" % TO,
"Subject: %s" % SUBJECT,
"",
image
),"\r\n")


def sendmail(FROM,TO,PASSWORD):
	smtp=smtplib.SMTP()
	smtp.connect(HOST,25)
	smtp.login(FROM,PASSWORD)
	smtp.sendmail(FROM,TO,msg)
	smtp.close()

sendmail(FROM,TO,PASSWORD)
