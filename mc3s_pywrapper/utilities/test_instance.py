import numpy as np

def is_number(val):
  try:
    v = float(val)
    return True
  except ValueError:
    return False

def is_integer(val):
  return (isinstance(val,int) or isinstance(val,np.int8) or isinstance(val,np.int16) or 
          isinstance(val,np.int32) or isinstance(val,np.int64))

def is_positive_integer(val):
  if is_integer(val):
    return val >= 0
  else:
    return False

def is_positive_number(val):
  if is_number(val):
    return val >= 0
  else:
    return False

def is_probability(val):
  if is_number(val):
    # No restriction to g.t. 0 because sometimes we need to set negative values to make sure moves
    # aren't done (e.g. I've heard from Rob he needs to set -1 on Mira computer)
    return val <= 1.0
  else:
    return False

def is_boolean(val):
  return val in [True, False]