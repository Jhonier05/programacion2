nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
edad =  int (input("ingrese su edad: "))
sexo = input("ingrese su sexo : femenino/masculino: ")

if edad >= 18:
     
     print (f"{nombre} {apellido} es mayor de edad")

else :
     
       print (f"{nombre} {apellido} es menor de edad")

if sexo.lower() == "masculino":
       
       print("es un hombre")
      
else :
      
      print("es mujer")