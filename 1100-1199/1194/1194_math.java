import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long n = in.nextLong(), k = in.nextLong();
        // every two hobbits shake hands exactly once, when their groups part,
        // except the married couples, who go home together and never part
        System.out.println(n * (n - 1) / 2 - k);
    }
}
