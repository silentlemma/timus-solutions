import java.util.Scanner;

public class Main {
    static final int SIDES = 2;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), k = in.nextInt();
        // every minute fries at most k of the 2n sides, and one steak takes
        // two minutes on its own; rotating sides cyclically reaches both bounds
        System.out.println(Math.max(SIDES, (SIDES * n + k - 1) / k));
    }
}
