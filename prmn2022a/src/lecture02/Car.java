package lecture02;

public class Car {
    int fuel;
    Tire[] tires = new Tire[4];
    Engine engine = new Engine(4000);


    Car(Tire[] tires , Engine engine){
        this.fuel = 0;
        for(int i = 0; i < 4; i++){
            this.tires[i] = new Tire(65);
        }
    }

    void run(){
        if(fuel <= 0){
            System.out.println("燃料が足りないため走れませんでした。");
        }
        else {
            fuel = fuel - 1;
            System.out.println("燃料を1消費して走りました。");
        }


    }

    void startEngine(){
        engine.start();
    }

}
