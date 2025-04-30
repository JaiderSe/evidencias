import javax.swing.JOptionPane;

public class JardinBotanicoGrupoCorto {
    public static void main(String[] args) {
        int numPersonas = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el número de personas en su grupo:"));
        int ultimoViernes = JOptionPane.showConfirmDialog(null, "¿Es el último viernes del mes?", "¿Último Viernes?", JOptionPane.YES_NO_OPTION);
        double valorTotal = 0;

        for (int i = 0; i < numPersonas; i++) {
            int edad = Integer.parseInt(JOptionPane.showInputDialog("Ingrese la edad de la persona " + (i + 1) + ":"));
            double valorEntradaPersona = 0;
            if (ultimoViernes == JOptionPane.YES_OPTION) {
                valorEntradaPersona = 0;
            } else if (edad < 5 || edad > 59) {
                valorEntradaPersona = 0;
            } else {
                valorEntradaPersona = 6000;
            }
            valorTotal += valorEntradaPersona;
        }

        JOptionPane.showMessageDialog(null, "Valor total a pagar para el grupo: COP $" + String.format("%.0f", valorTotal));
        System.exit(0);
    }
}