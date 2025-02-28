package semana3.dos;

import java.util.Random;
import javax.swing.JOptionPane;

public class Ejercicio1 {

    public static void main(String[] args) {
        
        
        // Crear una matriz de enteros de 6x2
        int[][] matriz = new int[6][2];
        int[][] matrizusuario = new int[6][2];
        int option = 0;
        int aciertos = 0;
        
        do{
        option= Integer.parseInt(JOptionPane.showInputDialog(null, "Por favor elija la modalidad que desea apostar: \n"
                + "1. Manual: usted escoge las balotas \n"
                + "2. Automático el sistema escoge por usted las balotas\n"
                + "3. Salir \n"));

        switch (option) {
            case 1:
                // Asignar valores a la matriz
                asignacion(matriz);
                adivinar(matrizusuario);
                aciertos = comparar(matriz, matrizusuario);
                imprimir(matrizusuario);
                imprimir(matriz);
                JOptionPane.showMessageDialog(null, "El número de aciertos es: " + aciertos);
                ganador(aciertos);
                break;

            case 2:
                asignacion(matriz);
                asignacion(matrizusuario);
                aciertos = comparar(matriz, matrizusuario);
                imprimir(matrizusuario);
                imprimir(matriz);
                JOptionPane.showMessageDialog(null, "El número de aciertos es: " + aciertos);
                ganador(aciertos);
                break;

            case 3:
                break;

            default:
                JOptionPane.showMessageDialog(null, "Digite una opción válida");
                break;
        }
        
        


        }while(option!=3);

        /* imprimir(matriz);
        imprimir(matrizusuario); */

  


         
    }
    
    public static void ganador(int aciertos){
    switch (aciertos) {
        case 3:
            JOptionPane.showMessageDialog(null, "Felicidades, ha ganado 1000 pesos");
            break;
        case 4:
            JOptionPane.showMessageDialog(null, "Felicidades, ha ganado 5000 pesos");
            break;
        case 5: 
            JOptionPane.showMessageDialog(null, "Felicidades, ha ganado 10000 pesos");
            break;  
        case 6:
            JOptionPane.showMessageDialog(null, "Felicidades, ha ganado 50000 pesos");
            break;      
            
    
        default:
            JOptionPane.showMessageDialog(null, "No ha ganado nada");
            break;
    }
}

    public static void imprimir(int [][] matriz){

        String colour;
        String conjuntobalotas = "";
        colour="";
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                

                switch (matriz[i][1]) {
                    case 0:
                        colour="Amarillo";
                        break;
                    case 1:
                        colour=("Azul");
                        break;
                    case 2:
                        colour=("Rojo");
                        break;
                    case 3:
                        colour=("Verde");
                        break;
                    case 4:
                        colour=("Blanco");
                        break;
                    case 5:
                        colour=("Negro");
                        break;

                
                }
                
            }
            conjuntobalotas+= "\nBalota "+(i+1)+" numero "+matriz[i][0]+" color :"+colour;
            
        }

        JOptionPane.showMessageDialog(null, conjuntobalotas);
}    

    public static void adivinar(int[][] matrizusuario) {
            for (int i = 0; i < matrizusuario.length; i++) {
                    for (int j = 0; j < matrizusuario[i].length; j++) {
                            boolean valorValido = false;

                            while (!valorValido) {
                                    if (j == 0) {
                                            int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el número de la balota numero " + (i + 1)));
                                            matrizusuario[i][j] = numero;
                                    } else {
                                            int color = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el color de la balota numero " + (i + 1) + "\n"
                                                            + "1. Amarillo\n"
                                                            + "2. Azul\n"
                                                            + "3. Rojo\n"
                                                            + "4. Verde\n"
                                                            + "5. Blanco\n"
                                                            + "6. Negro\n"));
                                            matrizusuario[i][j] = color;
                                    }

                                    valorValido = true;
                                    for (int k = 0; k < i; k++) {
                                            if (matrizusuario[k][0] == matrizusuario[i][0] && matrizusuario[k][1] == matrizusuario[i][1]) {
                                                    JOptionPane.showMessageDialog(null, "La combinación de número y color ya ha sido ingresada. Por favor, ingrese una combinación diferente.");
                                                    valorValido = false;
                                                    break;
                                            }
                                    }
                            }
                    }
            }
    }

    public static int comparar(int [][] matriz, int [][] matrizusuario){
    int aciertos = 0;
    int fallos = 0;
    
    for (int i = 0; i < matriz.length; i++) {
        for (int j = 0; j < matriz[i].length; j++) {
            if (matriz[i][j] == matrizusuario[i][j]) {
                aciertos++;
            } else {
                fallos++;
            }
        }
        }

     return aciertos;
}   

    public static void asignacion(int [][] matriz){

        Random rand = new Random();
        
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                matriz[i][j] = rand.nextInt(7);
         
          }
            
        
    }
 
}

}


