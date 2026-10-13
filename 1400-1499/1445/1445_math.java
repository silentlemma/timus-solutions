import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), biggest = 0, total = 0;
        for (int i = 0; i < n; i++) {
            int size = in.nextInt();
            biggest = Math.max(biggest, size);
            total += size;
        }
        // the biggest company needs gifts from outside it: prepared or from the others
        int best = Math.max(1, 2 * biggest - total);
        // in the worst order the biggest company comes first, and that many always suffice
        System.out.println(best + " " + biggest);
    }
}
