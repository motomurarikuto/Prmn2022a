package lecture02;

public class GasStation {
    void refuel(Car car){
        car.fuel = car.fuel + 20;
        System.out.println("給油したことによりfuelが20増えました。");
    }
}
