import java.util.Scanner;

public class Main {
    // three stones in a row can be cleared down to one, which settles the 2D case
    static final int GROUP = 3;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt(), b = in.nextInt();
        int m = Math.min(a, b), n = Math.max(a, b);
        int answer;
        if (m == 1) {
            answer = (n + 1) / 2;
        } else {
            answer = m % GROUP == 0 || n % GROUP == 0 ? 2 : 1;
        }
        System.out.println(answer);
    }
}
