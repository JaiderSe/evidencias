import javax.swing.JOptionPane;

public class DiasMesCorto {

    static int obtenerDiasDelMes(int mes) {
        switch (mes) {
            case 2: return 28;
            case 4: case 6: case 9: case 11: return 30;
            case 1: case 3: case 5: case 7: case 8: case 10: case 12: return 31;
            default: return -1;
        }
    }

    public static void main(String[] args) {
        do {
            try {
                int mes = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el número del mes (1-12):"));
                if (mes < 1 || mes > 12) {
                    JOptionPane.showMessageDialog(null, "Mes inválido. Ingrese un número entre 1 y 12.");
                    continue;
                }
                int dias = obtenerDiasDelMes(mes);
                JOptionPane.showMessageDialog(null, "El mes " + mes + " tiene " + dias + " días.");

            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "Entrada inválida. Ingrese un número entero.");
            }

            int continuar = JOptionPane.showConfirmDialog(null, "¿Consultar otro mes?", "Continuar", JOptionPane.YES_NO_OPTION);
            if (continuar != JOptionPane.YES_OPTION) break;

        } while (true);
        System.exit(0);
    }
}