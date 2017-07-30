class LexiconFun(object):
    def __init__(self):
       
        self.direction_words = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
        self.verbs = ['go', 'stop', 'kill', 'eat']
        self.stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
        self.nouns = ['door', 'bear', 'princess', 'cabinet']

    def convert_number(self, text):
        try:
            return int(text)
        except ValueError:
            return None


def scan(line):
    print "Scanning line '%s'" % line
    the_lexicon = LexiconC()
    ret_val = []
    words = line.split()
    for word in words:
        the_tuple = the_lexicon.get_tuple(word)
        ret_val.append(the_tuple)

    return ret_val