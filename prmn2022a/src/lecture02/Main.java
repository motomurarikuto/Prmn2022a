package lecture02;

public class Main {
    public static void main(String[] args) {


        Human human1 = new Human("本村陸斗", 20);
        human1.print();

        Human human2 = new Human("俺", 23);
        human2.print();

        Engine engine = new Engine(4000);
        Tire[] tires = new Tire[4];
        for(int i = 0; i < tires.length; i++){
            tires[i] = new Tire(65);
        }

        Car car = new Car(tires, engine);
        GasStation gasStation = new GasStation();

        gasStation.refuel(car);
        car.startEngine();
        car.run();
    }
}
