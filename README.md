Music Generation With a Genetic Algorithm

Eli Yale
June 6, 2018

This source code is for the final project in COEN 160:
Introduction to AI at Santa Clara University taught by Professor
Maya Ackerman

This source code includes

1) genetic.py
	A genetic algorithm class to generate python lists that 
	resemble a target list.

2) driver.py
	A main driver function used to interact with the genetic algorithm.
	It has various modes of operation described in useage below. 

3) playmidi.py, parsemidi.py, midi_strings.py, LZ77.py
	Files containg helper functions for inputing and outputting midi
	as well as the LZ77 compression algorithm.


USAGE:

If you would like to simply use my genetic algorithm class you may in your python code:

	include genetic.py
	#define a target array of strings
	target = ['','']
	#define the alphabet used to generate the target
	alphabet = ['','']
	#instantiate the generator
	generator = Generator(target, alphabet)
	#run the gnerator
	output = generator.run()
	#Please see the actual file for more documentation and parameters

If you would like to use the interactive tool from your command line run:

	driver.py [--verbose] [--interact] [--train] [--play] filename

where --verbose will print details while the algorithm runs
	  --interact will allow you to input midi from an available midi controller plug into your computer
	  	it will read, 48 notes (for the 12 bar blues) then begin the algorithm on that input
	  --train will instead read a midifile given in 'filename' and use this as input to the algorithm
	  --play allows you to play back the midifile you generated