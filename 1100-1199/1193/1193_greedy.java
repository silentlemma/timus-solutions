import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        // each student: ready, talk, deadline
        int[][] students = new int[n][];
        for (int i = 0; i < n; i++) {
            students[i] = new int[] {in.nextInt(), in.nextInt(), in.nextInt()};
        }
        Arrays.sort(students, (p, q) -> Integer.compare(p[0], q[0]));
        // moving the start earlier changes nobody's order or wait, it only
        // adds the same amount to every deadline: the answer is the worst
        // lateness
        int busyUntil = 0, worst = 0;
        for (int[] s : students) {
            busyUntil = Math.max(busyUntil, s[0]) + s[1];
            worst = Math.max(worst, busyUntil - s[2]);
        }
        System.out.println(worst);
    }
}
