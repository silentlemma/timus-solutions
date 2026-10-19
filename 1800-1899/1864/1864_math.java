import java.util.Scanner;

public class Main {
    static final int MONEY = 100;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] bought = new int[n];
        int total = 0;
        for (int i = 0; i < n; i++) {
            bought[i] = in.nextInt();
            total += bought[i];
        }
        // everybody, Den too, drinks total / (n + 1); in units of 1 / (n + 1)
        // litre, friend i paid for bought[i] (n + 1) - total litres of others
        int[] over = new int[n];
        int all = 0;
        for (int i = 0; i < n; i++) {
            over[i] = Math.max(0, bought[i] * (n + 1) - total);
            all += over[i];
        }
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++) {
            out.append(i > 0 ? " " : "").append(MONEY * over[i] / all);
        }
        System.out.println(out);
    }
}
