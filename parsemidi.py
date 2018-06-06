import mido

def parse_midi_file(filename):
    midi_list = []
    mid = mido.MidiFile(filename)
    for msg in mid:
        if msg.type == 'note_on' and msg.velocity != 0:
            #print(msg.note)
            midi_list.append(str(msg.note))
    #print(midi_list)
    return midi_list


def parse_midi_input():
	pass