package semana5.uno;

import java.util.Random;

import javax.swing.JOptionPane;

public class Ejercicio1 {

    public static void main(String[] args) {

        
        String [][] productos = {{"", ""},{"Smart phone", "300"},{"laptop ", "800"},{"Auriculares", "100"},{"televisor ", "500"},{"tablet ", "200"},
        {"Monitor led", "250"},{"Teclado  ", "70"},{"Cargador ", "40"},{"Pantalla tactil", "350"},{"Silla ergonómica ", "220"},
        {"Router WiFi ", "150"},{"Disco duro", "130"},{"Proyector", "300"}};

        int [] cantidades = new int [productos.length];
        double num1 =0;
        
        num1=Double.parseDouble(JOptionPane.showInputDialog(null, "Por favor digite su presupuesto inicial"));

        imprimirFactura(compraString(num1, productos, cantidades));
        

        
   }


   public static String compra(Double presupuesto, String [][] productos, int [] cantidades){
    String facturaString = "Producto \t Cantidad \t Precio \t Total\n";

    int precio;
        for (int i=0; i<productos.length; i++){
            
            do{

                precio = Integer.parseInt(productos[i][1]);
                cantidades[i] = Integer.parseInt(JOptionPane.showInputDialog(null, 
                "Por favor digite la cantidad del producto  "+productos[i][0]+" = $"+productos[i][1]+" \nSu presupuesto es de: "+presupuesto));
                presupuesto -= (precio * cantidades[i]);

                if(presupuesto < 0){
                    JOptionPane.showMessageDialog(null, "No tiene suficiente presupuesto para comprar este producto");
                }
                else{
                    facturaString += "   \n"+productos[i][0] + "\t " + cantidades[i] + "\t " + precio + "\t " + (precio * cantidades[i]) + "\n";
                }

            }while(presupuesto < 0);

        }



        return facturaString;
   }

   public static String compraString(Double presupuesto, String [][] productos, int [] cantidades){
    String nombre;
    nombre = JOptionPane.showInputDialog("Nombre del Cliente:");
    String facturaString = "Factura de compra\nCliente: " + nombre + "\n\nProducto  |  Cantidad  |  Precio  |  Subtotal ";
    

    double total = presupuesto;
    int precio;
    int i=1;
            
            do{
                i=Integer.parseInt(JOptionPane.showInputDialog("Por favor digite el número del producto que desea comprar: \n" +
                
                "1. Smart phone = $300 \n" +
                "2. laptop = $800 \n" +
                "3. Auriculares = $100 \n" +
                "4. televisor = $500 \n" +
                "5. tablet = $200 \n" +
                "6. Monitor led = $250 \n" +
                "7. Teclado = $70 \n" +
                "8. Cargador = $40 \n" +
                "9. Pantalla tactil = $350 \n" +
                "10. Silla ergonómica = $220 \n" +
                "11. Router WiFi = $150 \n" +
                "12. Disco duro = $130 \n" +
                "13. Proyector = $300 \n" +
                "0. Salir"));

                if (i==0){
                    break;
                }

                precio = Integer.parseInt(productos[i][1]);
                cantidades[i] = Integer.parseInt(JOptionPane.showInputDialog(null, 
                "Por favor digite la cantidad del producto  "+productos[i][0]+" = $"+productos[i][1]+" \nSu presupuesto es de: "+presupuesto));

                presupuesto = presupuesto-(precio * cantidades[i]);

                if(presupuesto <= 0){
                    JOptionPane.showMessageDialog(null, "No tiene suficiente presupuesto para comprar este producto");
                    presupuesto = presupuesto+(precio * cantidades[i]);
                    
                
                }
                else{
                   
                    facturaString += "   \n"+productos[i][0] + " | " + cantidades[i] + " | $" + precio + " | $" + (precio * cantidades[i]) + "\n";
                }

            }while(i!=0);

            total -= presupuesto;

            facturaString +=
            "\n" + "Total: $" + total + "\n" +
            "   \n"+ "IVA: $"+total*0.19+"\n"
            + "   \n"+ "Total + IVA: $"+total*1.19+"\n"
            + "   \n"+ "Descuento: $" + descuento(total) + "\n";

     
          

        return facturaString;
   }


   public static void imprimirFactura(String factura){
    JOptionPane.showMessageDialog(null, factura);
   }
   
   public static double descuento(double total){
    

    Random random = new Random();
    int descuento = random.nextInt(2);
    if (descuento==1){

            total*=0.5;
            JOptionPane.showMessageDialog(null, "felicitaciones ganó un descuento del 50% = $"+total);
            return total;        
    }
    
    else{
            JOptionPane.showMessageDialog(null, "no tiene descuento: \n");
    }

    return descuento;
   }

}
