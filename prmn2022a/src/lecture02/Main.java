package lecture02;

public class Main {
    public static void main(String[] args) {


        Human human1 = new Human("本村陸斗", 20);
        human1.print();

        Human human2 = new Human("俺", 23);
        human2.print();

        Car car = new Car();
        GasStation gas = new GasStation();
        car.run();
        gas.refuel(car);
        car.run();
    }
}
