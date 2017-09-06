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
    automaton = Automaton('q1', {'q4', 'q5'})

    automaton.add_state('q1', {'+':'q2', '-':'q2'})
    automaton.add_state('q1', {str(i):'q3' for i in range(0, 10)})
    automaton.add_state('q1', {i:'q5' for i in (string.ascii_lowercase + string.ascii_uppercase)}) 
    automaton.add_state('q1', {'/':'q6'})
    
    automaton.add_state('q2', {str(i):'q3' for i in range(0, 10)})

    automaton.add_state('q3', {str(i):'q3' for i in range(0, 10)})
    automaton.add_state('q3', {'.':'q4'})

    automaton.add_state('q4', {str(i):'q4' for i in range(0, 10)})

    automaton.add_state('q5', {i:'q5' for i in (string.ascii_lowercase + string.ascii_uppercase)})
    automaton.add_state('q5', {str(i):'q5' for i in range(0, 10)})
    automaton.add_state('q5', {'+':'q5', '-':'q5', '.':'q5', '/':'q5'})

    automaton.add_state('q6', {'/':'q5'})


if __name__ == '__main__':
    run()