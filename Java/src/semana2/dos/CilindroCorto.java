import javax.swing.JOptionPane;

public class CilindroCorto {
    public static void main(String[] args) {
        do {
            double radio = Double.parseDouble(JOptionPane.showInputDialog("Radio del cilindro:"));
            double altura = Double.parseDouble(JOptionPane.showInputDialog("Altura del cilindro:"));
            double area = 2 * Math.PI * radio * altura + 2 * Math.PI * Math.pow(radio, 2);
            double volumen = Math.PI * Math.pow(radio, 2) * altura;
            String resultado = "Área: " + String.format("%.2f", area) + "\nVolumen: " + String.format("%.2f", volumen);
            JOptionPane.showMessageDialog(null, resultado, "Resultados Cilindro", JOptionPane.INFORMATION_MESSAGE);
            int continuar = JOptionPane.showConfirmDialog(null, "¿Calcular otro cilindro?", "Continuar", JOptionPane.YES_NO_OPTION);
            if (continuar != JOptionPane.YES_OPTION) break;
        } while (true);
        System.exit(0);
    }
}