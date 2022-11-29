package Lecture05;

import java.util.ArrayList;

public class Exercise5_7 {
    public static void main(String[] args) {
        ArrayList<Insect> insectslist = new ArrayList<>();
        insectslist.add(new Insect());
        insectslist.add(new Butterfly());
        insectslist.add(new Locust());
        insectslist.add(new SwallowtailButterfly());

        for(Insect musi : insectslist){
            musi.move();
        }


    }
}
