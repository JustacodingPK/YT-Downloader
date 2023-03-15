#!/usr/bin/env python


# Download a YouTube video/audio

from pytube import YouTube

url = ""

while url.strip() == "":
    url = input("Enter the YouTube URL: ")
default_format = "audio"
format = input("What do you want, audio or video? Enter a or v: ") or default_format

yt_obj = YouTube(url)

if format in ("a", "A", "audio", "Audio"):
    print("audio is being downloaded...")
    audio_file = yt_obj.streams.filter(file_extension='webm', only_audio=True)
    audio_file[0].download()
elif format in ("v", "V", "video", "Video"):
    print("video is being downloaded...")
    video_file = yt_obj.streams.filter(file_extension='mp4', only_video=False)
    video_file[0].download()
else:
    print("please enter, audio or video, a or v.")


