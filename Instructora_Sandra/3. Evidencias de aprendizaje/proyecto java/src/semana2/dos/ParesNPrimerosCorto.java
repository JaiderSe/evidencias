import javax.swing.JOptionPane;

public class ParesNPrimerosCorto {
    public static void main(String[] args) {
        do {
            int n = Integer.parseInt(JOptionPane.showInputDialog("Ingrese la cantidad de números pares a generar:"));
            int limite = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el valor final límite:"));
            String pares = "Primeros " + n + " números pares hasta " + limite + ":\n";
            int count = 0;
            for (int i = 0; count < n && i <= limite; i += 2) {
                pares += i + "\n";
                count++;
            }
            JOptionPane.showMessageDialog(null, pares);
            int continuar = JOptionPane.showConfirmDialog(null, "¿Generar otra secuencia?", "Continuar", JOptionPane.YES_NO_OPTION);
            if (continuar != JOptionPane.YES_OPTION) break;
        } while (true);
        System.exit(0);
    }
}