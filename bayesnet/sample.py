from pgmpy.sampling import BayesianModelSampling
from collections import Counter
from model import model


# REJECTION SAMPLING EXAMPLE #

# Create a sampler object of our Bayesian model
sampler = BayesianModelSampling(model)

# Function to generate a sample
def generate_samples(num):
   # Generate samples of size num
   samples = sampler.forward_sample(size=num)
   # print(samples)
   return samples

N = 10000
samples = generate_samples(N)


# Access sample's data
samples_dict = samples.to_dict('records')

# Print the number of times appontment was 'attended' and 'missed'
data = []
for sample in samples_dict:
   if sample['train'] == "delayed":
       data.append(sample['appointment'])


# Count data and display resuly
print(Counter(data))