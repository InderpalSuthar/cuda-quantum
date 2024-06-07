# example_usage2.py
# multiple states in single bloch 

import sys
import os
import numpy as np
sys.path.append('python/cudaq/bloch_visualization')
from add_states_to_bloch_sphere import State,show,add_states_to_bloch_sphere

statevector1 = np.array([0,1])
statevector2=np.array([1,0])
statevector3=np.array([1/np.sqrt(2),1/np.sqrt(2)])
statevector4 = np.array([1/np.sqrt(2), 1/np.sqrt(2) * 1j])

# Create a State object
states1= State(statevector1)
states2= State(statevector2)
states3= State(statevector3)
states4= State(statevector4)

state_s=[states1,states2,states3,states4]
blochs=add_states_to_bloch_sphere(state_s)
show(blochs)


