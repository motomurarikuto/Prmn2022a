package Lecture06;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Exercise6_1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        try {
            System.out.println("小数を入力してください");
            Double n = scanner.nextDouble();
            System.out.println("入力した値: " + n);
        }
        catch (InputMismatchException e){
            System.out.println("エラー.");
        }

    }
}
