package semana4.tres;

import java.util.Random;

import javax.swing.JOptionPane;

public class Ejercicio4 {
        public static void main(String[] args) {
            // Declaración y creación de un array bidimensional de enteros de 3 filas y 4 columnas
            int num1;
            num1 =0;
            num1=personas();
            String matrizimpresa="";

            int[][] matriz = new int[num1][num1];
            String nombres [] = new String[num1];


            for (int i = 0; i < nombres.length; i++) {
                nombres[i] = JOptionPane.showInputDialog("Ingrese el nombre de la persona " + (i+1));
            }
            
            llenarMatriz(matriz);
            matrizimpresa=imprimirMatriz(matriz, nombres);
            // Impresión del array bidimensional
            System.out.println(matrizimpresa);
            JOptionPane.showMessageDialog(null, matrizimpresa);           
        }



public static int personas(){
            
            int num1;
            num1 = 0;

            num1=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el numero de personas"));

            return num1;
        }
        
public static void llenarMatriz(int mat[][]) {
 

    for (int i = 0; i < mat.length; i++) {
        for (int j = 0; j < mat[i].length; j++) {
           
            
            mat[i][j]=numeroRandom();
        }
    }
}

public static String imprimirMatriz(int mat[][], String nombres[]) {
     String matriz="";
    matriz+="Filas: "+ mat.length + "\nColumnas: "+mat[1].length + "\n";
    matriz+=repeatSpaces(25);
    for (int i = (mat.length-1); i >=0; i--) {
        matriz+=(nombres[i]+ repeatSpaces(20-(nombres[i].length())));
    }

    matriz+="\n";   

    for (int i = 0; i < mat.length ; i++)
    {
        matriz+=nombres[i]+ repeatSpaces(25-(nombres[i].length()));
        
        for (int j = 0; j < mat[i].length; j++) 
        {
            matriz+=("["+ mat[i][j] + "]"+repeatSpaces(15));
        }
        
        matriz+="\n";    
    }
                         
   
    return matriz;

}

public static String repeatSpaces(int count) {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < count; i++) {
        sb.append(" ");
    }
    return sb.toString();
}

public static int numeroRandom() {
    int num1;
    num1=0;
    Random rand = new Random();
    
        num1=rand.nextInt(2);
    return num1;
}
}