## Youtube Archive Downloader (Python)

This program allows you to download YouTube videos files that are archived on Wayback Machine from Archive.org

Usage: 
``` 
python3 yad.py *your link* ⏎
(for example: python3 yad.py https://web.archive.org/web/20180214215840/https://www.youtube.com/watch?v=aqz-KE-bpKQ)
```
or
```
python3 yad.py
Enter the Archived Youtube video link: https://web.archive.org/web/20180214215840/https://www.youtube.com/watch?v=aqz-KE-bpKQ ⏎
```
Features:
- The program downloads the video file as the video id into the folder called "downloads"
- If the folder called "downloads" doesn't exist , it will be created
- The program can be used with arguments passed in the command (as seen in the first example) 
- It can also be used by entering the link after running the program (as seen in the second example)
- If the video doesn't exist the program will exit and inform you that the video does not exist

How to Install:
```
git clone https://github.com/fsalamic/yad-python.git
cd yad-python
pip3 install -u requirements.txt
```
