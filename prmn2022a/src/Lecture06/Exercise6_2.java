package Lecture06;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Random;
import java.util.Scanner;

public class Exercise6_2 {
    public static void main(String[] args) {
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> arrayList = new ArrayList<>();
        for (int i = 0; i < 6; i++) {
            arrayList.add(i, random.nextInt(7));
        }
        System.out.println("サイコロを5つ振りました");
        System.out.print("何番目のサイコロを確認しますか:");
        try{
            int index = scanner.nextInt();
            System.out.println(arrayList.get(index));
        }
        catch(IndexOutOfBoundsException e){
            System.out.println("ArrayListの範囲外アクセスを確認しました");
            System.out.println("プログラムを終了します");
            System.exit(1);
        }
        catch (InputMismatchException e){
            System.out.println("整数以外の値が入力されました");
            System.out.println("プログラムを終了します");
            System.exit(1);
        }


    }
}
