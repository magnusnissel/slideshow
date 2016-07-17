#!/usr/bin/python

import glob
import os
import uuid
import subprocess
from mutagen.mp3 import MP3


OUTPUT_FILE='slideshow.mp4'    # Name of output video
CROSSFADE=2.0                  # Crossfade duration between two images
AUDIO='doc_fam_phg.mp3'        # Name of the mp3 audio file to use


def script(input_files, total, ofile):
    """Assemble the ffmpeg script."""
    n = len(input_files)
    # duration = (total - (n-1) * CROSSFADE) / (1.0 * n)
    t = total / (2.0 * n - 1.0)

    ingest = ''
    filters = ''
    output = '[0:v]'

    last = n - 1
    for i, fi in enumerate(input_files):
        ingest += ' -loop 1 -t %.2f -i %s' % (t, fi)

        if i != last:
            #filters += " [%s:v][%s:v]blend=all_expr='A*(if(gte(T,%s),"  % (i+1, i, CROSSFADE)
            filters += " [%s:v]trim=duration=%s[a%s]; [%s:v][a%s]blend=all_expr='A*(if(gte(T,%s),"  % (i, CROSSFADE, i, i+1, i, CROSSFADE)
            filters += "1,T/%s))+B*(1-(if(gte(T,%s),1," % (CROSSFADE, CROSSFADE)
            filters += "T/%s)))'[b%sv];"    % (CROSSFADE, i+1)

        if i != 0:
            output+="[b%sv][%s:v]" % (i, i)

    output += 'concat=n=%s:v=1:a=0,format=yuv420p[v]' % (len(input_files) * 2 - 1)

    script = 'ffmpeg %s -filter_complex "%s %s" -map "[v]" -r 30 -preset superfast -vcodec libx264 %s' % \
        (ingest, filters, output, ofile)
    return script


def find_files():
    """Find all *.jpg files in current folder."""
    return sorted(glob.glob('*.jpg'))


def audio_length(file_name):
    """Read the total play time of the MP3 file."""
    audio = MP3(file_name)
    return audio.info.length


def main():
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
    input_files = find_files()
    total = audio_length(AUDIO)
    tf_name = '/tmp/%s.mp4' % uuid.uuid4()
    subprocess.call(script(input_files, total, tf_name), shell=True)
    # add the audio
    subprocess.call('ffmpeg -i %s -i %s -codec copy  -shortest %s' % 
        (tf_name, AUDIO, OUTPUT_FILE), shell=True
    )
    # delete tempfile
    if os.path.exists(tf_name):
        os.remove(tf_name)

if __name__ == '__main__':
    main()
