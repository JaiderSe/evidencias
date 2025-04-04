public class cilindro extends figuras {
    
    private double radio;
    private double altura;
    
    public cilindro(double radio, double altura) {
        this.radio = radio;
        this.altura = altura;
    }
    
    public double getRadio() {
        return radio;
    }

    public double getAltura() {
        return altura;
    }

    @Override
    public double area() {
        return 2 * Math.PI * radio * (radio + altura);
    }
    
    @Override
    public double perimetro() {
        return 2 * Math.PI * radio * altura;
    }
    
    @Override
    public String tipoFigura() {
        return "Cilindro";
    }

}
