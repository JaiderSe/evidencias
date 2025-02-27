

import javax.swing.JOptionPane;

public class TiendaEnLineaCorto {
    public static void main(String[] args) {
        do {
            String producto = JOptionPane.showInputDialog("Producto:");
            double precio = Double.parseDouble(JOptionPane.showInputDialog("Precio del producto:"));
            String categoria = JOptionPane.showInputDialog("Categoría:\n1. Dispositivos móviles\n2. Accesorios y periféricos\n3. Entretenimiento y multimedia\n4. Domótica y hogares inteligentes\n5. Realidad virtual/aumentada\n6. Salud y bienestar\n7. Drones\n8. Carga y energía\n9. Hogar\n10. Computación");
            double descuentoPorcentaje = 0;

            switch (categoria) {
                case "1": case "5": descuentoPorcentaje = 7.5; break;
                case "2": descuentoPorcentaje = 12.5; break;
                case "3": descuentoPorcentaje = 2; break;
                case "4": descuentoPorcentaje = 10; break;
                case "6": descuentoPorcentaje = 20; break;
                case "7": descuentoPorcentaje = 19; break;
                case "8": descuentoPorcentaje = 35; break;
                case "9": descuentoPorcentaje = 25; break;
                case "10": descuentoPorcentaje = 40; break;
                default: JOptionPane.showMessageDialog(null, "Categoría no válida."); continue;
            }

            double valorDescuento = precio * (descuentoPorcentaje / 100);
            double totalPagar = precio - valorDescuento;

            String mensaje = "Precio del producto: $" + String.format("%.2f", precio) + "\n" +
                             "Porcentaje de descuento: " + String.format("%.2f", descuentoPorcentaje) + "%\n" +
                             "Valor descontado: $" + String.format("%.2f", valorDescuento) + "\n" +
                             "Total a pagar: $" + String.format("%.2f", totalPagar);
            JOptionPane.showMessageDialog(null, mensaje, "Precio Final", JOptionPane.INFORMATION_MESSAGE);

            int continuar = JOptionPane.showConfirmDialog(null, "¿Calcular otro producto?", "Continuar", JOptionPane.YES_NO_OPTION);
            if (continuar != JOptionPane.YES_OPTION) break;
        } while (true);
        System.exit(0);
    }
}