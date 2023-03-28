#                                     ***** download Youtube Audio File ***** 

from pytube import YouTube 

class YoutubeDowload:
 
       def audiodownlaod(self,YoutubeURL): 
         try:
            youtube_1 = YouTube(YoutubeURL)
            # print(youtube_1.title)
            # print(youtube_1.thumbnail_url)
            audios = youtube_1.streams.filter(only_audio=True)
            vid = list(enumerate(audios))
            for element in vid:
                print(element)
            
            strm = int(input("enter : "))
            audios[strm].download()
            print(" Your audio download successfully :",youtube_1.title)

         except Exception as e:
            print(e) 


Object=YoutubeDowload()
link1 = "https://www.youtube.com/watch?v=fWVtPYZxRXE"
Object.audiodownlaod(link1)   # audio function call