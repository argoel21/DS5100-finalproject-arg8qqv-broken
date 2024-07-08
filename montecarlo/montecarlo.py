import numpy as np
import pandas as pd

class Die():
    def __init__(self, faces):
        if not isinstance(faces, np.ndarray):
            raise TypeError("Input faces should be a numpy array")
        weights = np.ones_like(faces, dtype=float)
        self.die_data = pd.DataFrame({'weights': weights}, index=faces)
    
    def play(self, rolls):
        results = self.die_data.sample(n=times, weights='weights', replace=True).index.tolist()
        return results
    
    def results(self, form = 'wide'):
        return self.die_data.copy()


class Game():
    def __init__(self):
        pass

class Analyzer():
    def __init__(self):
        pass``