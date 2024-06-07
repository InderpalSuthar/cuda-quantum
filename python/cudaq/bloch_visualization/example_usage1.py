# example_usage.py
# single_bloch

import sys
import os
sys.path.append('python/cudaq/bloch_visualization')

from add_to_bloch_sphere import State,show


# Define some example states
state1 = State([1, 0])  # |0> state
# Create Bloch sphere and add states
bloch_sphere = state1.add_to_bloch_sphere()

# Show the Bloch sphere
show(bloch_sphere)
