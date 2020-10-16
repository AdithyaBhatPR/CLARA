def computeDeriv(poly):
  result = []
  for i in poly:
    result[i]=float((i)*poly[i])
  return result
