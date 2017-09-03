class Automaton:

    def __init__(self, initial_state, final_states):
        self.graph = {}
        self.initial_state = initial_state
        self.final_states = final_states

    def add_state(self, key, value):
        if self.graph.has_key(key):
            self.graph[key].update(value)
        else:
            self.graph[key] = value

    def validate(self, word):
        state = self.initial_state

        for letter in word:
            try:
                state = self.graph[state][letter]
            except KeyError:
                return False

        return state in self.final_states
        

    def show_graph(self):
        for key in self.graph.keys():
            print '{} : {}'.format(key, self.graph[key])


if __name__ == '__main__':
    pass