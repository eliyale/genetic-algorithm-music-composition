from genetic import *
from playmidi import *
from parsemidi import *

if __name__ == '__main__':

    target = parsemidi("midifiles/twinkle.mid")

    parser = argparse.ArgumentParser(description='generate music with a genetic algorithm')
    #parser.add_argument('dataset', metavar='dataset', nargs=1, type=str)
    parser.add_argument('--verbose', dest='x', action='store_const', const=True, default=False)
    args = parser.parse_args()


    #target_string = 

    #target = [str(x) for x in [29, 31, 45, 33, 25, 25, 34, 35, 29, 22, 22, 22, 34, 39, 51, 48, 48, 22, 22, 22]]
    #alphabet = list(string.ascii_letters+string.digits)
    alphabet = [str(x) for x in list(range(29,76))]

    

    generator = Generator(target, alphabet, iterations = 30, verbose=args.x)
    new_midi_list = generator.run()


    random_song = [str(random.choice(alphabet)) for x in range(len(new_midi_list))]

    print(new_midi_list)
    play_list(target)
    play_list(random_song)
    play_list(new_midi_list)

    #play_file('midifiles/Africa.mid')

