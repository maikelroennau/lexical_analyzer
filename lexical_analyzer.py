from string import ascii_lowercase, ascii_uppercase

from automaton import Automaton


def get_validation(automaton, words, primitives, identifiers):
    print '\nValidating words: ' + ', '.join(words) + '\n'

    symbols_table = {}
    error_list = []

    for i, word in enumerate(words):
        result = automaton.validate_identifier(word)
        
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
    for i, symbol in enumerate(symbols_table.keys()):
        print '{} - {}'.format(i+1, symbol)

    if len(error_list) > 0:
        print '\nThe program has erros in the lines: {}'.format(', '.join(error_list))

def validate_words(automaton, words):
    print '\nValidating words: ' + ', '.join(words) + '\n'

    for i, word in enumerate(words):
        if automaton.validate(word):
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
    automaton = Automaton('q1', ['q3', 'q5', 'q7', 'q8'] + ['q{}'.format(i) for i in range(9, 41)])

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

    automaton.add_state('q1', {'+': 'q2', '-': 'q3'})
    automaton.add_state('q1', get_numerals('q3'))
    automaton.add_state('q1', {'/': 'q6'})
    automaton.add_state('q1', get_alphabet('q8'))

    automaton.add_state('q2', get_numerals('q3'))

    automaton.add_state('q3', get_numerals('q3'))
    automaton.add_state('q3', {'.': 'q4'})

    automaton.add_state('q4', get_numerals('q5'))

    automaton.add_state('q5', get_numerals('q5'))

    automaton.add_state('q6', {'/': 'q7'})

    automaton.add_state('q7', {'+': 'q7', '-': 'q7',
                               '/': 'q7', '.': 'q7', ' ': 'q7'})
    automaton.add_state('q7', get_numerals('q7'))
    automaton.add_state('q7', get_alphabet('q7'))

    automaton.add_state('q8', {'n': 'q9', 'l': 'q11', 'e': 'q15', 'r': 'q18', 'h': 'q22', 'a': 'q25', 'o': 'q28'})
    automaton.add_state('q8', { i:'q8' for i in list(set(get_alphabet('q8')) - set(automaton.get_transitions_values('q8')))})
    automaton.add_state('q8', get_numerals('q8'))
    
    automaton.add_state('q9', {'t': 'q10'})
    automaton.add_state('q9', { i:'q8' for i in list(set(get_alphabet('q9')) - set(automaton.get_transitions_values('q9')))})

    automaton.add_state('q10', get_numerals('q8'))
    automaton.add_state('q10', get_alphabet('q8'))

    automaton.add_state('q11', {'o': 'q12'})
    automaton.add_state('q11', { i:'q8' for i in list(set(get_alphabet('q11')) - set(automaton.get_transitions_values('q11')))})

    automaton.add_state('q12', {'a': 'q13'})
    automaton.add_state('q12', { i:'q8' for i in list(set(get_alphabet('q12')) - set(automaton.get_transitions_values('q12')))})

    automaton.add_state('q13', {'t': 'q14'})
    automaton.add_state('q13', { i:'q8' for i in list(set(get_alphabet('q13')) - set(automaton.get_transitions_values('q13')))})

    automaton.add_state('q14', get_numerals('q8'))
    automaton.add_state('q14', get_alphabet('q8'))

    automaton.add_state('q15', {'a': 'q16'})
    automaton.add_state('q15', { i:'q8' for i in list(set(get_alphabet('q15')) - set(automaton.get_transitions_values('q15')))})

    automaton.add_state('q16', {'l': 'q17'})
    automaton.add_state('q16', { i:'q8' for i in list(set(get_alphabet('q16')) - set(automaton.get_transitions_values('q16')))})

    automaton.add_state('q17', get_numerals('q8'))
    automaton.add_state('q17', get_alphabet('q8'))

    automaton.add_state('q18', {'e': 'q19'})
    automaton.add_state('q18', { i:'q8' for i in list(set(get_alphabet('q18')) - set(automaton.get_transitions_values('q18')))})

    automaton.add_state('q19', {'a': 'q20'})
    automaton.add_state('q19', { i:'q8' for i in list(set(get_alphabet('q19')) - set(automaton.get_transitions_values('q19')))})

    automaton.add_state('q20', {'k': 'q21'})
    automaton.add_state('q20', { i:'q8' for i in list(set(get_alphabet('q20')) - set(automaton.get_transitions_values('q20')))})

    automaton.add_state('q21', get_numerals('q8'))
    automaton.add_state('q21', get_alphabet('q8'))

    automaton.add_state('q22', {'a': 'q23'})
    automaton.add_state('q22', { i:'q8' for i in list(set(get_alphabet('q22')) - set(automaton.get_transitions_values('q22')))})

    automaton.add_state('q23', {'r': 'q24'})
    automaton.add_state('q23', { i:'q8' for i in list(set(get_alphabet('q23')) - set(automaton.get_transitions_values('q23')))})

    automaton.add_state('q24', get_numerals('q8'))
    automaton.add_state('q24', get_alphabet('q8'))

    automaton.add_state('q25', {'s': 'q26'})
    automaton.add_state('q25', { i:'q8' for i in list(set(get_alphabet('q25')) - set(automaton.get_transitions_values('q25')))})

    automaton.add_state('q26', {'e': 'q27'})
    automaton.add_state('q26', { i:'q8' for i in list(set(get_alphabet('q26')) - set(automaton.get_transitions_values('q26')))})

    automaton.add_state('q27', get_numerals('q8'))
    automaton.add_state('q27', get_alphabet('q8'))

    automaton.add_state('q28', {'u': 'q29', 'n': 'q33'})
    automaton.add_state('q28', { i:'q8' for i in list(set(get_alphabet('q28')) - set(automaton.get_transitions_values('q28')))})

    automaton.add_state('q29', {'b': 'q30'})
    automaton.add_state('q29', { i:'q8' for i in list(set(get_alphabet('q29')) - set(automaton.get_transitions_values('q29')))})

    automaton.add_state('q30', {'l': 'q31'})
    automaton.add_state('q30', { i:'q8' for i in list(set(get_alphabet('q30')) - set(automaton.get_transitions_values('q30')))})

    automaton.add_state('q31', {'e': 'q32'})
    automaton.add_state('q31', { i:'q8' for i in list(set(get_alphabet('q31')) - set(automaton.get_transitions_values('q31')))})

    automaton.add_state('q32', get_numerals('q8'))
    automaton.add_state('q32', get_alphabet('q8'))

    automaton.add_state('q33', {'s': 'q34', 't': 'q36'})
    automaton.add_state('q33', { i:'q8' for i in list(set(get_alphabet('q33')) - set(automaton.get_transitions_values('q33')))})

    automaton.add_state('q34', {'t': 'q35'})
    automaton.add_state('q34', { i:'q8' for i in list(set(get_alphabet('q34')) - set(automaton.get_transitions_values('q34')))})

    automaton.add_state('q35', get_numerals('q8'))
    automaton.add_state('q35', get_alphabet('q8'))

    automaton.add_state('q36', {'i': 'q37'})
    automaton.add_state('q36', { i:'q8' for i in list(set(get_alphabet('q36')) - set(automaton.get_transitions_values('q36')))})

    automaton.add_state('q37', {'n': 'q38'})
    automaton.add_state('q37', { i:'q8' for i in list(set(get_alphabet('q37')) - set(automaton.get_transitions_values('q37')))})

    automaton.add_state('q38', {'u': 'q39'})
    automaton.add_state('q38', { i:'q8' for i in list(set(get_alphabet('q38')) - set(automaton.get_transitions_values('q38')))})

    automaton.add_state('q39', {'e': 'q40'})
    automaton.add_state('q39', { i:'q8' for i in list(set(get_alphabet('q39')) - set(automaton.get_transitions_values('q39')))})

    automaton.add_state('q40', get_numerals('q8'))
    automaton.add_state('q40', get_alphabet('q8'))

    words = filter(None, read_text_file('words.txt'))
    get_validation(automaton, words, primitives, identifiers)

if __name__ == '__main__':
    run()
