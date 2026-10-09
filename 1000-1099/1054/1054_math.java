import java.util.Scanner;

public class Main {
    // the disks start on the source rod and go to the target rod
    static final int SOURCE = 1, TARGET = 2, SPARE = 3;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] rod = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            rod[i] = in.nextInt();
        }
        // disks 1..k are being moved from a to b over c; disk k moves once, in the
        // middle: before it the others go to c, after it they go from c to b
        int a = SOURCE, b = TARGET, c = SPARE;
        long steps = 0;
        for (int k = n; k >= 1; k--) {
            if (rod[k] == a) {
                int t = b;
                b = c;
                c = t;
            } else if (rod[k] == b) {
                steps += 1L << (k - 1);
                int t = a;
                a = c;
                c = t;
            } else {
                steps = -1;
                break;
            }
        }
        System.out.println(steps);
    }
}
