from pytube import *

url = str(input('Enter the URL: '))
try:
    yt = YouTube(url) 
except:
    print('Invalid URL')
    exit()

title = yt.title  
print('Title: '+title)

thumbnail = yt.thumbnail_url  
print('Thumbnail: '+thumbnail)

desc = yt.description[:200]
print('Description: '+desc)

time = yt.length
print('Time: '+str(time)+' seconds')

Highvideo_file = yt.streams.filter(progressive=True,file_extension='mp4').last()
print('High video : '+str(Highvideo_file))

H_size_inBytes = Highvideo_file.filesize
H_max_size = H_size_inBytes/1024000
H_mb = str(round(H_max_size,2))
print('High quality video size: '+H_mb+'MB')

Lowideo_file =yt.streams.filter(progressive=True,file_extension='mp4').first()  
print('Low video : '+str(Lowideo_file))

L_size_inBytes = Lowideo_file.filesize
L_max_size = L_size_inBytes/1024000
L_mb = str(round(L_max_size,2))
print('Low quality video size: '+L_mb+'MB')

OnlyAudio_file = yt.streams.filter(only_audio=True,file_extension='mp4').last()
print('Audio : '+str(OnlyAudio_file))

A_size_inBytes = OnlyAudio_file.filesize
A_max_size = A_size_inBytes/1024000
A_mb = str(round(A_max_size,2))
print('Audio size: '+A_mb+'MB')

# Highvideo_file.download('High/') 
# Lowideo_file.download('Videos/')
# OnlyAudio_file.download('Audios/')  