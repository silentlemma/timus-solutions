import java.util.Scanner;

public class Main {
    static final int WIN = 3;

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // every match gives out at least 2 points (a draw) and at most WIN,
        // so the leader has at least the average of all draws and the last team
        // at most the average of all wins; both bounds can be reached
        System.out.println((n - 1) + " " + WIN * (n - 1) / 2);
    }
}
