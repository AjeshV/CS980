from utils import argmax, vector_add, orientations, turn_right, turn_left

import random
import pandas as pd
class MDP:
    def __init__(self, init, actlist, terminals, transitions={}, states=None, gamma=.9):
        if not (0 < gamma <= 1):
            raise ValueError("")

        if states:
            self.states = states
        else:
            self.states = set()
        self.init = init
        self.actlist = actlist
        self.terminals = terminals
        self.transitions = transitions
        self.gamma = gamma
        self.reward = {}

    def R(self, state):
        return self.reward[state]

    def T(self, state, action):
        if(self.transitions == {}):
            raise ValueError("")
        else:
            return self.transitions[state][action]

    def actions(self, state):
        if state in self.terminals:
            return [None]
        else:
            return self.actlist

def value_iteration(mdp, epsilon=0.001):
    U1 = {s: 0 for s in mdp.states}
    R, T, gamma = mdp.R, mdp.T, mdp.gamma
    while True:
        U = U1.copy()
        delta = 0
        for s in mdp.states:
            U1[s] = R(s) + gamma * max([sum([p * U[s1] for (p, s1) in T(s, a)])
                                        for a in mdp.actions(s)])
            delta = max(delta, abs(U1[s] - U[s]))
        if delta < epsilon * (1 - gamma) / gamma:
            return U


__doc__ += """
>>> pi = best_policy(sequential_decision_environment, value_iteration(sequential_decision_environment, .01))
>>> sequential_decision_environment.to_arrows(pi)
[['>', '>', '>', '.'], ['^', None, '^', '.'], ['^', '>', '^', '<']]
>>> from utils import print_table
>>> print_table(sequential_decision_environment.to_arrows(pi))
>   >      >   .
^   None   ^   .
^   >      ^   <
>>> print_table(sequential_decision_environment.to_arrows(policy_iteration(sequential_decision_environment)))
>   >      >   .
^   None   ^   .
^   >      ^   <
"""  # noqa