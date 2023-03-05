from pytube import YouTube
import text2art
link = input("Enter YouTube URL:")

yv = YouTube(link)
print("Title",yv.title)
print("views",yv.views)
print("Duration",yv.length)
yd = yv.streams.get_highest_resolution()
print("Wait for Downloading")

yd.download()

print("Your Video Successfully Downloaded")
author = "justacoding "
print(text2art,(author))
# Author by Justacoding Follow for more 
# FB       @justacoding 
# insta   @justacoding 
# Tiktok @justacoding 

