public class cilindro_hueco extends cilindro {
    
    private double radioInterno;
    
    public cilindro_hueco(double radio, double altura, double radioInterno) {
        super(radio, altura);
        this.radioInterno = radioInterno;
    }
    
    @Override
    public double area() {
        return 2 * Math.PI * (super.getRadio() + radioInterno) * (super.getAltura() + super.getRadio() - radioInterno);
    }
    
    @Override
    public String tipoFigura() {
        return "Cilindro Hueco";
    }   

}
