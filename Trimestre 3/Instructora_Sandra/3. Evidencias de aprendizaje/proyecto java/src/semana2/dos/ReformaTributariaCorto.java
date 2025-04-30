import javax.swing.JOptionPane;

public class ReformaTributariaCorto {
    public static void main(String[] args) {
        do {
            double monto = Double.parseDouble(JOptionPane.showInputDialog("Ingrese el monto del movimiento financiero:"));
            double impuesto = 0;
            if (monto >= 1000000) {
                impuesto = monto * 0.005;
            }
            JOptionPane.showMessageDialog(null, "Impuesto a pagar: COP $" + String.format("%.0f", impuesto));
            int continuar = JOptionPane.showConfirmDialog(null, "¿Calcular otro movimiento?", "Continuar", JOptionPane.YES_NO_OPTION);
            if (continuar != JOptionPane.YES_OPTION) break;
        } while (true);
        System.exit(0);
    }
}