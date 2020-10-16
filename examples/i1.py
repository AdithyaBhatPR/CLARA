def computeDeriv(poly):
  new = []
  for i in range(1,len(poly)):
    new.append(
        (i*poly[i]))
  if new == 0:
    return [0.0]
  return new
