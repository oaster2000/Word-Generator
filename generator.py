import random

C = ('s', 'z', 'v', 'f', 'm', 'n', 'p', 't', 'g')
V = ('a', 'i', 'o')

PATTERN = "(C)(C)(C)V(C)(C)"

def select_pattern(pattern):
    final_pattern = ""
    optional_flag = False
    for c in pattern:
        if(c == '('):
            optional_flag = True
            continue
        elif(c == ')'):
            continue
        
        if(optional_flag == False):
            final_pattern = ''.join((final_pattern, c))
        else:
            included = random.randint(0, 1)
            if(included == 1):
                final_pattern = ''.join((final_pattern, c))
            optional_flag = False
            
    return final_pattern
    
def select_phoneme(collection):
    return random.choice(collection)

def select_by_pattern(c, v, pattern):
    working_pattern = select_pattern(pattern)
    word = ""
    for char in working_pattern:
        if(char == 'C'):
            word = ''.join((word, select_phoneme(c)))
        elif(char == 'V'):
            word = ''.join((word, select_phoneme(v)))
    
    print(word)
    


def main():
    for i in range(random.randint(1, 20)):
        select_by_pattern(C, V, PATTERN)

if __name__ == "__main__":
    main()