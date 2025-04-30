import javax.swing.JOptionPane;

public class contadorparimpar {
    public static void main(String[] args) {
        int n = Integer.parseInt(JOptionPane.showInputDialog("¿Cuántos números vas a ingresar?"));
        int paresCount = 0;
        int imparesCount = 0;
        String resultados = ""; // To store results for display

        for (int i = 0; i < n; i++) {
            int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingresa el número " + (i + 1) + ":"));
            String tipo = (numero % 2 == 0) ? "PAR" : "IMPAR";
            resultados += "Número " + numero + " es " + tipo + "\n"; // Add result to string
            if (tipo.equals("PAR")) {
                paresCount++;
            } else {
                imparesCount++;
            }
        }

        resultados += "\n--- Conteo Final ---" +
                      "\nNúmeros PARES: " + paresCount +
                      "\nNúmeros IMPARES: " + imparesCount;

        JOptionPane.showMessageDialog(null, resultados, "Resultados Pares/Impares", JOptionPane.INFORMATION_MESSAGE);
        System.exit(0);
    }
}