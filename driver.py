from genetic import *
from playmidi import *
from parsemidi import *

if __name__ == '__main__':


    parser = argparse.ArgumentParser(description='generate music with a genetic algorithm')
    #parser.add_argument('dataset', metavar='dataset', nargs=1, type=str)
    parser.add_argument('--verbose', dest='x', action='store_const', const=True, default=False)
    parser.add_argument('--interact', dest='interact', action='store_const', const=True, default=False)
    parser.add_argument('--train', dest='train', action='store_const', const=True, default=False)
    args = parser.parse_args()

    global verbose_print
    verbose_print = print if args.x else lambda *a, **k: None

    if args.interact:
        #read midi input
        #target = parse_midi_input()
        target = parse_midi_input()

    else:
        target = parse_midi_file("midifiles/twinkle.mid")




    #target_string = 

    #target = [str(x) for x in [29, 31, 45, 33, 25, 25, 34, 35, 29, 22, 22, 22, 34, 39, 51, 48, 48, 22, 22, 22]]
    #alphabet = list(string.ascii_letters+string.digits)
    alphabet = list(set(target))
    verbose_print(alphabet)
    
    if args.train:
        generator = Generator(target, alphabet, iterations = 100, verbose=args.x, crossover_rate = 0.8)
        new_midi_list = generator.run()
        save_song(new_midi_list)
    else:
        new_midi_list = parse_midi_file('generated_song.mid')

    #new_midi_list = ['65', '62', '52', '48', '67', '52', '69', '62', '55', '60', '52', '55', '60', '48', '60', '52', '67', '65', '53', '48', '52', '62', '55', '67', '52', '67', '53', '48', '52', '67', '52', '65', '50', '65', '65', '60', '48', '65', '62', '52', '62', '53', '62', '67', '69', '53', '69', '67', '52', '52', '67', '69', '53', '69', '50', '65', '64', '48', '64', '62', '55', '60', '48', '65', '62', '52', '48', '67', '52']
    random_song = [str(random.choice(alphabet)) for x in range(len(new_midi_list))]

    verbose_print("generated song:", new_midi_list)
    play_list(target)
    input()
    play_list(random_song)
    input()
    play_file('generated_song.mid')

    #play_file('midifiles/Africa.mid')

