#coding= utf-8
import sys,urllib,chardet,time,os

# get the html content, input: url, output: content
def getHtml(url):
	#url="http://www.imaibo.net/live/1954702"
	wp = urllib.urlopen(url)
	content = wp.read()
	return content

# main function, no input, no output
def run():

	pass
if __name__ == '__main__':
	url='http://www.imaibo.net/index.php?app=home&mod=Space&act=getSpaceWeibo300&uid=1954702&limit=10&p=1&lastId=0&syncShareSpaceWeiboId=0'
	try:
		content=getHtml(url).count('\u')
	except Exception, e:
		content=0
	'''
	print type(content)
	content1=content.decode('ascii')
	print type(content1)
	print content1
	content2=content.decode("ascii").encode("utf-8")
	print content2
	print type(content2)
	#print chardet.detect(content2)
	'''
	while (1):
		time.sleep(1)
		try:
			newcontent = getHtml(url).count('\u')
		except Exception, e:
			newcontent = content
		#print content.count('\u')

		if newcontent!=content:
			os.system('say "There is a new message. There is a new message." ')
			print time.localtime()
		else:
			print 'nothing'
			pass
		content=newcontent


