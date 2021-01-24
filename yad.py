import re, requests, sys, time, threading, argparse
from os import mkdir, listdir

parser = argparse.ArgumentParser(description='This program allows you to download YouTube videos files that are archived on Wayback Machine from Archive.org.')
parser.add_argument('link', metavar='link', type=str, action='store', default='',
                    help='enter a link for the youtube video you would like to archive (it could be from youtube or from wayback machine)')

print ('YouTube Archive Downloader')
#print(len(sys.argv))

def link_check():
	if len(sys.argv) < 2:
		link = input(str("Enter the Archived Youtube video link: "))
		return link
		print(len(sys.argv))
	else:
		args = parser.parse_args()
		link = str(args.link)
		return link

videolink = str(link_check())
#video_id = re.search('v=(.*)|&|yt/(.*)', videolink)[1]
video_id = re.sub(".*\?v=" , "", videolink)
download_url = ("https://web.archive.org/web/2oe_/http://wayback-fakeurl.archive.org/yt/"+video_id)
folderexists = 0

#print(link_check())
if 'downloads' in (listdir()):
	folderexists += 1
else:
	mkdir('downloads',0o755)
	folderexists += 1

def checker_web():
	h = requests.head(download_url)
	h2 = h.headers.get('location')
	response = str(h.status_code)
	if response == "302":
		time.sleep(10)
	elif response == "404":
		exit()
	text = requests.head(h2)
	#print (text)
	type = text.headers.get('content-type')
	type2 = re.sub(".*\/" , "", str(type))

	return str(type2)
	exit()

if folderexists == 1:
	time.sleep(1)
	print("Checking if the video exists in the Web Archive...")
	checker = threading.Thread(target=checker_web)
	checker.start()
	time.sleep(4)
	if checker.is_alive() :
		print("Video found!\nDownloading... (Please be patient, this could take a while)")
		download = requests.get(download_url)
		vid_type = str(checker_web())
		filepath = 'downloads/'+ video_id + ('.'+vid_type or '.mp4')
		open(filepath, 'wb').write(download.content)
		#with open(filepath, 'w') as file:
    		#	file.write(download.content)
		print ("Video downloaded.")
	else:
		print ("Video not found.\n")
