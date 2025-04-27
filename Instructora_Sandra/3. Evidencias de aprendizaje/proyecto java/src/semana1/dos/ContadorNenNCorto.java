import javax.swing.JOptionPane;

public class ContadorNenNCorto {
    public static void main(String[] args) {
        do {
            int n = Integer.parseInt(JOptionPane.showInputDialog("Ingresa el valor del incremento (n):"));
            int valorFinal = Integer.parseInt(JOptionPane.showInputDialog("Ingresa el valor final:"));

            String conteo = "Conteo de " + n + " en " + n + " hasta " + valorFinal + ":\n";

            for (int i = 0; i <= valorFinal; i += n) {
                conteo += i + "\n";
            }

            JOptionPane.showMessageDialog(null, conteo, "Conteo", JOptionPane.INFORMATION_MESSAGE);

            int continuar = JOptionPane.showConfirmDialog(null, "¿Desea realizar otro conteo?", "Continuar", JOptionPane.YES_NO_OPTION);
            if (continuar != JOptionPane.YES_OPTION) {
                break; 
            }
        } while (true);
        System.exit(0); 
    }
}