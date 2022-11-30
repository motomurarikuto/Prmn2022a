package lecture04;
import java.util.Scanner;

import java.util.ArrayList;

public class ATM {

    private  ArrayList<Account> accountlist;


    public ATM(){
     accountlist = new ArrayList<>();

    }

    public  void registerAccount(String name, String number){
        accountlist.add(new Account(name,number));
        System.out.println(name + "　さんのアカウントを口座番号:" + name + "で登録しました。");

    }

    public boolean existAccount(String name, String number){


        for(Account account : accountlist) {
            if (account.getName().equals(name)) {
                if (account.getNumber().equals(number)) {
                    System.out.println("名前:" + name + "口座番号:" + number + "は存在します。");
                    return true;
                }
            }
        }
        System.out.println("名前:" + name + "口座番号:" + number + "は存在しません。");

        return false;
    }

    public void deposit(String name, String number, long money){
        if(existAccount(name,number)){
            for(Account account : accountlist) {
                if (account.getName().equals(name)) {
                    if (account.getNumber().equals(number)) {
                        account.setBalance(account.getBalance() + money);
                        System.out.println("口座番号:" + number + "に"  + money + "円入金しました。");

                    }
                }
            }

        }else{
            existAccount(name,number);
        }

    }

    public long withdraw(String name,String number, long money){
        if(existAccount(name,number)){
            for(Account account : accountlist) {
                if (account.getName().equals(name)) {
                    if (account.getNumber().equals(number)) {
                        if(account.getBalance() - money <0) {
                            System.out.println("口座番号:" + number + "から"  + money + "円h引きませんでした。残高:" + account.getBalance() + " 円です。");
                        }else {
                            account.setBalance(account.getBalance() - money);
                            System.out.println("口座番号:" + number + "から" + money + "円引き出しました。残高:" + account.getBalance() + " 円です。");
                        }

                    }
                }
            }

        }
        return 1;
    }

}
