package lecture02;

public class Car {
    int fuel;
    Tire[] tires ;
    Engine engine;

    Car(){
        this.fuel = 0;
    }
    Car(Tire[] tires , Engine engine){
        this.fuel = 0;
        this.tires = tires;
        this.engine = engine;
    }

    void run(){
        if(fuel <= 0){
            System.out.println("燃料が足りないため走れませんでした。");
        }
        else {
            fuel -= 1;
            System.out.println("燃料を1消費して走りました。");
        }


    }

    void startEngine(){
        engine.start();
    }

}
