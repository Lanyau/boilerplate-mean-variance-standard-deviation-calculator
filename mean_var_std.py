import numpy as np


def calculate(input_list):
     """Calculate mean, variance, standard deviation, max, min and sum

     Args:
          input_list (list): list of 9 numbers

     Returns:
          dict: dictionary with the required calculations in the shape expected by the tests
     """
     if len(input_list) != 9:
          raise ValueError("List must contain nine numbers.")

     n = np.array(input_list).reshape(3, 3)

     calculations = {
          'mean': [n.mean(axis=0).tolist(), n.mean(axis=1).tolist(), n.mean().tolist()],
          'variance': [n.var(axis=0).tolist(), n.var(axis=1).tolist(), n.var().tolist()],
          'standard deviation': [n.std(axis=0).tolist(), n.std(axis=1).tolist(), n.std().tolist()],
          'max': [n.max(axis=0).tolist(), n.max(axis=1).tolist(), n.max().tolist()],
          'min': [n.min(axis=0).tolist(), n.min(axis=1).tolist(), n.min().tolist()],
          'sum': [n.sum(axis=0).tolist(), n.sum(axis=1).tolist(), n.sum().tolist()]
     }

     return calculations