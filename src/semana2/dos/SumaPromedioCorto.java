import javax.swing.JOptionPane;

public class SumaPromedioCorto {

    static int obtenerEnteroPositivo(String mensaje) {
        while (true) {
            try {
                int num = Integer.parseInt(JOptionPane.showInputDialog(mensaje));
                if (num > 0) return num;
                else JOptionPane.showMessageDialog(null, "Ingrese un número positivo.");
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "Ingrese un número entero válido.");
            }
        }
    }

    static String calcularSumaPromedio(int num1, int num2) {
        int suma = num1 + num2;
        double promedio = (double) suma / 2;
        return "Suma: " + suma + "\nPromedio: " + String.format("%.2f", promedio);
    }

    public static void main(String[] args) {
        do {
            int num1 = obtenerEnteroPositivo("Ingrese el primer número entero positivo:");
            int num2 = obtenerEnteroPositivo("Ingrese el segundo número entero positivo:");
            String resultados = calcularSumaPromedio(num1, num2);
            JOptionPane.showMessageDialog(null, resultados, "Resultados", JOptionPane.INFORMATION_MESSAGE);
            int continuar = JOptionPane.showConfirmDialog(null, "¿Calcular otra suma y promedio?", "Continuar", JOptionPane.YES_NO_OPTION);
            if (continuar != JOptionPane.YES_OPTION) break;
        } while (true);
        System.exit(0);
    }
}