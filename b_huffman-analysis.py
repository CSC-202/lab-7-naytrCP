# huffman-analysis.py
## author - nick s.
### get huffman.py working first, then work on this file

import matplotlib.pyplot as plt

# DATA - lyrics
LIKE_THE_MOVIES_LYRICS = 'Maybe one day I will fall in a bookstore. Into the arms of a guy. Well sneak into bars and gaze at the stars. surrounded by fireflies. Oh, Id like to sleep in till two on a sunday. And listen to the bluebirds sigh. Get soaked in the rain and smile through the pain. Slow dance under stormy skies. Maybe Im just old fashioned. Read too many fairytales. Its no wonder Ive had no luck. No ones ever good enough. I want a love like Ive seen in the movies. Thats why Ill never fall in love. Oh, maybe Im just old fashioned. Read too many fairytales. Its no wonder Ive had no luck. No ones ever good enough. I want a love like Ive seen in the movies. Thats why Ill never fall in love'
KILL_BILL_LYRICS = 'Im still a fan even though I was salty. Hate to see you with some other broad, know you happy. Hate to see you happy if Im not the one driving. Im so mature, Im so mature, Im so mature. i got me a therapist to tell me theres other men. I dont want none, I jsut want you. If I cant have you, no one should. I might. I might kill my ex. Not the best idea. His new girlfriends next. Howd I get here? I might kill my ex. I still love hime though. Rather be in jail than alone. I get the senses that its a lost cause. I get the sense that you might reallyb love her. The text gon be evidence, this text is evidence. I tried to ration with you, no murders or crimes of passion. But damn, you was out of reach. You was at the farmers market with yoiur perfect peach. Now Im in the basement, plannning home invasion. Now you laying face down. Got me saying over a beat. Im so mature, Im so mature, Im so mature. I got me a therapist it tell me theres other men. I dont want none, I just want you. If I cant have you, no one will, oh. I might kill my ex not the best idea. His new girlfriends next. Howd I get here? I might kill my ex. I still love him though. Rather be in jail than alone. I did it all for love. I did it all on no drugs. I did all of this sober. I did it all for us, oh. I did it all for love. I did all of this on no drugs. I did all this sober. Dont you know I did it all for us? Oh. I just killed my ex. No the best idea. killed his girlfriend next. Howd I get here? I jsut killed my ex. I still love him though. Rather be in hell than alone'
MA_BELLE_EVANGELINE_LYRICS = 'Look how she lights up the sky. Ma belle Evnageline. so far above me yet I. Know her heart belings to only me. Je t adore, je t aime Evangeline. Youre my queen of the night, so still, so bright. That someone as beautiful as she. Could love someone like me. Love always finds a way, its true. And I love you, Evangeline, ooh, yeah. Ooh, love is beautiful, love is wonderful. love is everything, do you agree? Mais oui. Lokk how she lights up the sky. I love you Evangeline.'

# DATA - mantras
ANNE_FRANK = 'dead people recieve more flowers than lving ones because regret is stronger than gratitude'
MULAN_1 = 'The flower that blooms in adversity is the most rare and beautiful of all'
MEX_INSP = 'Como que tienen ganas de ir a la escuela? Echenle ganas raza que nuestros padres no cruzaron para que fueramos flojos'

# the input, what we want to encode
def huffman(message: str) -> float:
    message = message.upper()

    # the output, should be all 0's and 1s
    result: str = str()

    # for counting the letter frequencies
    freq: dict = dict() # key  -> a letter
                        # item -> num of occurences

    # for holding the nodes of the huffman tree
    nodes: list = list() 

    # for storing the code for each letter
    coding: dict = dict()   # key  -> a letter
                            # item -> a binary encoding

    class Node:
        weight: int
        letters: str
        left: any
        right: any

        def __init__(self, weight, letter=None, left=None, right=None):
            self.weight = weight
            self.letter = letter
            self.left = left
            self.right = right
            return
    #  STEP 0
    ## defining our data structures
    ## defining operations
    def retrieve_codes(v: Node, path: str=''):
        if v.letter != None: # if 'TODO': # TODO
            coding[v.letter] = path # TODO
        else:
            retrieve_codes(v.left, path + '0') # TODO
            retrieve_codes(v.right, path + '1') # TODO
    # STEP 1
    ## counting the frequencies
    for x in message:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    # STEP 2
    ## initialize the nodes
    nodes = list()
    for letter, count in freq.items():
        nodes.append(Node(count, letter))

    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.weight, reverse=True)
        min_a: Node = nodes.pop()
        min_b: Node = nodes.pop()

        combined = Node(min_a.weight + min_b.weight, None, min_a, min_b)
        nodes.append(combined)

    # STEP 3
    ## combine each nodes until there's only one item in the nodes list
    

    # STEP 4
    ## reconstruct the codes
    tree_root = nodes[0]
    retrieve_codes(tree_root)
    print(coding)
    
    for x in message:
        result += str(coding[x])

    # STEP 5
    ## analyize compression performance
    n_original_bits: int = len(message) * 8
    n_encoded_bits: int = len(result)
    compression_ratio: float = (1 - n_encoded_bits / n_original_bits) * 100
    
    print(f'original: {n_original_bits:^4d} bits')
    print(f'encoded : {n_encoded_bits:^4d} bits')
    print(f'savings : {int(compression_ratio):^4d} % compression')
    
    return result, coding, compression_ratio

# LYRICS
plt.subplot(2, 1, 1)
plt.suptitle('Lab 7 - Rubalcava Analyzing Huffman')

MAX_N: int = int(128 * 3 / 2)

# PLOT 1
## POKEMON
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = LIKE_THE_MOVIES_LYRICS[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)

## JIGGLE JIGGLE
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = KILL_BILL_LYRICS[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)

## ALPHABET
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = MA_BELLE_EVANGELINE_LYRICS[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)

# PLOT 2
plt.subplot(2, 1, 2)

## SITH CODE
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = ANNE_FRANK[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)

## GREEN LATERN'S OATH
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = MULAN_1[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)

## JEDI CODE
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = MEX_INSP[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
