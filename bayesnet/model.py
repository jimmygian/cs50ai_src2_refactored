from pgmpy.models import BayesianNetwork # for defining the model
from pgmpy.factors.discrete.CPD import TabularCPD # for CPDs
from pgmpy.inference import VariableElimination  # for inference


# Bayesian Network pgmpy Documentation:
# https://pgmpy.org/models/bayesiannetwork.html


# 1. Define the Bayesian Network structure
model = BayesianNetwork([ # the model is a Bayesian Network
   ('rain', 'maintenance'), # the model has an edge from 'rain' to 'maintenance'
   ('rain', 'train'),      # the model has an edge from 'rain' to 'train'
   ('maintenance', 'train'), # the model has an edge from 'maintenance' to 'train'
   ('train', 'appointment') # the model has an edge from 'train' to 'appointment'
])

# 2. Define the CPDs (Conditional Probability Distributions)

# CPD for Rain (CPD means Conditional Probability Distribution) - although rain in this case is a discrete variable (unconditional)
cpd_rain = TabularCPD(variable='rain', variable_card=3,
                     values=[[0.7], [0.2], [0.1]],
                     state_names={'rain': ['none', 'light', 'heavy']})


# CPD for Maintenance given Rain (this is a conditional probability distribution - depends on the value of 'rain')
cpd_maintenance = TabularCPD(variable='maintenance', variable_card=2,
                            values=[[0.4, 0.2, 0.1], # P(maintenance='yes' | rain='none', light, heavy)
                                    [0.6, 0.8, 0.9]], # P(maintenance='no' | rain='none', light, heavy)
                            evidence=['rain'], # the evidence is the value of 'rain'
                            evidence_card=[3], # the evidence is a discrete variable with 3 possible values
                            state_names={'maintenance': ['yes', 'no'], # the state names for 'maintenance'
                                         'rain': ['none', 'light', 'heavy']}) # the state names for 'rain'


# CPD for Train given Rain and Maintenance
cpd_train = TabularCPD(variable='train', variable_card=2,
                      values=[[0.8, 0.9, 0.6, 0.7, 0.4, 0.5], # P(train='on time' | rain='none', light, heavy, maintenance='yes', 'no')
                              [0.2, 0.1, 0.4, 0.3, 0.6, 0.5]], # P(train='delayed' | rain='none', light, heavy, maintenance='yes', 'no')
                      evidence=['rain', 'maintenance'],
                      evidence_card=[3, 2], # the evidence is a discrete variable with 3 possible values for 'rain' and 2 possible values for 'maintenance'
                      state_names={'train': ['on time', 'delayed'],
                                   'rain': ['none', 'light', 'heavy'],
                                   'maintenance': ['yes', 'no']})


# CPD for Appointment given Train
cpd_appointment = TabularCPD(variable='appointment', variable_card=2,
                            values=[[0.9, 0.6], # P(appointment='attend' | train='on time', 'delayed')
                                    [0.1, 0.4]], # P(appointment='miss' | train='on time', 'delayed')
                            evidence=['train'],
                            evidence_card=[2], # the evidence is a discrete variable with 2 possible values for 'train'
                            state_names={'appointment': ['attend', 'miss'], # the state names for 'appointment' (state is a discrete variable and it means the value of the variable)
                                         'train': ['on time', 'delayed']}) # the state names for 'train'





# Add CPDs to the model (Create a Bayesian Network and add states)
model.add_cpds(cpd_rain, cpd_maintenance, cpd_train, cpd_appointment) # the model has 4 CPDs



if __name__ == "__main__":
    # Check if the model is valid
    assert model.check_model()

    nodes = model.nodes()
    edges = model.edges()
    print("=========")
    print("Nodes:", nodes)
    print("Edges:", edges)
    print()
    
    for node in nodes:
        print(model.get_cpds(node))

    print()
    print("Specific info (check & modify code to taste:)")
    print(model.get_markov_blanket("train")) # Check node's dependencies (parents)
    print(model.get_markov_blanket("appointment")) # Check node's dependencies (parents)
    print(model.get_state_probability({"rain": "none", "maintenance": "no", "train": "on time", "appointment": "attend"})) # Get probability given a folly specified Bayesian Network
    print("=========")