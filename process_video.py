import os
from moviepy.editor import VideoFileClip
from tqdm import tqdm


for file in tqdm(os.listdir('demos/demo_all')):
    if file.split('.')[-1] == 'mp4':
        cur_video = VideoFileClip(os.path.join('demos/demo_all', file))
        cur_video.write_videofile(os.path.join('demos/demo_all', file), fps=24, codec="mpeg4", audio_codec='aac')