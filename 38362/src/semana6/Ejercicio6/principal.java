package semana6.Ejercicio6;



public class Principal {
    public static void main(String[] args) {
         
            // Crear instancia con constructor por defecto
            Circulo circulo1 = new Circulo();
            
            circulo1.setRadio(4);
            System.out.println(circulo1);
            System.out.println("Área: " + circulo1.calcularArea());
            System.out.println("Perímetro: " + circulo1.calcularPerimetro());

            // Crear instancia con constructor por parámetros
            Circulo circulo2 = new Circulo(5.0);
            System.out.println(circulo2);
            System.out.println("Área: " + circulo2.calcularArea());
            System.out.println("Perímetro: " + circulo2.calcularPerimetro());

            // Cambiar el radio del primer círculo
            circulo1.setRadio(3.0);
            System.out.println("Nuevo radio de circulo1: " + circulo1.getRadio());
            System.out.println("Nueva área: " + circulo1.calcularArea());
            System.out.println("Nuevo perímetro: " + circulo1.calcularPerimetro());
        
    }
}
