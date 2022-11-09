package Lecture3;
import java.util.Scanner;
import java.util.ArrayList;

public class Exercise3_3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> strings = new ArrayList<>();

        int n = 2;


        for (int i = 0; i < n; i++) {
            System.out.println((i+1) + "つ目の整数を入力してください");
            String str = scanner.nextLine();
            strings.add(i, str);

        }


        int l = 0;
        int sum = 0;
        for(String str : strings){
            if(l != 0){
                System.out.print(" + ");
            }
            System.out.print( Integer.parseInt(str.toString()));
            sum += Integer.parseInt(str.toString());

            l++;

        }
        System.out.print(" = " + sum);
    }
}
