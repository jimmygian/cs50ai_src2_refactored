import numpy as np
from model import create_hmm

# Observed data
observations = [
    "umbrella",
    "umbrella",
    "no umbrella",
    "umbrella",
    "umbrella",
    "umbrella",
    "umbrella",
    "no umbrella",
    "no umbrella"
]

# Create the model
model = create_hmm()

# Map observations to numerical indices
observation_map = {"umbrella": 0, "no umbrella": 1}
observed_sequence = np.array([observation_map[obs] for obs in observations]).reshape(-1, 1)

# Perform inference (Viterbi algorithm)
logprob, state_sequence = model.decode(observed_sequence)

state_names = ["sun", "rain"]


# Print the predictions
print()
print("Observed Sequence (names):", observations)
print("\n")
print("Predicted State Sequence (names):")
for prediction in state_sequence:
    print(state_names[prediction])
print()