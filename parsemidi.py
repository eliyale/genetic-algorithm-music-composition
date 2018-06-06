#this file contains several helper functions for parsing midi files
#and input. It is seperated from the playmidi files for simplicity and 
#ease of use.

import mido

#this function takes a midifile and returns a list of strings of midi notes
#please note the notes are integers when they are readm but they are converted to strings
#so that they can be inputted to the genetic algorithm.
#also, then notes are added monophonetically in the order in which they appeare in the file
#multiple midi notes cannot be read at once
def parse_midi_file(filename):
    midi_list = []
    mid = mido.MidiFile(filename)
    for msg in mid:
        if msg.type == 'note_on' and msg.velocity != 0:
            #print(msg.note)
            midi_list.append(str(msg.note))
    #print(midi_list)
    return midi_list

#this function will read any available midi inputs
#and parse them one at a time in the order they are received
#it listens for 48 notes, (4 notes per bar in the 12 bar blues)
#then returns the midi list
def parse_midi_input():
    midi_list = []
    inport = mido.open_input()
    note_count = 0
    while(note_count <= 48):
        msg = inport.receive()
        print(msg)
        if msg.type == 'note_on' and msg.velocity != 0:
            midi_list.append(str(msg.note))
            note_count = note_count + 1

    return midi_list

