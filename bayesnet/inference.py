from pgmpy.inference import VariableElimination
from model import model


# Create an inference object
inference = VariableElimination(model)

# Define the evidence
evidence = {'train': 'delayed'}
# evidence = {'train': 'delayed', 'rain': 'heavy'}

print("Knowing the evidence: ", evidence, " the probability of the following is: \n")

# Calculate predictions for each node given the evidence
predictions = {}
for node in model.nodes():
   if node in evidence:
       print(f"Node '{node}' is known to be '{evidence[node]}'.")
       print()
       continue

   # Query the probability distribution for each node given the evidence
   prediction = inference.query(variables=[node], evidence=evidence)
   print(prediction)
   print()


