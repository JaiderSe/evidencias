import javax.swing.JOptionPane;

public class ParesHastaNCorto {
    public static void main(String[] args) {
        int n = Integer.parseInt(JOptionPane.showInputDialog("Ingresa un número límite:"));
        String pares = "Números pares hasta " + n + ":\n";

        for (int i = 0; i <= n; i += 2) {
            pares += i + "\n";
        }

        JOptionPane.showMessageDialog(null, pares, "Números Pares", JOptionPane.INFORMATION_MESSAGE);
        System.exit(0);
    }
}