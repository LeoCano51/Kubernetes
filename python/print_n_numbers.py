try: 
  n = 10
  print("el numero seleccionado fue ", n)
  for x in range(n):
    print(x)
    
except ValueError:
  print("Error: no se puede convertir el parametro proporcionado")
