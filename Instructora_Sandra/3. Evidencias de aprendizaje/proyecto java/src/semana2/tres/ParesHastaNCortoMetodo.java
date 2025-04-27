import javax.swing.JOptionPane;

public class ParesHastaNCortoMetodo {

    static void imprimirParesHasta(int numero) {
        String pares = "Números pares hasta " + numero + ":\n";
        for (int i = 0; i <= numero; i += 2) {
            pares += i + "\n";
        }
        JOptionPane.showMessageDialog(null, pares);
    }

    public static void main(String[] args) {
        do {
            try {
                int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número entero positivo:"));
                if (numero >= 0) {
                    imprimirParesHasta(numero);
                } else {
                    JOptionPane.showMessageDialog(null, "Por favor, ingrese un número positivo.");
                }
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "Entrada inválida. Ingrese un número entero.");
            }
            int continuar = JOptionPane.showConfirmDialog(null, "¿Generar otra lista de pares?", "Continuar", JOptionPane.YES_NO_OPTION);
            if (continuar != JOptionPane.YES_OPTION) break;
        } while (true);
        System.exit(0);
    }
}