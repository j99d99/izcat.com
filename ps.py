#!/usr/bin/env python
#_*_coding:utf-8_*_
import os
import sys
import psutil
def cpuinfo():
	cpu_all=psutil.cpu_times_percent(interval=3)
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
def meminfo():
	mem_info=psutil.virtual_memory()
	mem_total=mem_info.total/1024/1024
	mem_used=mem_info.used/1024/1024
	mem_free=mem_info.free/1024/1024
	mem_images="The memory images is:\nmem_total:%6sM\tmem_used:%6sM\tmem_free:%6sM\n" % (mem_total,mem_used,mem_free)
	return mem_images
p=cpuinfo()
f=diskinfo()
m=meminfo()
print p
print "分区\tdisk_total\tdisk_used\tdisk_free"
for k ,v in f.items():
	for i in v:
		k=k+"\t"+str(i/1024/1024)+"M"
	print k
print m
