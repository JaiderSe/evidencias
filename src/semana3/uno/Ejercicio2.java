/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package semana3.uno;


import javax.swing.JOptionPane;

/**
 *
 * @author Ambiente
 */
public class Ejercicio2 {
    
     public static int  azul=0, rojo=0, magenta=0, gris=0, naranja=0, blanco=0, verde=0, amarillo=0;

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       
        
        int colornum = 0;
        int resp = 0;
        do {
            
            colornum = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el numero del color que desea consultar: "
                    + "\n1.rojo"
                    + "\n2.amarillo"
                    + "\n3.naranja"
                    + "\n4.verde"
                    + "\n5.azul"
                    + "\n6.morado"
                    + "\n7.negro"
                    + "\n8.blanco"
                    + ""));
            consultar(colornum);
            resp = Integer.parseInt(JOptionPane.showInputDialog("Desea repetir el lanzamiento del dado? 1:si 2:no"));

        } while (resp == 1);
    }
    

 
    
    public static void consultar(int colornum){
        
        switch (colornum){
            
                
                case 1:
                    JOptionPane.showMessageDialog(null, "Significado Positivo:\n Pasión, atrevimiento, importancia, fuerza, calor, energía, estimulación, masculinidad, excitación, exuberancia, osadía.");
                    JOptionPane.showMessageDialog(null, "Significado Negativo:\n Desafío, agresión, impacto, tensión.");
                    JOptionPane.showMessageDialog(null, "Observaciones:\n El rojo trae atención a textos e imágenes, así que úsalo como un color para estimular a las personas a tomar decisiones rápidas. Es un color perfecto para botones con Call-To-Actions como \"Comprar ahora\" o \"Hacer clic aquí\".");
                    
                    break;
                case 2:
                    JOptionPane.showMessageDialog(null, "Significado Positivo: \nFelicidad, amistad, advertencia, optimismo, caluroso, velocidad, amabilidad, autoestima, extroversión.");
                    JOptionPane.showMessageDialog(null, "Significado Negativo: \nAnsiedad, irracionalidad, fragilidad, miedo.");
                    JOptionPane.showMessageDialog(null, "Observaciones: \nEl amarillo evoca sentimientos agradables y alegres, así que puedes usarlo para promocionar productos infantiles y artículos relacionados con el ocio. Usualmente se percibe al amarillo como un color despreocupado e inestable, por lo que no se recomienda usarlo para vender productos de prestigio o caros: nadie compra un traje o un Mercedes Benz amarillo.");
                    break;
                case 3:
                    JOptionPane.showMessageDialog(null, "Significado Positivo: \nEnergía, vitalidad, diversión, seguridad, juguetón, calidez, confort, comida.");
                    JOptionPane.showMessageDialog(null, "Significado Negativo: \nPrivación, frustración, frivolidad, inmadurez.");
                    JOptionPane.showMessageDialog(null, "Observaciones: \nEl naranja es un color que da la sensación de calor, por lo que produce un efecto estimulante y es muy aceptado entre los jóvenes. Este color tiene una visibilidad muy alta, por lo que puedes usarlo para llamar la atención y promocionar productos alimenticios o juguetes.");
                    break;
                case 4:
                    JOptionPane.showMessageDialog(null, "Significado Positivo: \nNaturaleza, salud, paz, orgánico, equilibrio, restauración, conciencia, armonía.");
                    JOptionPane.showMessageDialog(null, "Significado Negativo: \nAburrimiento, estancamiento, enervación.");
                    JOptionPane.showMessageDialog(null, "Observaciones: \nEl verde tiene un gran poder curativo, el cual lo hace el color más relajante para el ojo humano; este sugiere estabilidad y resistencia. Usa el verde para indicar equilibrio en tus mensajes o promocionar productos 'verdes'.");
                    break;
                case 5:
                    JOptionPane.showMessageDialog(null, "Significado Positivo: \nInteligencia, confianza, seguridad, serenidad, comunicación, eficiencia, lógica, reflexión, calma.");
                    JOptionPane.showMessageDialog(null, "Significado Negativo: \nFrialdad, distanciamiento, falta emocional.");
                    JOptionPane.showMessageDialog(null, "Observaciones: \nEl azul es un color que se considera beneficioso para mente y cuerpo. Disminuye el metabolismo humano, produce un efecto calmante y emite seguridad. Varios bancos, hospitales y Facebook gustan usar del color azul para demostrar confianza a sus clientes. Además, puedes usar azul para promocionar productos o servicios relacionados con la limpieza, aerolíneas y agencias de viajes. Evita usarlo para promover comida, ya que el azul suprime el apetito.");
                    break;
                case 6:
                    JOptionPane.showMessageDialog(null, "Significado Positivo: \nLujo, misterio, creatividad, espiritualismo, visión, autenticidad, verdad.");
                    JOptionPane.showMessageDialog(null, "Significado Negativo: \nIntroversión, decadencia, supresión.");
                    JOptionPane.showMessageDialog(null, "Observaciones: \nEl morado está asociado con la realeza; representa la sabiduría, la imaginación, la locura, la creatividad, el misterio y la magia. Es una buena opción para un diseño femenino o una agencia de publicidad.");
                    break;
                case 7:
                    JOptionPane.showMessageDialog(null, "Significado Positivo: \nSofisticación, protección, elegancia, sustancia, glamour.");
                    JOptionPane.showMessageDialog(null, "Significado Negativo: \nOpresión, frialdad, amenaza, pesadez.");
                    JOptionPane.showMessageDialog(null, "Observaciones: \nEl negro es un color misterioso asociado con el miedo, lo desconocido y, por lo general, tiene una connotación negativa: lista negra, humor negro, muerte negra. De la misma forma, es un color elegante y prestigioso: corbata negra, Mercedes Benz negro. Un excelente color para marcas de lujo o moda.");
                    break;
                case 8:
                    JOptionPane.showMessageDialog(null, "Significado Positivo: \nVirtuoso, pureza, juventud, esterilidad, limpieza, simplicidad, sofisticación, claridad.");
                    JOptionPane.showMessageDialog(null, "Significado Negativo: \nElitismo, esterilidad, frialdad, antipatía.");
                    JOptionPane.showMessageDialog(null, "Observaciones: \nEl blanco es considerado el color de la perfección, un nuevo comienzo y es el color representativo de la fe. Es un color apropiado para organizaciones caritativas o religiosas. El blanco se asocia con salud y esterilidad, por lo que puedes usarlo para dar seguridad al promocionar productos médicos, alimentos bajos en grasa y productos lácteos.");
                    break;
                    
        }
        
    }

}