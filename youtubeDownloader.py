from pytubefix import YouTube
from sys import argv

link = input("Enter the link of the video: ")
yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)

print(yt.title)

format = input("Choose resolution: h(high) l(low) a(audio)")
if format == 'a':
  print("downloading the audio, please wait...")
  yd = yt.streams.get_audio_only()
  if yd :
    yd.download('C:/Users/RYZEN/Videos/pytubed')
    print("audio downloaded successfully in C:/Users/RYZEN/Videos/pytubed")
  elif format == 'h':
      print("downloading the video, please wait...")
      yd = yt.streams.get_highest_resolution()
      if yd :
        yd.download('C:/Users/RYZEN/Videos/pytubed')
        print("video downloaded successfully in C:/Users/RYZEN/Videos/pytubed")
  elif format == 'l':
    print("downloading the video, please wait...")
    yd = yt.streams.get_lowest_resolution()
    if yd :
      yd.download('C:/Users/RYZEN/Videos/pytubed')
      print("video downloaded successfully in C:/Users/RYZEN/Videos/pytubed")
