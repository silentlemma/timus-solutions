import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static final int LONGEST = 30, BASE = 10;
    static final int[] DIGITS = {1, 2};

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // breadth-first search over remainders: shorter numbers come first, and
        // within one length the queue keeps numeric order, so the first number
        // to reach a remainder is the smallest one with it
        int[] parent = new int[n], digit = new int[n], length = new int[n], queue = new int[n];
        Arrays.fill(parent, -2);
        int tail = 0;
        for (int d : DIGITS) {
            int r = d % n;
            if (parent[r] == -2) {
                parent[r] = -1;
                digit[r] = d;
                length[r] = 1;
                queue[tail++] = r;
            }
        }
        for (int head = 0; head < tail && parent[0] == -2; head++) {
            int r = queue[head];
            if (length[r] == LONGEST)
                continue;
            for (int d : DIGITS) {
                int s = (int)(((long)r * BASE + d) % n);
                if (parent[s] == -2) {
                    parent[s] = r;
                    digit[s] = d;
                    length[s] = length[r] + 1;
                    queue[tail++] = s;
                }
            }
        }
        if (parent[0] == -2) {
            System.out.println("Impossible");
            return;
        }
        StringBuilder out = new StringBuilder();
        for (int r = 0; r != -1; r = parent[r])
            out.append(digit[r]);
        System.out.println(out.reverse());
    }
}
