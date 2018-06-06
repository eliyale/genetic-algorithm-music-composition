from genetic import *
from playmidi import *
from parsemidi import *
import sys #for sys.exit


#this is the main driver that will be used for demo pruposes.
#it takes various command line arguments to interact with the program
#to see useage details please refer to the readme doc
if __name__ == '__main__':


    parser = argparse.ArgumentParser(description='generate music with a genetic algorithm')
    parser.add_argument('filename', metavar='filename', nargs='?', type=str, default=False)
    parser.add_argument('--verbose', dest='x', action='store_const', const=True, default=False)
    parser.add_argument('--interact', dest='interact', action='store_const', const=True, default=False)
    parser.add_argument('--train', dest='train', action='store_const', const=True, default=False)
    parser.add_argument('--play', dest='play', action='store_const', const=True, default=False)
    args = parser.parse_args()

    global verbose_print
    verbose_print = print if args.x else lambda *a, **k: None

    if not args.filename and not args.interact:
        print("please provide a file for non-interactive mode\n\nusage: driver.py [--verbose] [--interact] [--train] [--play] filename")
        sys.exit()
    if args.interact:
        #read midi input
        #target = parse_midi_input()
        target = parse_midi_input()
        alphabet = list(set(target))
        verbose_print(alphabet)

    elif args.filename:
        target = parse_midi_file(args.filename)
        alphabet = list(set(target))
        verbose_print(alphabet)

    if args.train:
        generator = Generator(target, alphabet, iterations = 50, verbose=args.x, crossover_rate = 0.8)
        new_midi_list = generator.run()
        save_song(new_midi_list)
    else:
        new_midi_list = parse_midi_file('generated_song.mid')

    if args.play:
        #new_midi_list = ['65', '62', '52', '48', '67', '52', '69', '62', '55', '60', '52', '55', '60', '48', '60', '52', '67', '65', '53', '48', '52', '62', '55', '67', '52', '67', '53', '48', '52', '67', '52', '65', '50', '65', '65', '60', '48', '65', '62', '52', '62', '53', '62', '67', '69', '53', '69', '67', '52', '52', '67', '69', '53', '69', '50', '65', '64', '48', '64', '62', '55', '60', '48', '65', '62', '52', '48', '67', '52']
        random_song = [str(random.choice(alphabet)) for x in range(len(new_midi_list))]

        verbose_print("generated song:", new_midi_list)
        play_list(target)
        input()
        play_list(random_song)
        input()
        play_file('generated_song.mid')


    if not args.interact and not args.play:
        print("please provide a mode\n\nusage: driver.py [--verbose] [--interact] [--train] [--play] filename")


    #play_file('midifiles/Africa.mid')

