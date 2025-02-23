from pgmpy.models import MarkovChain as MC


# Choose Number of Samples
SAMPLE_SIZE = 50

# Init Markov Chain model
model = MC()

# Add variable (weather which has 2 possible values: 0 (sun) and 1 (rain))
model.add_variables_from(['weather'], [2])

# Create transition model
tm = {
    0: {0: 0.8, 1: 0.2}, #  sun: {sun, rain}
    1: {0: 0.3, 1: 0.7}  # rain: {sun, rain}
}
model.add_transition_model('weather', tm)

# Choose a starting state randomly
random_start_state = model.random_state()

# Do sampling
generated_sample = model.generate_sample(start_state=random_start_state, size=SAMPLE_SIZE)
# sample = model.sample(start_state=random_start_state, size=SAMPLE_SIZE)


# Examine sample
rain, sun, chain = 0, 0, []
for sample in generated_sample:
    current_sample = sample[0][1]

    if current_sample == 0:
        sun+=1
        chain.append("sun")
    elif current_sample == 1:
        rain+=1
        chain.append("rain")
    
    
print(chain)

