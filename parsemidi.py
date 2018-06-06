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

