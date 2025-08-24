/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package actividad_2condicionales;

import java.util.Scanner;

/**
 *
 * @author JHONIER
 */
public class Actividad_2condicionales {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
         Scanner leer = new Scanner(System.in);
        
        System.out.println("ingrese su nombre : ");
        String nombre = leer.nextLine();
        
        System.out.println("ingrese su apellido : ");
         String apellido = leer.nextLine();
        
        System.out.println("ingrese su edad : ");
         int edad = leer.nextInt();
          
         leer.nextLine();
           System.out.print("Ingrese su sexo (masculino/femenino): ");
        String sexo = leer.nextLine();
         
         if (edad >= 18){
             System.out.println(nombre+ " "  + apellido +  " es mayor de edad ");
         }else{
             System.out.println(nombre+ " "  + apellido +  " es menor de edad ");
         }
         
       if (sexo.equalsIgnoreCase("masculino")){
           System.out.println("es un hombre");
       } else{
           System.out.println("es una mujer");
       }
    }
    
}

        // TODO code application logic here
    
    

