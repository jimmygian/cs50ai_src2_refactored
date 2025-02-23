import numpy as np
from hmmlearn import hmm

def create_hmm():
    # Observation model for each state (emission probabilities)
    emission_prob = np.array([
        [0.2, 0.8],  # "umbrella", "no umbrella" for "sun"
        [0.9, 0.1]   # "umbrella", "no umbrella" for "rain"
    ])

    # Transition model
    transition_prob = np.array([
        [0.8, 0.2],  # "sun" to "sun", "sun" to "rain"
        [0.3, 0.7]   # "rain" to "sun", "rain" to "rain"
    ])

    # Starting probabilities
    start_prob = np.array([0.5, 0.5])

    # Create the Hidden Markov Model (discrete emissions)
    model = hmm.CategoricalHMM(n_components=2)  # 2 states: "sun" and "rain"

    # Set the parameters
    model.startprob_ = start_prob
    model.transmat_ = transition_prob
    model.emissionprob_ = emission_prob

    return model

if __name__ == "__main__":
    model = create_hmm()
    print("Model created successfully.")