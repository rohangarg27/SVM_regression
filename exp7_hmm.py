""" Experiment 7: Hidden Markov Model (HMM) for Sequential Data """
import numpy as np

# Simple HMM Implementation using probabilities (manual demonstration)
states = ('Sunny', 'Rainy')
observations = ('Walk', 'Shop', 'Clean')

# Transition and emission probabilities
transition_probs = {
    'Sunny': {'Sunny': 0.8, 'Rainy': 0.2},
    'Rainy': {'Sunny': 0.4, 'Rainy': 0.6}
}

emission_probs = {
    'Sunny': {'Walk': 0.6, 'Shop': 0.3, 'Clean': 0.1},
    'Rainy': {'Walk': 0.1, 'Shop': 0.4, 'Clean': 0.5}
}

print("Transition Probabilities:", transition_probs)
print("Emission Probabilities:", emission_probs)
