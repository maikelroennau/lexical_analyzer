import string
from automata import Automata


def get_validation(automata, words):
        print '\nValidating words: ' + ', '.join(words) + '\n'

        for word in words:
            if automata.validate(word):
                print 'Accept: {}'.format(word)
            else:
                print 'Reject: {}'.format(word)

def run():
    print '\nAutomata 1: real numbers'
    automata = Automata('q1', {'q4'})

    automata.add_state('q1', {'+':'q2', '-':'q2'})
    automata.add_state('q1', {str(i):'q3' for i in range(0, 10)})

    automata.add_state('q2', {str(i):'q3' for i in range(0, 10)})

    automata.add_state('q3', {str(i):'q3' for i in range(0, 10)})
    automata.add_state('q3', {'.':'q4'})

    automata.add_state('q4', {str(i):'q4' for i in range(0, 10)})

    automata.show_graph()

    words = ['1.0', '4.2', '4.', '56.9', '0.53', '0.55593', '4582580.99553', '+12.0', '-1548.844', '+4559.66', '-9984.98554455', '1..2', '1.55.5']
    get_validation(automata, words)


    print '\nAutomata 2: quoted text'
    automata.clear_all_states()
    automata.set_initial_state('q1')
    automata.set_final_states({'q3'})

    automata.add_state('q1', {'\"':'q2'})

    automata.add_state('q2', {i:'q2' for i in (string.ascii_lowercase + string.ascii_uppercase)})
    automata.add_state('q2', {' ':'q2', '\"':'q3'})
    
    automata.add_state('q3', {}) # even it is empty, it should be added

    automata.show_graph()

    words = ['""', '"Maikel"', '"Maikel Maciel Ronnau"', 'Maikel', 'Maikel\"', '\"']
    get_validation(automata, words)


    print '\nAutomata 3: commented text in C style'
    automata.clear_all_states()
    automata.set_initial_state('q1')
    automata.set_final_states({'q5'})

    automata.add_state('q1', {'/':'q2'})

    automata.add_state('q2', {'*':'q3'})

    automata.add_state('q3', {i:'q3' for i in (string.ascii_lowercase + string.ascii_uppercase)})
    automata.add_state('q3', {' ':'q3', '*':'q4'})

    automata.add_state('q4', {'/':'q5'})

    automata.show_graph()

    words = ['/**/', '/*Maikel*/', '/* Maikel Maciel Ronnau */', '/*', '**', '/* Maikel *', '/* Maikel /']
    get_validation(automata, words)


    print '\nAutomata 4: integer numbers'
    automata.clear_all_states()
    automata.set_initial_state('q1')
    automata.set_final_states({'q3'})

    automata.add_state('q1', {'+':'q2', '-':'q2'})
    automata.add_state('q1', {str(i):'q3' for i in range(0, 10)})

    automata.add_state('q2', {str(i):'q3' for i in range(0, 10)})

    automata.add_state('q3', {str(i):'q3' for i in range(0, 10)})

    automata.show_graph()

    words = ['0', '0001', '123', '1249745', '+12', '-1548', '1.2', '+4559.66', '-9984.98554455']
    get_validation(automata, words)


if __name__ == '__main__':
    run()
