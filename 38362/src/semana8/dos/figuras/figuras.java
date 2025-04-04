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
        
    }
    public figuras() {
        // Constructor vacío
    }

    public abstract double perimetro();
    public abstract double area();
    public abstract String tipoFigura();


}
