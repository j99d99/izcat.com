#!/usr/bin/env python
#coding:utf-8

#脚本功能:
#commpare函数:比较两个文件夹dir1和dir2中存在于dir1和不同的文件,如果存在子目录,则继续遍历子目录文件,最后返回一个包括文件和子目录绝对路径的列表,left_llist表示dir1的文件及目录列表,diff_files表示两个目录不匹配的文件
#main函数：
	#首先判断是否正确输入了dir1和dir2
	#调用commpare生成dir1的文件及目录和不匹配文件的列表
	#将commpare生成的列表的绝对路径换成dir2觉得路径并生成一个新数组
	#判断列表现是否为目录,如果是目录且不存在则建立，并status标记建立成功
	#子目录建立成功后重新比较两个目录
	#复制文件


import filecmp,os,re,sys,shutil
dir1="/root/izcat.com/test1"
dir2="/root/izcat.com/test2"
L=[]

def commpare(dir1,dir2):
	list=filecmp.dircmp(dir1,dir2)
	only_test1=list.left_list
	only_test2=list.right_list
	diff_test=list.diff_files
	[L.append(os.path.abspath(os.path.join(dir1,x))) for x in only_test1]
	[L.append(os.path.abspath(os.path.join(dir1,x))) for x in diff_test]
	if len(list.common_dirs) > 0:
		for items in list.common_dirs:
			commpare(os.path.abspath(os.path.join(dir1,items)),os.path.abspath(os.path.join(dir1,items)))
	return L
def main():
	if len(sys.argv)>2:
		dir1=sys.argv[1]
		dir2=sys.argv[2]
	else:
		print "USAGE:",sys.argv[0],"datadir backdir"
	source_file=commpare(dir1,dir2)
	dir1=os.path.abspath(dir1)
	if not dir2.endswith("/"):dir2=dir2+'/'
	dir2=os.path.abspath(dir2)
	back_file_name=[]
	print source_file
	for item in source_file:
		back_file=re.sub(dir1,dir2,item)
		back_file_name.append(back_file)
		status=False
		if os.path.isdir(item):
			if not os.path.exists(back_file):
				os.makedirs(back_file)
				status=True
	if status:
		source_file=[]
		back_file_name=[]
		source_file=commpare(dir1,dir2)
		for item in source_file:
			back_file=re.sub(dir1,dir2,item)
			back_file_name.append(back_file)
		print source_file
	copy_file=zip(source_file,back_file_name)
	for item in copy_file:
		if os.path.isfile(item[0]):
			shutil.copyfile(item[0],item[1])
	print copy_file
if __name__=='__main__':
	main()
