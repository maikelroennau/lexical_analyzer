from string import ascii_lowercase, ascii_uppercase

from automaton import Automaton


def get_validation(automaton, words):
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
    automaton = Automaton('q1', {'q3', 'q5', 'q7', 'q8', 'q10', 'q14', 'q17', 'q21', 'q24', 'q27', 'q32', 'q35', 'q40'})

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
    automaton.add_state('q8', get_numerals('q8'))
    automaton.add_state('q8', get_alphabet('q8'))

    automaton.add_state('q9', {'t': 'q10'})

    automaton.add_state('q10', get_numerals('q8'))
    automaton.add_state('q10', get_alphabet('q8'))

    automaton.add_state('q11', {'o': 'q12'})

    automaton.add_state('q12', {'a': 'q13'})

    automaton.add_state('q13', {'t': 'q14'})

    automaton.add_state('q14', get_numerals('q8'))
    automaton.add_state('q14', get_alphabet('q8'))

    automaton.add_state('q15', {'a': 'q16'})

    automaton.add_state('q16', {'l': 'q17'})

    automaton.add_state('q17', get_numerals('q8'))
    automaton.add_state('q17', get_alphabet('q8'))

    automaton.add_state('q18', {'e': 'q19'})

    automaton.add_state('q19', {'a': 'q20'})

    automaton.add_state('q20', {'k': 'q21'})

    automaton.add_state('q21', get_numerals('q8'))
    automaton.add_state('q21', get_alphabet('q8'))

    automaton.add_state('q22', {'a': 'q23'})

    automaton.add_state('q23', {'r': 'q24'})

    automaton.add_state('q24', get_numerals('q8'))
    automaton.add_state('q24', get_alphabet('q8'))

    automaton.add_state('q25', {'s': 'q26'})

    automaton.add_state('q26', {'e': 'q27'})

    automaton.add_state('q27', get_numerals('q8'))
    automaton.add_state('q27', get_alphabet('q8'))

    automaton.add_state('q28', {'u': 'q29', 'n': '33'})

    automaton.add_state('q29', {'b': 'q30'})

    automaton.add_state('q30', {'l': 'q31'})

    automaton.add_state('q31', {'e': 'q32'})

    automaton.add_state('q32', get_numerals('q8'))
    automaton.add_state('q32', get_alphabet('q8'))

    automaton.add_state('q33', {'s': 'q34', 't': 'q36'})

    automaton.add_state('q34', {'t': 'q35'})

    automaton.add_state('q35', get_numerals('q8'))
    automaton.add_state('q35', get_alphabet('q8'))

    automaton.add_state('q36', {'i': 'q37'})

    automaton.add_state('q37', {'n': 'q38'})

    automaton.add_state('q38', {'u': 'q39'})

    automaton.add_state('q39', {'e': 'q40'})

    automaton.add_state('q40', get_numerals('q8'))
    automaton.add_state('q40', get_alphabet('q8'))

    print '\nAutomaton'
    automaton.show_graph()

    words = read_text_file('words.txt')
    get_validation(automaton, words)

    # Errors: 99., real a, double _c, as_asd, -- Teste, Tales Viegas --


if __name__ == '__main__':
    run()
