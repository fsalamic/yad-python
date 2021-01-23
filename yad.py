import re,requests,sys,time,threading
from os import mkdir,listdir

if len(sys.argv) < 2  :
	link = input("Enter the Archived Youtube video link: ")
elif len(sys.argv) > 2 and sys.argv[2] == "--help" or "\h":
	print("""Youtube Archive Downloader by https://github.com/fsalamic
This program allows you to download YouTube videos files
that are archived on Wayback Machine from Archive.org.

Usage: python3 yad.py *archived youtube video link*

or

python3 yad.py 
Enter the Deleted Youtbe video link: *archived youtube video link*

To show this help page python3 yad.py --help or python3 yad.py \h
""")
	exit()
else:
	link = str(sys.argv[1])

print ('YouTube Archive Downloader')

video_id = re.sub(".*\?v=","",link)
download_url = ("https://web.archive.org/web/2oe_/http://wayback-fakeurl.archive.org/yt/"+video_id)
folderexists = 0
if 'downloads' in (listdir()):
	folderexists += 1
else:
	mkdir('downloads',0o755)
	folderexists += 1

def checker_web():
	r = requests.get(download_url,timeout=3)
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
		open('downloads/' + video_id + '.mp4', 'wb').write(download.content)
		print ("Video downloaded.")
	else:
		print ("Video not found.\n")
