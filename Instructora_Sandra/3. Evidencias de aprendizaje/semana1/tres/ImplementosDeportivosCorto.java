import javax.swing.JOptionPane;

public class ImplementosDeportivosCorto {
    public static void main(String[] args) {
        do {
            String deporte = JOptionPane.showInputDialog("Seleccione un deporte:\n1. Fútbol\n2. Baloncesto\n3. Tenis\n4. Natación\n5. Atletismo");
            String implementos = "";
            switch (deporte) {
                case "1": implementos = "Balón de fútbol\nRopa deportiva\nZapatos deportivos"; break;
                case "2": implementos = "Balón de baloncesto\nRopa deportiva\nZapatos deportivos"; break;
                case "3": implementos = "Raqueta de tenis\nPelotas de tenis\nRopa deportiva\nZapatos deportivos"; break;
                case "4": implementos = "Traje de baño\nGafas de natación\nGorro de natación"; break;
                case "5": implementos = "Ropa deportiva\nZapatos deportivos para correr"; break;
                default: implementos = "Deporte no válido.";
            }
            JOptionPane.showMessageDialog(null, "Implementos deportivos para:\n" + getDeporteNombre(deporte) + "\n\n" + implementos);
            int continuar = JOptionPane.showConfirmDialog(null, "¿Consultar otro deporte?", "Continuar", JOptionPane.YES_NO_OPTION);
            if (continuar != JOptionPane.YES_OPTION) break;
        } while (true);
        System.exit(0);
    }

    static String getDeporteNombre(String deporteOpcion) {
        switch (deporteOpcion) {
            case "1": return "Fútbol";
            case "2": return "Baloncesto";
            case "3": return "Tenis";
            case "4": return "Natación";
            case "5": return "Atletismo";
            default: return "Opción seleccionada";
        }
    }
}