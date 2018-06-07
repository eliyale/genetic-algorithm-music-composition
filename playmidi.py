# play an embedded midi music file on your computer's sound card
# experiments with module pygame from: http://www.pygame.org/
# tested with Python25 and PyGame171      vegaseat      04sep2007

# use this short program to create the base64 encoded midi music string
# (base64 encoding simply produces a readable string from binary data)
# then copy and paste the result into your pygame program ...
# import base64
# mid_file = "./midifiles/Africa.mid"
# print(base64.encodestring(open(mid_file, 'rb').read()))
# mid64="'''\\\n" + str(base64.encodestring(open(mid_file, 'rb').read())) + "'''"


import pygame
import base64
from mido import Message, MidiFile, MidiTrack
import random
import time

def play_music(music_file):
    """
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    """
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(music_file)
        print("Music file %s loaded!", music_file)
    except pygame.error:
        print( "File %s not found! (%s)", (music_file, pygame.get_error()))
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)

#play a .mid file with the pygame mixer
def play_file(filename):

    music_file = filename
    # the below code is included for legacy reasons
    # convert back to a binary midi and save to a file in the working directory
    # fish = base64.b64decode(mid64)
    # fout = open(music_file,"wb")
    # fout.write(fish)
    # fout.close()
    freq = 44100    # audio CD quality
    bitsize = -16   # unsigned 16 bit
    channels = 2    # 1 is mono, 2 is stereo
    buffer = 1024    # number of samples
    pygame.mixer.init(freq, bitsize, channels, buffer)
    # optional volume 0 to 1.0
    pygame.mixer.music.set_volume(0.8)
    try:
        # use the midi file you just saved
        play_music(music_file)
    except KeyboardInterrupt:
        # if user hits Ctrl/C then exit
        # (works only in console mode)
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.stop()
        raise SystemExit

#save a list of midi notes as a midifle in the directory
def save_song(midi_list):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(Message('program_change', program=12, time=0))
    for midi_note in midi_list:
        track.append(Message('note_on', note=int(midi_note), velocity=110, time=160))
        track.append(Message('note_off', note=int(midi_note), velocity=127, time=64))

    mid.save('generated_song.mid')

#play a list of midi notes by saving the file, then calling the play_file method
#note a file is created, list_song.mid, in order to play it, it is generally not needed
#after execution of this function
def play_list(midi_list):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(Message('program_change', program=12, time=0))  #program=12 is the marimba
    for midi_note in midi_list:
        track.append(Message('note_on', note=int(midi_note), velocity=110, time=160))
        track.append(Message('note_off', note=int(midi_note), velocity=127, time=64))

    mid.save('list_song.mid')
    play_file('list_song.mid')







