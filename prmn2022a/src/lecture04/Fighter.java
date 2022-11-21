package lecture04;

public class Fighter {
    private int hitPoint;
    private int power;
    private String name;

    public Fighter(int hitPoint, int power, String name) {
        this.hitPoint = hitPoint;
        this.power = power;
        this.name = name;
    }

    public void attack(Fighter enemy) {
        enemy.hitPoint -= power;
        System.out.println(name + "は" + enemy.name + "に" + power + "ダメージを与えた。");

    }

    public boolean isAlive() {
        if (hitPoint <= 0) {
            System.out.println(getName() + "は倒れた");
            return true;
        } else {
            System.out.println(name + "の残り　hitPoint :" + hitPoint);
            return false;
        }
    }

    public int getHitPoint() {
        return hitPoint;
    }

    public void setHitPoint(int hitPoint) {
        this.hitPoint = hitPoint;
    }

    public String getName() {
        return name;
    }
}
