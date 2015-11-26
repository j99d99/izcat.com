#!/usr/bin/env python
#_*_coding:utf-8_*_
import os
import sys
import psutil
def cpuinfo():
	cpu_all=psutil.cpu_times_percent()
	cpu_idle=cpu_all.idle
	print cpu_all
	cpu_system=cpu_all.system
	cpu_iowait=cpu_all.iowait
	cpu_infomation="cpu.idle: %6s\ncpu.system: %6s\ncpu.iowait: %6s\n" % (cpu_idle,cpu_system,cpu_iowait)
	return cpu_infomation
def diskinfo():
	disk_par=psutil.disk_partitions()
	info={}
	for u in disk_par:
		info1=[]
		disk_part=u.mountpoint 
		info1.append(psutil.disk_usage(disk_part).total)
		info1.append(psutil.disk_usage(disk_part).used)
		info1.append(psutil.disk_usage(disk_part).free)
		info[disk_part]=info1
	return info
p=cpuinfo()
f=diskinfo()
print p
print "分区\tdisk_total\tdisk_used\tdisk_free"
for k ,v in f.items():
	for i in v:
		k=k+"\t"+str(i/1024/1024)+"M"
	print k
