def assert_equals(a, b, precision=0.001):
  diff = abs(a - b)
  return diff <= precision