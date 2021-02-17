from tkinter import *
from tkinter import ttk
from pytube import *
from PIL import Image,ImageTk
import requests
import io
import os
import pyperclip

class App:
    #! Initialization 
    def __init__(self,root):
        #! Initial
        self.root = root
        self.root.title('Youtube Downloader')
        self.root.geometry('800x420+350+200') 
        self.root.resizable(False,False)
        self.root.config(bg='white')
        icon = Image.open('Image\icon.png')
        photo = ImageTk.PhotoImage(icon)
        self.root.iconphoto(False,photo)
        
        #! Title
        title = Label(self.root,text='YouTube Downloader',font=('times new roman',15),bg='#262626',fg='white').pack(side=TOP,fill=X) 
        
        #! URL Label and Entry
        self.var_url = StringVar()
        lbl_url = Label(self.root,text='Video URL:',font=('times new roman',15),bg='white').place(x=10,y=50)
        lbl_entry = Entry(self.root,font=('times new roman',13),bg='lightyellow',textvariable=self.var_url).place(x=120,y=50,width=670) 
        
        #! File type Label and Radio Button
        lbl_filetype = Label(self.root,text='File Type:',font=('times new roman',15),bg='white').place(x=10,y=90)
        self.var_fileType = StringVar()
        self.var_fileType.set('Video')
        video_radio = Radiobutton(self.root,text='LQ Video',variable=self.var_fileType,value='Video',font=('times new roman',15),bg='white',activebackground='white').place(x=120,y=90)
        high_radio = Radiobutton(self.root,text='HQ Video',variable=self.var_fileType,value='High',font=('times new roman',15),bg='white',activebackground='white').place(x=250,y=90)
        audio_radio = Radiobutton(self.root,text='Only Audio',variable=self.var_fileType,value='Audio',font=('times new roman',15),bg='white',activebackground='white').place(x=380,y=90)
        
        #! Search Button
        btn_search = Button(self.root,text='Search',font=('times new roman',15),bg='blue',fg='white',command=self.search).place(x=670,y=90,height=30,width=120) 
        
        #! Paste button
        btn_paste = Button(self.root,text='Paste URL',font=('times new roman',15),bg='Yellow',fg='Black',command=self.paste).place(x=560,y=90,height=30,width=100) 
        
        #! Frame Area
        frame1 = Frame(self.root,bd=2,relief=RIDGE,bg='lightyellow')
        frame1.place(x=10,y=130,width=780,height=180) 
        
        #! Video Name
        self.video_title = Label(frame1,text='Video Title Here',font=('times new roman',12),bg='lightgrey',anchor='w')
        self.video_title.place(x=0,y=0,relwidth=1) 
        
        #! Video Image
        self.video_image = Label(frame1,font=('times new roman',15),bg='white',bd=2,relief=RIDGE)
        self.defalt_img = Image.open('Image\icon.png')
        self.defalt_img = self.defalt_img.resize((180,140),Image.ANTIALIAS) 
        self.defalt_img = ImageTk.PhotoImage(self.defalt_img)
        self.video_image.config(image=self.defalt_img)
        self.video_image.place(x=5,y=30,width=220,height=140) 
        
        #! Video Description
        lbl_desc = Label(frame1,text='Description:',font=('times new roman',15),bg='lightyellow').place(x=230,y=30) 
        self.video_desc = Text(frame1,font=('times new roman',12),bg='lightyellow')
        self.video_desc.place(x=230,y=60,width=540,height=110)  
        
        #! Video Length 
        self.lbl_length = Label(self.root,text='Duration: 0:0:0',font=('times new roman',13),bg='white')
        self.lbl_length.place(x=10,y=320) 
        
        #! Video Size
        self.lbl_size = Label(self.root,text='Total Size: - MB',font=('times new roman',13),bg='white')
        self.lbl_size.place(x=200,y=320)
        
        #! Video Downlord percentage
        self.lbl_percentage = Label(self.root,text='Downlording: 0%',font=('times new roman',13),bg='white')
        self.lbl_percentage.place(x=420,y=320) 
        
        #! Clear Button
        btn_clear = Button(self.root,text='Clear',font=('times new roman',13),bg='gray',fg='white',command=self.clear).place(x=620,y=320,height=25,width=70) 
        
        #! Downlord Button
        self.btn_downlord = Button(self.root,text='Downlord',font=('times new roman',13),bg='green',fg='white',command=self.download,state=DISABLED)
        self.btn_downlord.place(x=700,y=320,height=25,width=90) 
        
        #! Progress Bar
        self.prog = ttk.Progressbar(self.root,orient=HORIZONTAL,length=500,mode='determinate')
        self.prog.place(x=10,y=360,width=780,height=25) 
        
        #! Error Message
        self.lbl_message = Label(self.root,text='',font=('times new roman',13),bg='white')
        self.lbl_message.place(x=0,y=390,relwidth=1)
        
        #! Create Audio/Video file
        if not os.path.exists('Audios'):
            os.mkdir('Audios')
        if not os.path.exists('Videos'):
            os.mkdir('Videos')
        if not os.path.exists('High'):
            os.mkdir('High')
        
    #! Search function
    def search(self):
        try:
            #! Get URL
            yt = YouTube(self.var_url.get())               
            
            #! Select File type and search whether the file is exist or not
            if self.var_fileType.get() == 'Audio':
                select_file = yt.streams.filter(only_audio=True,file_extension='mp4').first()
                if os.path.exists('Audios/'+yt.title+'.mp4'):
                    self.btn_downlord.config(state=DISABLED)
                    self.lbl_message.config(text='Audio file already exist',fg='blue')
                else:
                    self.btn_downlord.config(state=NORMAL)
                    self.lbl_message.config(text='Search completed',fg='blue')
                    
            if self.var_fileType.get() == 'Video':
                select_file = yt.streams.filter(progressive=True,file_extension='mp4').first()    
                if os.path.exists('Videos/'+yt.title+'.mp4'):
                    self.btn_downlord.config(state=DISABLED)
                    self.lbl_message.config(text='Video file already exist',fg='blue')
                else:
                    self.btn_downlord.config(state=NORMAL)
                    self.lbl_message.config(text='Search completed',fg='blue')
                
            if self.var_fileType.get() == 'High':
                select_file = yt.streams.filter(progressive=True,file_extension='mp4').last()   
                if os.path.exists('High/'+yt.title+'.mp4'):
                    self.btn_downlord.config(state=DISABLED)
                    self.lbl_message.config(text='High file already exist',fg='blue')
                else:
                    self.btn_downlord.config(state=NORMAL)
                    self.lbl_message.config(text='Search completed',fg='blue')
            
            #! Display title                                         
            self.video_title.config(text=yt.title)                        
            
            #! Display description                                 
            self.video_desc.delete('1.0',END)                           
            self.video_desc.insert(END,yt.description[:200])                            
            
            #! Display thumbnail                               
            response = requests.get(yt.thumbnail_url)
            img_byte = io.BytesIO(response.content)
            self.img = Image.open(img_byte)
            self.img = self.img.resize((220,140),Image.ANTIALIAS) 
            self.img = ImageTk.PhotoImage(self.img)
            self.video_image.config(image=self.img)
                
            #! Display size of file
            self.size_inBytes = select_file.filesize
            max_size = self.size_inBytes/1024000
            self.mb = str(round(max_size,2))
            self.lbl_size.config(text='Total size: '+self.mb+' MB')
            
            #! Function to convert sec to H:M:S
            def get_time(sec):
                mins = sec // 60
                sec = sec % 60
                hours = mins // 60
                mins = mins % 60
                return 'Duration: ' + str(hours) +':' + str(mins) + ':' + str(sec)
            
            #! Display length of file
            self.lbl_length.config(text = get_time(yt.length))
            
        except:
            #! If Error is raised
            self.lbl_message.config(text='Video URL is required',fg='red')
            
    #! Paste function
    def paste(self):
        self.var_url.set(pyperclip.waitForPaste()) 
        
    #! Progress Bar
    def progress(self,streams,chunk,bytes_remaining):
        percentage = (float(abs(bytes_remaining-self.size_inBytes)/self.size_inBytes))*float(100)
        self.prog['value']=percentage  
        self.prog.update()
        self.lbl_percentage.config(text='Downlording: '+str(round(percentage,2))+' %')  
        if round(percentage,2) == 100:
            self.lbl_message.config(text='Download Completed',fg='green')
            self.btn_downlord.config(state=DISABLED)
            
    #! Clear all
    def clear(self):
        self.var_fileType.set('Video')
        self.var_url.set('')
        self.prog['value']=0
        self.btn_downlord.config(state=DISABLED)
        self.lbl_message.config(text='')
        self.video_title.config(text='Video Title Here')
        self.video_image.config(image=self.defalt_img)
        self.video_desc.delete('1.0',END)
        self.lbl_length.config(text='Duration: 0:0:0')
        self.lbl_size.config(text='Total Size: - MB')
        self.lbl_percentage.config(text='Downlording: 0%')
    
    def download(self):
        #! Get URL
        yt = YouTube(self.var_url.get(),on_progress_callback=self.progress)   
        
        #! Select File type
        if self.var_fileType.get() == 'Audio':
            select_file = yt.streams.filter(only_audio=True,file_extension='mp4').first()
            select_file.download('Audios/')   
        if self.var_fileType.get() == 'Video':
            select_file = yt.streams.filter(progressive=True,file_extension='mp4').first()
            select_file.download('Videos/')  
        if self.var_fileType.get() == 'High':
            select_file = yt.streams.filter(progressive=True,file_extension='mp4').last()
            select_file.download('High/')

if __name__ == '__main__':
    root = Tk()
    obj = App(root)
    root.mainloop()