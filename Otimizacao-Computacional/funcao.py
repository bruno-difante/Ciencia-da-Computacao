def funcao(a, b, x0, x1):
  result = []
  
  for i in range(x0, x1 + 1):
    result.append((a * i) + b)
  return result

r = funcao(5, -11, -2, 5) #colocar os valores aqui  -> a, b, x0, x1
print(r)
