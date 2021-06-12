'''
视频剪辑用,可转换为mp4, gif格式
Author: Ran S.Y.
E-Mail: rsy98@163.com
'''
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import tkinter.filedialog as tkf
import os
import moviepy.editor as mpy

class VideoCut:
    def __init__(self, start_time, end_time):
        self.path = tkf.askopenfilename()
        self.start_time = start_time
        self.end_time = end_time
    def videoName(self):
        return os.path.basename(self.path)
    def videoNameNoextension(self):
        return os.path.splitext(self.path)[0]
    def videoPath(self):
        return self.path
    def videoContent(self):
        return mpy.VideoFileClip(self.videoPath())
        # self.file_name.delete(0, 'end')
        # self.file_name.insert(1, self.path)
    def outMp4Path(self):
        return os.path.join(self.videoNameNoextension()+'_'+format(self.start_time)+'-'+format(self.end_time)+"_cut"+'.mp4')
        # return os.path.join(os.path.dirname(self.videoPath()),self.videoName()+"_cut"+'.mp4')
    def outGifPath(self):
        return os.path.join(self.videoNameNoextension()+'_'+format(self.start_time)+'-'+format(self.end_time)+"_cut"+'.gif')
    def cutVideo(self):
        ffmpeg_extract_subclip(self.videoPath(), self.start_time, self.end_time, targetname=self.outMp4Path())
    def writeGif(self):
        gif = self.videoContent().subclip((0, self.start_time), (0, self.end_time)).resize((320, 240))
        gif.write_gif(self.outGifPath())

videoCut = VideoCut(17,39)

# videoCut.cutVideo()
videoCut.writeGif()
