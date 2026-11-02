# PART 1: Ask the agent for their details
name = input("Enter your real name, Agent : ")
gadget = input("Enter your favorite gadget : ")

# PART 2: Store the agent's details using different data types
agent_number = 7
speed_rating = 9.5
mission_count = 12
height_m = 1.65
is_active = True

# PART 3: Print each detail along with data type
print("Name : ", name, "-> type : ", type(name))
print("Gadget : ", gadget, "-> type : ", type(gadget))
print("Agent Number : ", agent_number, "-> type : ", type(agent_number))
print("Speed Rating : ", speed_rating, "-> type : ", type(speed_rating))
print("Mission Count : ", mission_count, "-> type : ", type(mission_count))
print("Height (m) : ", height_m, "-> type : ", type(height_m))
print("Is Active : ", is_active, "-> type : ", type(is_active))