import numpy as np
from qutip import Bloch, Qobj
from check_qutip_installed import check_qutip_installed
import matplotlib.pyplot as plt

class State:
    def __init__(self, statevector):
        self.statevector = np.array(statevector)
        if len(self.statevector) != 2:
            raise ValueError("The state is not a single qubit state.")    
    def get_bloch_vector(self):
        state = Qobj(self.statevector)
        return [
            np.real(state[1, 0] * np.conjugate(state[0, 0])),
            np.imag(state[1, 0] * np.conjugate(state[0, 0])),
            np.real(state[0, 0] * np.conjugate(state[0, 0])) - np.real(state[1, 0] * np.conjugate(state[1, 0]))
        ]
    
def add_states_to_bloch_sphere(states, bloch_sphere=None):
    check_qutip_installed()
    bloch_sphere = bloch_sphere or Bloch()
    for state in states:
        bloch_sphere.add_vectors(state.get_bloch_vector())
    return bloch_sphere

def show(*bloch_spheres):
    n = len(bloch_spheres)
    if n == 0:
        raise ValueError("No Bloch spheres to show.")
    
    fig, axes = plt.subplots(1, n, subplot_kw={'projection': '3d'}, figsize=(5 * n, 5))
    
    if n == 1:
        bloch_spheres[0].fig = fig
        bloch_spheres[0].axes = axes
        bloch_spheres[0].render()
    else:
        for i, bloch_sphere in enumerate(bloch_spheres):
            bloch_sphere.fig = fig
            bloch_sphere.axes = axes[i]
            bloch_sphere.render()

    plt.show()

