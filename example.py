import scp

# Open the config file and putting into a variable
with open("example", "r") as f:
    raw = f.read()

# Create the parser object
config = scp.Parse(raw)

# Parse
config.parse()

# The data from the config file is now in a dict called "variables"
print(config.variables)

# Copying the data to python variables 
ex_string = config.variables["ex_string"]
ex_int = config.variables["ex_int"]
print(ex_string)
print(ex_int)