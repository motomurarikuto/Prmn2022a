package lecture01;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("We are Project Member.");
        int summ = 5 + 3;    //sumには8が入る
        int sub = 5 - 3;    //subには2が入る
        int mul = 5 * 3;    //mulには15が入る
        int div = 5 / 3;    //divには1が入る(小数点以下は切り捨て)
        int mod = 5 % 3;

        double temp = 18.7;
        System.out.println("The temperature is " + temp + " degrees");//"The tempareture is 18.7 degrees"と表示
        int[] aa = new int[10]; //int型の配列を10要素分確保
        aa[4] = 3;    //arrayの5番目に3を代入する

        int[] a = {1, 2, 3, 4};

        //課題1-1
        System.out.println("B2212400 Rikuto motomura");

        //課題1-2
        int studentNumber = 2212400;
        System.out.println("B" + studentNumber + " Rikuto motomura");

        //課題1-3
        Scanner input = new Scanner(System.in);
        System.out.println("年齢を入力してください");
        int age = input.nextInt();

        if (age < 20) {
            System.out.println("I am" + age + "years old so I cannot drink liquor.");
        } else {
            System.out.println("I am" + age + "years old so I can drink liquor.");
        }

        //課題1-4
        int sum = 0;
        int[] array = new int[100];
        for (int i = 0; i < 100; i++) {
            array[i] = i + 1;
        }

        for (int i = 0; i < 100; i++) {
            if (i % 2 == 0) {
                sum = sum + array[i];

            }
        }

        System.out.println("配列番号が偶数の総和　＝" + sum);

        //課題1-5
        int[] score = {41, 85, 72, 38, 80};
        int min1 = min(score);
        int max1 = max(score);
        double ave1 = average(score);

        for(int i=0; i< score.length; i++){
            if(score[i]>=90){
                System.out.println(i + "番" + score[i] + "点　秀");
            }
            else if(score[i]>=80){
                System.out.println(i + "番" + score[i] + "点　優");
            }
            else if(score[i]>=70){
                System.out.println(i + "番" + score[i] + "点　良");
            }
            else if(score[i]>=60){
                System.out.println(i + "番" + score[i] + "点　可");
            }
            else{
                System.out.println(i + "番" + score[i] + "点　不可");
            }
        }

        System.out.println("最高点" + max1 + "点");
        System.out.println("最低点" + min1 + "点");
        System.out.println("平均点" + ave1 + "点");


    }


    static int min(int[] x){
        int minimum = x[0];
        for (int l = 0; l<x.length;l++){
            if (minimum > x[l]) {
                minimum = x[l];
            }
        }
        return minimum;
    }

    static int max ( int[] x){

        int maximum = x[0];
        for (int l = 0; l<x.length;l++){
            if (maximum < x[l]) {
                maximum = x[l];
            }
        }


        return maximum;
    }

    static double average ( int[] x){
        double ave = x[0];
        int sum = 0;
        for (int i= 0; i<x.length;i++){
            sum = sum + x[i];
        }
        ave = (double)sum/x.length;
        return ave;
    }

}

