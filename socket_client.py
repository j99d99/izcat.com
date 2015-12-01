#!/usr/bin/env python
#coding:utf-8

import socket
import sys

host,port="127.0.0.1",18000
socket_cli=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_cli.connect((host,port))
socket_cli.send("up")
socket_cli.close()
