def superDigit(n, k):
  
  def process_division(d):
    if len(d) < 2:
      return d

    mid = int(len(d) / 2)
    res1 = process_division( d[:mid] )
    res2 = process_division( d[mid:] )
    new_res = int(res1) + int(res2)
    if new_res > 9:
      return process_division( str(new_res) )
    
    return str(new_res)

  if len(n) == 1:
    return int(n)
  
  n = str( int(n) * k)

  mid = int(len(n) / 2)
  # for even length
  if len(n) % 2 == 0:
    res = int(process_division( n[:mid] )) + int(process_division( n[mid:] ))
  
  else:
    res = int(process_division( n[:mid] )) + int(n[mid]) + int(process_division( n[mid + 1:] ))

  if res > 9:
    res = int(process_division( str(res) ))
  
  # if k > 1:
  #   return superDigit(n * k, 1)
  
  return res

print(superDigit('148', 3))