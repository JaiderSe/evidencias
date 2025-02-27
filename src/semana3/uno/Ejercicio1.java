/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package semana3.uno;

import java.util.Random;
import javax.swing.JOptionPane;

/**   
 * 
 * 
 *
 * @author Ambiente
 */
public class Ejercicio1 {
    
    public static int  azul=0, rojo=0, magenta=0, gris=0, naranja=0, blanco=0, verde=0, amarillo=0;
    
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int estudiantes = 0;
        int balota=0;
        int resp=0;
    do{ 
        azul=0;
        rojo=0;
        magenta=0;
        gris=0;
        naranja=0;
        blanco=0;
        verde=0;
        amarillo=0;
        
        estudiantes = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el número de estudiantes: "));
            
    for(int i=0;i<estudiantes;i++){
        
        balota=numeroRandom();
        calcular(balota);
    }
    
    imprimir();
    
    
    resp = Integer.parseInt(JOptionPane.showInputDialog("Desea repetir el lanzamiento del dado? 1:si 2:no"));
                
     }while(resp == 1);
    }
    
    public static int numeroRandom(){
        int num1;
        num1=0;
        Random rand = new Random();
        
            num1=rand.nextInt(8);
        return num1;
    }
    
    public static void calcular(int num2){
        
        switch (num2){
            
                case 0:
                    JOptionPane.showMessageDialog(null, "el color es azul va para el servicio en la armada");
                    azul++;
                    break;
                case 1:
                    JOptionPane.showMessageDialog(null, "el color es rojo, va para el ejercito");
                    rojo++;
                    break;
                case 2:
                    JOptionPane.showMessageDialog(null, "el color es magenta, va para el imperio");
                    magenta++;
                    break;
                case 3:
                    JOptionPane.showMessageDialog(null, "el color es gris, va para la fuerza aerea");
                    gris++;
                    break;
                case 4:
                    JOptionPane.showMessageDialog(null, "el color es naranja, va para la policia");
                    naranja++;
                    break;
                case 5:
                    JOptionPane.showMessageDialog(null, "el color es blanco, va exonerado ");
                    blanco++;
                    break;
                case 6:
                    JOptionPane.showMessageDialog(null, "el color es verde, aplazado");
                    verde++;
                    break;
                case 7:
                    JOptionPane.showMessageDialog(null, "el color es Amarillo, se pospone problema de salud");
                    amarillo++;
                    break;
                    
        }
        
    }
     public static void imprimir (){
         
         JOptionPane.showMessageDialog(null,
            "\n Hay  " +amarillo +" Amarillos"
            +"\n Hay  " +rojo +" Rojos"
            +"\n Hay  " +azul +" Azules"
            +"\n Hay  " +magenta +" Magentas"
            +"\n Hay  " +gris +" Grises"
            +"\n Hay  " +naranja +" Naranjas"
            +"\n Hay  " +blanco +" Blancos"
            +"\n Hay  " +verde +" Verdes");
         
     }
}












    
    

