import subprocess
from pydub import AudioSegment
from glob import glob
import os.path as osp
DATA_HOME = '/app/data/'
AUDIO_RAW = osp.join(DATA_HOME, 'audio_raw')
AUDIO_OUT = osp.join(DATA_HOME, 'audio')



if __name__ == "__main__":
    audio_files = glob(osp.join(AUDIO_RAW, '*.m4a'))
    print(audio_files)
