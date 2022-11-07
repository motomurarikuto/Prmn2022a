package lecture02;

public class Human {
    String name;
    int age;
    Human(String name,int age){
        this.name = name;
        this.age = age;
    }

    void print(){
        if(age <= 18  ){
            System.out.print("生徒:");
        }
        else if(age <= 22){
            System.out.print("学生:");
        }
        else{

        }
        System.out.println(name + age + "歳です。");
    }
}
