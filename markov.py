"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.
    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    return open(file_path).read()



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.
    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.
    For example:
        >>> chains = make_chains('hi there mary hi there juanita')
    Each bigram (except the last) will be a key in chains:
        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]
    Each item in chains is a list of all possible following words:
        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    new_list = text_string.split() # take the string input and convert it to a list split on any whitespace

    for i in range(len(new_list) -2):
        new_tuple = (new_list[i], new_list[i+1]) 
        if new_tuple in chains:
            chains[new_tuple].append(new_list[i+2])
        else:
            words_list =[new_list[i+2]] 
            chains[new_tuple]=words_list  
    
    return chains



def make_text(chains):
    """Return text from chains."""
    words = []
    # create a link bascially a seed for the function
    link = choice(list(chains.keys()))
# now add this link value to the words list
    words.extend(list(link)) # bc i think link is a tuple, so covert to a list then add to words
# using the link value as a key for the chains dictionary, now use random.choice to choose one of the values of the link key
    words.append(choice(chains[link])) # from the value for the link key, chose a random value and then add it to the words list
    while chains.get(link) != None:
    # now take the last 2 values of the list words and repeat
        link = (words[-2], words[-1]) # reassign link to the new seed values
        if chains.get(link) is None:
            break
        words.append(choice(chains[link])) # add a random value from the key:pair list to the words list
    return ' '.join(words)



input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)


print(random_text)
