import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
    static final int SIZE = 3;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int k = in.nextInt();
        String[][] teams = new String[k][SIZE];
        for (int i = 0; i < k; i++) {
            for (int j = 0; j < SIZE; j++) {
                teams[i][j] = in.next();
            }
        }
        // clash[i]: the teams sharing a member with team i, i itself included
        int[] clash = new int[k];
        for (int i = 0; i < k; i++) {
            Set<String> members = new HashSet<>(Arrays.asList(teams[i]));
            for (int j = 0; j < k; j++) {
                for (String name : teams[j]) {
                    if (members.contains(name)) {
                        clash[i] |= 1 << j;
                    }
                }
            }
        }
        // the lowest team of a set is either skipped or taken with its clashes
        // out; both smaller sets come earlier in this order
        int[] best = new int[1 << k];
        for (int mask = 1; mask < (1 << k); mask++) {
            int i = Integer.numberOfTrailingZeros(mask);
            best[mask] = Math.max(best[mask & (mask - 1)], 1 + best[mask & ~clash[i]]);
        }
        System.out.println(best[(1 << k) - 1]);
    }
}
