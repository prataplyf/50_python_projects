from pytube import YouTube
from tqdm import tqdm # progressbar library
import time 

# for converting data into kb
chunk_size = 1024
# https://www.youtube.com/watch?v=d3D7Y_ycSms

def start_download(link):
    global count
    count = 0
    flag = True
    while flag:
        try:
            print("entered")
            yt = YouTube(link)
            # video_type = yt.streams.filter(progressive=True, file_extension='mp4').first()
            print("linked url")
            if yt is not None:
                flag = False
            else:
                continue
        except:
            count += 1
            print("ERROR. Check your:\n  -connection\n  -url is a YouTube url\n\nTry again.")
            # call function for restart download
            if count >3:
                print("Network Connection: Poor. Please check your internet connection")
                flag = False
            else:
                start_download(link)
    time.sleep(0.5)
    print("Network Connection: OK")
    time.sleep(1)
    #Showing details
    print("Title: ",yt.title)
    time.sleep(0.02)
    print("Number of views: ",yt.views)
    time.sleep(0.02)
    print("Length of video: ",yt.length)
    time.sleep(0.02)
    print("Rating of video: ",yt.rating)
    time.sleep(0.02)
    # file size
    # print('FileSize : ' + str(round(video_type.filesize/(1024*1024))) + 'MB')
    time.sleep(1)
    # Download video
    for i in tqdm(range(100), desc="Downloading...", ascii=True, ncols=100):
        i += 1
        time.sleep(0.03)
    # video_type.download()
    print("Done")
    

# youtube url
link = input("Enter the link of YouTube video you want to download:  ")
start_download(link)