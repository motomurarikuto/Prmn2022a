package lecture04;
import java.util.Scanner;

import java.util.ArrayList;

public class Exercise4_2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ATM atm = new ATM();
        System.out.println("こんにちは");
        while(true) {
            System.out.println("口座の登録 1: 入金2: 引き出し3: 終了0:");
            int i = input.nextInt();
            if (i == 1) {
                System.out.print("名前を入力してください:");
                String name = input.next();
                System.out.print("口座番号を入力してください:");
                String kouzabangou = input.next();
                atm.registerAccount(name, kouzabangou);
            }
            if (i == 2) {
                System.out.print("名前を入力してください:");
                String name = input.next();
                System.out.print("口座番号を入力してください:");
                String kouzabangou = input.next();
                System.out.print("入金する金額を入力してください:");
                Long money = input.nextLong();


                atm.deposit(name, kouzabangou, money);
            }
            if (i == 3) {
                System.out.print("名前を入力してください:");
                String name = input.next();
                System.out.print("口座番号を入力してください:");
                String kouzabangou = input.next();
                System.out.print("引き出す金額を入力してください:");
                Long money = input.nextLong();


                Long kane = atm.withdraw(name, kouzabangou, money);
            }
            if(i == 0){
                System.exit(0);
            }
        }





    }
}
