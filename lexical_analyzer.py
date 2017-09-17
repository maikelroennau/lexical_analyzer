from string import ascii_lowercase, ascii_uppercase
import sys

from automata import Automata


def get_validation(automata, words, primitives, identifiers):
    print '\nValidating words: ' + ', '.join(filter(None, words)) + '\n'

    symbols_table = {}
    error_list = []

    for i, word in enumerate(words):
        if word == '':
            continue

        result = automata.validate_identifier(word)
        
        if result is not False:
            if primitives[result] in identifiers:
                if word not in symbols_table.keys():
                    symbols_table[word] = len(symbols_table.keys())+1
            
            if word in symbols_table.keys():
                print '[{}] {} {}'.format(i+1, primitives[result], symbols_table[word])
            else:
                print '[{}] {}'.format(i+1, primitives[result])
        else:
            error_list.append(str(i+1))

    print '\nTable of symbols:'
    keys = symbols_table.keys()
    values = symbols_table.values()

    values, keys  = zip(*sorted(zip(values, keys)))

    for i in range(len(keys)):
        print '{} - {}'.format(values[i], keys[i])

    if len(error_list) > 0:
        print '\nThe program has erros in the lines: {}'.format(', '.join(error_list))

def validate_words(automata, words):
    print '\nValidating words: ' + ', '.join(words) + '\n'

    for i, word in enumerate(words):
        if automata.validate(word):
            print 'Accept[{}]: {}'.format(i + 1, word)
        else:
            print 'Reject[{}]: {}'.format(i + 1, word)

def read_text_file(path):
    with open(path, 'r') as file:
        return file.read().split('\n')

def get_numerals(state):
    return {str(i): state for i in range(0, 10)}


def get_alphabet(state):
    return {i: state for i in (ascii_lowercase + ascii_uppercase)}


def run():
    automata = Automata('q1', ['q3', 'q5', 'q7', 'q8'] + ['q{}'.format(i) for i in range(9, 41)])

    primitives = {'q3':'INTEGER NUMBER', 
                  'q5':'REAL NUMBER',
                  'q7':'COMMENT',
                  'q8':'IDENTIFIER',
                  'q9':'IDENTIFIER',
                  'q10':'INT',
                  'q11':'IDENTIFIER',
                  'q12':'IDENTIFIER',
                  'q13':'IDENTIFIER',
                  'q14':'FLOAT',
                  'q15':'IDENTIFIER',
                  'q16':'IDENTIFIER',
                  'q17':'REAL',
                  'q18':'IDENTIFIER',
                  'q19':'IDENTIFIER',
                  'q20':'IDENTIFIER',
                  'q21':'BREAK',
                  'q22':'IDENTIFIER',
                  'q23':'IDENTIFIER',
                  'q24':'CHAR',
                  'q25':'IDENTIFIER',
                  'q26':'IDENTIFIER',
                  'q27':'CASE',
                  'q28':'IDENTIFIER',
                  'q29':'IDENTIFIER',
                  'q30':'IDENTIFIER',
                  'q31':'IDENTIFIER',
                  'q32':'DOUBLE',
                  'q33':'IDENTIFIER',
                  'q34':'IDENTIFIER',
                  'q35':'CONST',
                  'q36':'IDENTIFIER',
                  'q37':'IDENTIFIER',
                  'q38':'IDENTIFIER',
                  'q39':'IDENTIFIER',
                  'q40':'CONTINUE'}
    
    identifiers = ['IDENTIFIER', 'INTEGER NUMBER', 'REAL NUMBER']

    automata.add_state('q1', {'+': 'q2', '-': 'q3'})
    automata.add_state('q1', get_numerals('q3'))
    automata.add_state('q1', {'/': 'q6'})
    automata.add_state('q1', get_alphabet('q8'))

    automata.add_state('q2', get_numerals('q3'))

    automata.add_state('q3', get_numerals('q3'))
    automata.add_state('q3', {'.': 'q4'})

    automata.add_state('q4', get_numerals('q5'))

    automata.add_state('q5', get_numerals('q5'))

    automata.add_state('q6', {'/': 'q7'})

    automata.add_state('q7', {'+': 'q7', '-': 'q7',
                               '/': 'q7', '.': 'q7', ' ': 'q7'})
    automata.add_state('q7', get_numerals('q7'))
    automata.add_state('q7', get_alphabet('q7'))

    automata.add_state('q8', {'n': 'q9', 'l': 'q11', 'e': 'q15', 'r': 'q18', 'h': 'q22', 'a': 'q25', 'o': 'q28'})
    automata.add_state('q8', { i:'q8' for i in list(set(get_alphabet('q8')) - set(automata.get_transitions_values('q8')))})
    automata.add_state('q8', get_numerals('q8'))
    
    automata.add_state('q9', {'t': 'q10'})
    automata.add_state('q9', { i:'q8' for i in list(set(get_alphabet('q9')) - set(automata.get_transitions_values('q9')))})

    automata.add_state('q10', get_numerals('q8'))
    automata.add_state('q10', get_alphabet('q8'))

    automata.add_state('q11', {'o': 'q12'})
    automata.add_state('q11', { i:'q8' for i in list(set(get_alphabet('q11')) - set(automata.get_transitions_values('q11')))})

    automata.add_state('q12', {'a': 'q13'})
    automata.add_state('q12', { i:'q8' for i in list(set(get_alphabet('q12')) - set(automata.get_transitions_values('q12')))})

    automata.add_state('q13', {'t': 'q14'})
    automata.add_state('q13', { i:'q8' for i in list(set(get_alphabet('q13')) - set(automata.get_transitions_values('q13')))})

    automata.add_state('q14', get_numerals('q8'))
    automata.add_state('q14', get_alphabet('q8'))

    automata.add_state('q15', {'a': 'q16'})
    automata.add_state('q15', { i:'q8' for i in list(set(get_alphabet('q15')) - set(automata.get_transitions_values('q15')))})

    automata.add_state('q16', {'l': 'q17'})
    automata.add_state('q16', { i:'q8' for i in list(set(get_alphabet('q16')) - set(automata.get_transitions_values('q16')))})

    automata.add_state('q17', get_numerals('q8'))
    automata.add_state('q17', get_alphabet('q8'))

    automata.add_state('q18', {'e': 'q19'})
    automata.add_state('q18', { i:'q8' for i in list(set(get_alphabet('q18')) - set(automata.get_transitions_values('q18')))})

    automata.add_state('q19', {'a': 'q20'})
    automata.add_state('q19', { i:'q8' for i in list(set(get_alphabet('q19')) - set(automata.get_transitions_values('q19')))})

    automata.add_state('q20', {'k': 'q21'})
    automata.add_state('q20', { i:'q8' for i in list(set(get_alphabet('q20')) - set(automata.get_transitions_values('q20')))})

    automata.add_state('q21', get_numerals('q8'))
    automata.add_state('q21', get_alphabet('q8'))

    automata.add_state('q22', {'a': 'q23'})
    automata.add_state('q22', { i:'q8' for i in list(set(get_alphabet('q22')) - set(automata.get_transitions_values('q22')))})

    automata.add_state('q23', {'r': 'q24'})
    automata.add_state('q23', { i:'q8' for i in list(set(get_alphabet('q23')) - set(automata.get_transitions_values('q23')))})

    automata.add_state('q24', get_numerals('q8'))
    automata.add_state('q24', get_alphabet('q8'))

    automata.add_state('q25', {'s': 'q26'})
    automata.add_state('q25', { i:'q8' for i in list(set(get_alphabet('q25')) - set(automata.get_transitions_values('q25')))})

    automata.add_state('q26', {'e': 'q27'})
    automata.add_state('q26', { i:'q8' for i in list(set(get_alphabet('q26')) - set(automata.get_transitions_values('q26')))})

    automata.add_state('q27', get_numerals('q8'))
    automata.add_state('q27', get_alphabet('q8'))

    automata.add_state('q28', {'u': 'q29', 'n': 'q33'})
    automata.add_state('q28', { i:'q8' for i in list(set(get_alphabet('q28')) - set(automata.get_transitions_values('q28')))})

    automata.add_state('q29', {'b': 'q30'})
    automata.add_state('q29', { i:'q8' for i in list(set(get_alphabet('q29')) - set(automata.get_transitions_values('q29')))})

    automata.add_state('q30', {'l': 'q31'})
    automata.add_state('q30', { i:'q8' for i in list(set(get_alphabet('q30')) - set(automata.get_transitions_values('q30')))})

    automata.add_state('q31', {'e': 'q32'})
    automata.add_state('q31', { i:'q8' for i in list(set(get_alphabet('q31')) - set(automata.get_transitions_values('q31')))})

    automata.add_state('q32', get_numerals('q8'))
    automata.add_state('q32', get_alphabet('q8'))

    automata.add_state('q33', {'s': 'q34', 't': 'q36'})
    automata.add_state('q33', { i:'q8' for i in list(set(get_alphabet('q33')) - set(automata.get_transitions_values('q33')))})

    automata.add_state('q34', {'t': 'q35'})
    automata.add_state('q34', { i:'q8' for i in list(set(get_alphabet('q34')) - set(automata.get_transitions_values('q34')))})

    automata.add_state('q35', get_numerals('q8'))
    automata.add_state('q35', get_alphabet('q8'))

    automata.add_state('q36', {'i': 'q37'})
    automata.add_state('q36', { i:'q8' for i in list(set(get_alphabet('q36')) - set(automata.get_transitions_values('q36')))})

    automata.add_state('q37', {'n': 'q38'})
    automata.add_state('q37', { i:'q8' for i in list(set(get_alphabet('q37')) - set(automata.get_transitions_values('q37')))})

    automata.add_state('q38', {'u': 'q39'})
    automata.add_state('q38', { i:'q8' for i in list(set(get_alphabet('q38')) - set(automata.get_transitions_values('q38')))})

    automata.add_state('q39', {'e': 'q40'})
    automata.add_state('q39', { i:'q8' for i in list(set(get_alphabet('q39')) - set(automata.get_transitions_values('q39')))})

    automata.add_state('q40', get_numerals('q8'))
    automata.add_state('q40', get_alphabet('q8'))

    words = read_text_file(sys.argv[1])
    get_validation(automata, words, primitives, identifiers)

if __name__ == '__main__':
    run()
