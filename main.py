from automaton import Automaton

def run():
    automaton = Automaton('1', {'4'})

    automaton.add_state('1', {'d':'3', '+':'2', '-':'2'})
    automaton.add_state('2', {'d':'3'})
    automaton.add_state('3', {'d':'3', '.':'4'})
    automaton.add_state('4', {'d':'4'})

    automaton.show_graph()

    print automaton.validate('d.d')
    print automaton.validate('d.')
    print automaton.validate('dd.d')
    print automaton.validate('d.dd')

if __name__ == '__main__':
    run()
