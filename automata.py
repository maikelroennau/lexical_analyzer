class Automata:

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

    def validate_identifier(self, word):
        state = self.initial_state

        for letter in word:
            try:
                state = self.graph[state][letter]
            except KeyError:
                return False

        if state in self.final_states:
            return state
        else:
            return False
            
    def get_transitions(self, state):
        if state in self.graph.keys():
            return self.graph[state]

    def get_transitions_values(self, state):
        if state in self.graph.keys():
            return self.graph[state].keys()

    def set_initial_state(self, state):
        self.initial_state = state

    def get_initial_state(self):
        return self.initial_state

    def set_final_states(self, states):
        self.final_states = states

    def get_final_states(self):
        return self.final_states

    def clear_all_states(self):
        self.graph.clear()

    def show_graph(self):
        for key in self.graph.keys():
            print '{} : {}'.format(key, self.graph[key])


if __name__ == '__main__':
    pass
