#Briyith Paola Prieto Salazar
#Prueba para postular a Intern Tech - TUL
#14/04/2023

def highestValuePalindrome (s,n,k, r=0):
  s = list (s) #Tomar s como lista

  if len(s) != n :
    print ("Longitud no válida, n = ", len(s))
    print ("Intente de nuevo.")
    return "-1"

  for i in range(n//2):
    lCount = n - i - 1    
    if s[i] != s[lCount]: #Validar igualdad en posiciones de la lista 
        if s[lCount] > s[i]:
            s[i] = s[lCount]
        else:
            s[i] = s[lCount]
        r += 1       
        if r > k :
           return "-1"         

  return "".join(s)


s = input('Ingresa el número "s": ')
n = int(input('¿Qué longitud tiene s?: '))
k = int(input('¿Cuántos cambios deseas que realice?: '))

if n > 100000 or n <= 0 : 
  print("Valor fuera de rango")
else:
  print(n, ' ', k, ' ', s, ' ')
  print(highestValuePalindrome(s,n,k))

if k < 0 or k > 100000 :
  print("Valor fuera de rango")
else:
  print(n, ' ', k, ' ', s, ' ')
  print(highestValuePalindrome(s,n,k))

