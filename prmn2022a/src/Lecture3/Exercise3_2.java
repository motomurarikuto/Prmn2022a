package Lecture3;
import java.util.Scanner;
import java.util.ArrayList;

public class Exercise3_2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> strings = new ArrayList<>();

        System.out.println("何行分入力しますか？");
        int n = scanner.nextInt();
        scanner.nextLine();

        for (int i = 0; i < n; i++) {
            System.out.println((i+1) + "行目:");
            String str = scanner.nextLine();
            strings.add(i, str);


        }
        System.out.println("入力した文字列");

        int l = 0;
        for(String str : strings){
            System.out.println("[" + l + "]" + str.toString());
            l++;

        }



    }
}
