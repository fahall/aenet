import os.path as osp
from glob import glob

from pydub import AudioSegment
from tqdm import tqdm

DATA_HOME = '/data/'
AUDIO_RAW = osp.join(DATA_HOME, 'audio_raw')
AUDIO_OUT = osp.join(DATA_HOME, 'audio')


def infile_to_outfile(infile, filetype='.wav'):
    title = osp.splitext(osp.basename(infile))[0]
    return osp.join(AUDIO_OUT, title + filetype)


def convert(infile, new_file_extension='.wav'):
    old_ext = osp.splitext(infile)[1][1:]  # remove leading '.'

    outfile = infile_to_outfile(infile, new_file_extension)
    if not osp.exists(outfile):
        try:
            sound = AudioSegment.from_file(infile, format=old_ext)
            # remove leading '.'
            return sound.export(outfile, format=new_file_extension[1:])
        except:
            with open('falures.txt', 'a') as f:
                f.write(outfile + '\n')


if __name__ == "__main__":
    audio_files = glob(osp.join(AUDIO_RAW, '*.m4a'))

    for a in tqdm(audio_files):
        convert(a)
