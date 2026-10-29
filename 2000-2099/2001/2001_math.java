import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a1 = in.nextInt(), b1 = in.nextInt();
        int a2 = in.nextInt(), b2 = in.nextInt();
        int a3 = in.nextInt(), b3 = in.nextInt();
        // b2 is the empty second basket, a3 the empty first one
        System.out.println((a1 - a3) + " " + (b1 - b2));
    }
}
