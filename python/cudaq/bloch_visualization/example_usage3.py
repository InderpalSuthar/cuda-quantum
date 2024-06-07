# example_usage.py
# mulitple bloch side by side

import sys
sys.path.append('python/cudaq/bloch_visualization')

from add_to_bloch_sphere import State,show
import numpy as np

statevector1 = np.array([0,1])
statevector2=np.array([1,0])
statevector3=np.array([1/np.sqrt(2),1/np.sqrt(2)])
statevector4 = np.array([1/np.sqrt(2), 1/np.sqrt(2) * 1j])

# Create a State object
states1= State(statevector1)
states2= State(statevector2)
states3= State(statevector3)
states4= State(statevector4)

# Plot on a Bloch sphere
bloch_sphere1= states1.add_to_bloch_sphere()
bloch_sphere2= states2.add_to_bloch_sphere()
bloch_sphere3= states3.add_to_bloch_sphere()
bloch_sphere4= states4.add_to_bloch_sphere()

# Display the Bloch sphere
show(bloch_sphere1,bloch_sphere2,bloch_sphere3,bloch_sphere4)