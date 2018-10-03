/*
Author : Sandali Samarawickrama
Language : Java
Github : https://github.com/sandali95/
*/
public class Sandali95{

     public static void main(String []args){
        for (int i =1;i<=100;i++){
            if(i%3 == 0 & i%5 == 0){
                System.out.println("Spiders");
            }
            else if(i%3 == 0){
                System.out.println("Cats");
            }else if(i%5 == 0){
                System.out.println("Bats");
            }else{
                System.out.println(i);
            }
        }
     }
}