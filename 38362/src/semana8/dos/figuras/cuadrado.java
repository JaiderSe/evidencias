public class cuadrado extends figuras {
    
    private double lado;
    
    public cuadrado(double lado) {
        this.lado = lado;
    }
    
    @Override
    public double area() {
        return lado * lado;
    }
    
    @Override
    public double perimetro() {
        return 4 * lado;
    }
    
    @Override
    public String tipoFigura() {
        return "Cuadrado";
    }

}
