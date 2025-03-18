import javax.swing.JOptionPane;

public class ComercianteCorto {
    public static void main(String[] args) {
        do {
            String producto = JOptionPane.showInputDialog("Producto:");
            double costo = Double.parseDouble(JOptionPane.showInputDialog("Costo:"));
            double ganancia = costo * 0.15;
            double precioVenta = costo + ganancia;
            JOptionPane.showMessageDialog(null, "Usted debe vender el producto a COP $" + String.format("%.0f", precioVenta) + " para obtener una ganancia del 15%");
            int continuar = JOptionPane.showConfirmDialog(null, "¿Consultar otro producto?", "Continuar", JOptionPane.YES_NO_OPTION);
            if (continuar != JOptionPane.YES_OPTION) break;
        } while (true);
        System.exit(0);
    }
}