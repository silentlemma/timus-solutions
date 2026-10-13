import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

public class Main {
    static final int BITS = 21; // the answer stays below 900 000 cells, a table of 2^21 is enough
    static final int WORD = 64;
    static final int SLOTS = 1 << BITS;
    static final long MIX = 0x9E3779B97F4A7C15L;

    // an open-addressing set of cell numbers; 0 marks an empty slot, so numbers are stored + 1
    static long[] table = new long[SLOTS];
    static int distinct = 0;

    static void add(long cell) {
        long key = cell + 1;
        int h = (int)((key * MIX) >>> (WORD - BITS));
        while (table[h] != 0 && table[h] != key)
            h = (h + 1) & (SLOTS - 1);
        if (table[h] == 0) {
            table[h] = key;
            distinct++;
        }
    }

    static int n, s;

    // how many steps fit on the board from cell in direction v
    static int room(int[] cell, int[] v) {
        int r = s;
        for (int i = 0; i < n; i++)
            if (v[i] > 0)
                r = Math.min(r, s - 1 - cell[i]);
            else if (v[i] < 0)
                r = Math.min(r, cell[i]);
        return r;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        s = in.nextInt();
        int[] start = new int[n];
        for (int i = 0; i < n; i++)
            start[i] = in.nextInt() - 1;
        // a cell is the number with digits x_i in base S
        long[] weight = new long[n];
        weight[0] = 1;
        for (int i = 1; i < n; i++)
            weight[i] = weight[i - 1] * s;
        // rook directions along each axis, bishop directions along all axes at once
        List<int[]> dirs = new ArrayList<>();
        Set<String> seen = new HashSet<>();
        List<int[]> candidates = new ArrayList<>();
        for (int i = 0; i < n; i++)
            for (int sign = -1; sign <= 1; sign += 2) {
                int[] v = new int[n];
                v[i] = sign;
                candidates.add(v);
            }
        for (int mask = 0; mask < (1 << n); mask++) {
            int[] v = new int[n];
            for (int i = 0; i < n; i++)
                v[i] = (mask >> i & 1) == 1 ? -1 : 1;
            candidates.add(v);
        }
        for (int[] v : candidates)
            if (seen.add(Arrays.toString(v))) // in one dimension they coincide
                dirs.add(v);
        List<int[]> first = new ArrayList<>();
        Set<String> seenCell = new HashSet<>();
        for (int[] v : dirs) {
            int r = room(start, v);
            for (int k = 1; k <= r; k++) {
                int[] cell = new int[n];
                for (int i = 0; i < n; i++)
                    cell[i] = start[i] + k * v[i];
                if (seenCell.add(Arrays.toString(cell)))
                    first.add(cell);
            }
        }
        for (int[] cell : first) {
            long here = 0;
            for (int i = 0; i < n; i++)
                here += cell[i] * weight[i];
            for (int[] v : dirs) {
                long step = 0;
                for (int i = 0; i < n; i++)
                    step += v[i] * weight[i];
                // every cell on the ray after the first move
                int r = room(cell, v);
                for (int k = 1; k <= r; k++)
                    add(here + k * step);
            }
        }
        System.out.println(distinct);
    }
}
