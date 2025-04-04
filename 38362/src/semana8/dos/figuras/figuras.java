public abstract  class figuras {
    
    // protected double area = 0;
    // protected double perimetro = 0;

    public static void main(String[] args) {
        
        figuras figura = new triangulo(1, 1, 2, 3, 4);
        System.out.println("\nEl área del " + figura.tipoFigura() + " es: " + figura.area());
        System.out.println("\nEl perímetro del " + figura.tipoFigura() + " es: " + figura.perimetro());

        figuras figura2 = new cuadrado(5);
        System.out.println("\nEl área del " + figura2.tipoFigura() + " es: " + figura2.area());
        System.out.println("\nEl perímetro del " + figura2.tipoFigura() + " es: " + figura2.perimetro());
        
        figuras figura3 = new cilindro(5, 10);
        System.out.println("\nEl área del " + figura3.tipoFigura() + " es: " + figura3.area());
        System.out.println("\nEl perímetro del " + figura3.tipoFigura() + " es: " + figura3.perimetro());

        figuras figura4 = new circulo(5);
        System.out.println("\nEl área del " + figura4.tipoFigura() + " es: " + figura4.area());
        System.out.println("\nEl perímetro del " + figura4.tipoFigura() + " es: " + figura4.perimetro());

        figuras figura5 = new cilindro_hueco(5, 10, 2);
        System.out.println("\nEl área del " + figura5.tipoFigura() + " es: " + figura5.area());
        System.out.println("\nEl perímetro del " + figura5.tipoFigura() + " es: " + figura5.perimetro());

    }
    public figuras() {
        // Constructor vacío
    }

    public abstract double perimetro();
    public abstract double area();
    public abstract String tipoFigura();


}
