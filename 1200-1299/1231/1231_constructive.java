import java.io.*;

public class Main {
    static final int MAX_N = 200;
    // state i (1 to MAX_N+1) stands on cell i of the minuses; state SEEK+d
    // still has to move d cells to the left before reaching the survivor
    static final int SEEK = 300;
    // states that cross the minuses to the right of the survivor, walk back
    // over it, cross those to its left and return to it
    static final int RIGHT = 600, BACK = 601, LEFT = 602, RETURNED = 603;

    static StringBuilder out = new StringBuilder();
    static int count = 0;

    static void rule(int state, char read, int next, char write, char move) {
        out.append(state).append(' ').append(read).append(' ').append(next);
        out.append(' ').append(write).append(' ').append(move).append('\n');
        count++;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(in.readLine().trim());
        // survivor = 0-based position of the minus that stays out of n, by the
        // Josephus recurrence
        int survivor = 0;
        for (int n = 1; n <= MAX_N; n++) {
            survivor = (survivor + k) % n;
            rule(n, '-', n + 1, '-', '>');
            // the head stands on the # after n minuses and moves onto cell n
            rule(n + 1, '#', SEEK + n - 1 - survivor, '#', '<');
        }
        for (int d = 1; d < MAX_N; d++)
            rule(SEEK + d, '-', SEEK + d - 1, '-', '<');
        rule(SEEK, '-', RIGHT, '-', '>');
        rule(RIGHT, '-', RIGHT, '+', '>');
        rule(RIGHT, '+', RIGHT, '+', '>');
        rule(RIGHT, '#', BACK, '#', '<');
        rule(BACK, '+', BACK, '+', '<');
        rule(BACK, '-', LEFT, '-', '<');
        rule(LEFT, '-', LEFT, '+', '<');
        rule(LEFT, '+', LEFT, '+', '<');
        rule(LEFT, '#', RETURNED, '#', '>');
        rule(RETURNED, '+', RETURNED, '+', '>');
        System.out.print(count + "\n" + out);
    }
}
