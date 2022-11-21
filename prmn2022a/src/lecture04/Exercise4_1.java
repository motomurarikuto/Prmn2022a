package lecture04;

public class Exercise4_1 {


    public static void main(String[] args) {
        Fighter fighter1 = new Fighter(10,3,"俺様");
        Fighter fighter2 = new Fighter(5,1,"てっきー");
        while(true){
            fighter1.attack(fighter2);
            fighter2.setHitPoint(fighter2.getHitPoint());
            if(fighter2.isAlive()){
                break;
            }

            fighter2.attack(fighter1);
            fighter1.setHitPoint(fighter1.getHitPoint());
            if(fighter2.isAlive()){
                break;
            }

        }




        }


    }




