import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  
  list = np.array(list).reshape((3,3))
  
  calculations = {}
  
  calculations["mean"] = [list.mean(axis =  0).tolist(), list.mean(axis = 1).tolist(), list.mean()]
  calculations["variance"] = [list.var(axis =  0).tolist(), list.var(axis = 1).tolist(), list.var()]
  calculations["standard deviation"] = [list.std(axis =  0).tolist(), list.std(axis = 1).tolist(), list.std()]
  calculations["max"] = [list.max(axis =  0).tolist(), list.max(axis = 1).tolist(), list.max()]
  calculations["min"] = [list.min(axis =  0).tolist(), list.min(axis = 1).tolist(), list.min()]
  calculations["sum"] = [list.sum(axis =  0).tolist(), list.sum(axis = 1).tolist(), list.sum()]
  
  return calculations
