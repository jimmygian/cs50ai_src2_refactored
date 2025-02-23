from model import model


# Define the observation
observation = {
   "rain": "none",
   "maintenance": "no",
   "train": "on time",
   "appointment": "attend",
}

# Quick way:
print("Probability for observation: ", observation)
print(model.get_state_probability(observation))



# ========================== #

# VERBOSE EXAMPLE (check it to better understand the math)
# You can calculate the probability of something by multiplying the probabilities of each variable given its parents.

# 1. Access the values of the probabilities for each node, based on our prefered observation (as shown above)
probability_rain = model.get_cpds("rain")  # P(rain='none')
probability_maintenance = model.get_cpds("maintenance") # P(maintenance='no' | rain='none')
probability_train = model.get_cpds("train")  # P(train='on time' | rain='none', maintenance='no')
probability_appointment = model.get_cpds("appointment")  # P(appointment='miss' | train='on time')

rain_no = probability_rain.values[0]
maintenance_no = probability_maintenance.values[1][0]
train_ontime = probability_train.values[0][0][1]
appt_attend = probability_appointment.values[0][0]

# Calculate the joint probability by multiplying all individual probabilities
joint_probability = (
   float(rain_no)
   * float(maintenance_no)
   * float(train_ontime)
   * float(appt_attend)
)

# Print Results:
print()
print("========VERBOSE EXAMPLE=======")
# print(probability_rain)
print("P(no rain): ", rain_no)

# print(probability_maintenance)
print("P(no maintenance|no rain): ", maintenance_no)

# print(probability_train)
print("P(on time|no maintenance, no rain): ", train_ontime)

# print(probability_appointment)
print("P(attend|on time, no maintenance, no rain): ", appt_attend)

print()
print(f"{rain_no} * {maintenance_no} * {train_ontime} * {appt_attend} = {joint_probability}")
print("Joint Probability: ", joint_probability)
print("==============================")

