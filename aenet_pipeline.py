import logging
import os.path as osp
import pickle
import sys
from glob import glob

from aenet import AENet
from pydub import AudioSegment
from scipy import sparse
from tqdm import tqdm

DATA_HOME = '/data/'
AUDIO_HOME = osp.join(DATA_HOME, 'audio')
AUDIO_EXT = '.wav'
OUT_DIR = osp.join(DATA_HOME, 'aenet_results')


def setup_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler('log.txt', mode='w')
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)
    return logger


logger = setup_custom_logger(__name__)


def title_to_output(title):
    return osp.join(OUT_DIR, title + '.pkl')


def path_to_title(path):
    return osp.splitext(osp.basename(f))[0]


if __name__ == "__main__":
    ae = AENet()
    audio_files = glob(osp.join(AUDIO_HOME, '*' + AUDIO_EXT))
    logger.info(' '.join(['Found:', str(len(audio_files)),
                          'audio files in', AUDIO_HOME])
                )

    logger.info('Extracting features...')
    # default shift. explicit > implicit
    feats = ae.feat_extract(audio_files, shift=100)
    titles = [path_to_title(f) for f in audio_files]
    feats = [sparse.csr_matrix(f) for f in feats]
    outfiles = [title_to_output(f) for f in titles]
    data = zip(feats, outfiles)
    logger.info('Saving outputs...')
    for d in tqdm(data):
        with open(d[1], 'wb') as f:
            pickle.dump(data[0], f)
