import string
from automaton import Automaton


def get_validation(automaton, words):
        print '\nValidating words: ' + ', '.join(words) + '\n'

        for word in words:
            if automaton.validate(word):
                print 'Accept: {}'.format(word)
            else:
                print 'Reject: {}'.format(word)

def run():
    print '\nAutomaton 1: real numbers'
    automaton = Automaton('q1', {'q4'})

    automaton.add_state('q1', {'+':'q2', '-':'q2'})
    automaton.add_state('q1', {str(i):'q3' for i in range(0, 10)})

    automaton.add_state('q2', {str(i):'q3' for i in range(0, 10)})

    automaton.add_state('q3', {str(i):'q3' for i in range(0, 10)})
    automaton.add_state('q3', {'.':'q4'})

    automaton.add_state('q4', {str(i):'q4' for i in range(0, 10)})

    automaton.show_graph()

    words = ['1.0', '4.2', '4.', '56.9', '0.53', '0.55593', '4582580.99553', '+12.0', '-1548.844', '+4559.66', '-9984.98554455', '1..2', '1.55.5']
    get_validation(automaton, words)


    print '\nAutomaton 2: quoted text'
    automaton.clear_all_states()
    automaton.set_initial_state('q1')
    automaton.set_final_states({'q3'})

    automaton.add_state('q1', {'\"':'q2'})

    automaton.add_state('q2', {i:'q2' for i in string.ascii_lowercase})
    automaton.add_state('q2', {i:'q2' for i in string.ascii_uppercase})
    automaton.add_state('q2', {' ':'q2', '\"':'q3'})
    
    automaton.add_state('q3', {}) # even it is empty, it should be added

    automaton.show_graph()

    words = ['""', '"Maikel"', '"Maikel Maciel Ronnau"', 'Maikel', 'Maikel\"', '\"']
    get_validation(automaton, words)


    print '\nAutomaton 3: commented text in C style'
    automaton.clear_all_states()
    automaton.set_initial_state('q1')
    automaton.set_final_states({'q5'})

    automaton.add_state('q1', {'/':'q2'})

    automaton.add_state('q2', {'*':'q3'})

    automaton.add_state('q3', {i:'q3' for i in string.ascii_lowercase})
    automaton.add_state('q3', {i:'q3' for i in string.ascii_uppercase})
    automaton.add_state('q3', {' ':'q3', '*':'q4'})

    automaton.add_state('q4', {'/':'q5'})

    automaton.show_graph()

    words = ['/**/', '/*Maikel*/', '/* Maikel Maciel Ronnau */', '/*', '**', '/* Maikel *', '/* Maikel /']
    get_validation(automaton, words)


    print '\nAutomaton 4: integer numbers'
    automaton.clear_all_states()
    automaton.set_initial_state('q1')
    automaton.set_final_states({'q3'})

    automaton.add_state('q1', {'+':'q2', '-':'q2'})
    automaton.add_state('q1', {str(i):'q3' for i in range(0, 10)})

    automaton.add_state('q2', {str(i):'q3' for i in range(0, 10)})

    automaton.add_state('q3', {str(i):'q3' for i in range(0, 10)})

    automaton.show_graph()

    words = ['0', '0001', '123', '1249745', '+12', '-1548', '1.2', '+4559.66', '-9984.98554455']
    get_validation(automaton, words)


if __name__ == '__main__':
    run()
