from automaton import Automaton

def run():
    automaton = Automaton('q1', {'q4'})

    automaton.add_state('q1', {'+':'q2', '-':'q2'})
    automaton.add_state('q1', {str(i):'q3' for i in range(0, 10)})

    automaton.add_state('q2', {str(i):'q3' for i in range(0, 10)})

    automaton.add_state('q3', {str(i):'q3' for i in range(0, 10)})
    automaton.add_state('q3', {'.':'q4'})

    automaton.add_state('q4', {str(i):'q4' for i in range(0, 10)})

    automaton.show_graph()

    print automaton.validate('1.0')
    print automaton.validate('4.2')
    print automaton.validate('56.9')
    print automaton.validate('0.53')
    print automaton.validate('0.55593')
    print automaton.validate('4582580.99553')

if __name__ == '__main__':
    run()
