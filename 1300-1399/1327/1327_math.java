import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt(), b = in.nextInt();
        // the fuses burn on the odd days; (x + 1) / 2 odd days are in 1..x
        System.out.println((b + 1) / 2 - a / 2);
    }
}
