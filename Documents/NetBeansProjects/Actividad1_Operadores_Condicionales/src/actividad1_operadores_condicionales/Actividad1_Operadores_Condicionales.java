/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */


package actividad1_operadores_condicionales;

/**
 *
 * @author JHONIER
 */

import java.util.Scanner;

public class Actividad1_Operadores_Condicionales {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

    System.out.println("ingrese la nita 1");
    double nota1 = leer.nextDouble();

    System.out.println("ingrese la nita 2");
    double nota2 = leer.nextDouble();

    System.out.println("ingrese la nita 3");
    double nota3 = leer.nextDouble();

    double p1 = nota1 * 0.30;
    double p2 = nota2 * 0.30;
    double p3 = nota3 * 0.40;

    double nf = p1 + p2 + p3;

    System.out.println("la nota final es " + nf);

    if (nf >= 1 && nf <= 1.9) {
        System.out.println("la nota es deficiente");
    } else if (nf >= 2 && nf <= 2.9) {
        System.out.println("la nota es insuficiente");
    } else if (nf >= 3 && nf <= 3.9) {
        System.out.println("la nota es aprobada");
    } else if (nf >= 4 && nf <= 5) {
        System.out.println("la nota es destacada");
    }

        // TODO code application logic here
    }
    
}
