import java.io.*;
import java.util.*;

public class Main {
    static final int SIDE = 4, CELLS = SIDE * SIDE;
    static final int LETTERS = 26;

    static String grid = "", word;
    static List<List<Integer>> nearCells = new ArrayList<>();
    // (visited cells, last cell) that cannot finish the word
    static HashSet<Integer> dead = new HashSet<>();

    // cell holds word[i - 1]; mask is every cell used so far
    static boolean walk(int cell, int mask, int i) {
        if (i == word.length())
            return true;
        int key = mask * CELLS + cell;
        if (dead.contains(key))
            return false;
        for (int next : nearCells.get(cell))
            if ((mask >> next & 1) == 0 && grid.charAt(next) == word.charAt(i) &&
                walk(next, mask | 1 << next, i + 1))
                return true;
        dead.add(key);
        return false;
    }

    static boolean found() {
        int[] have = new int[LETTERS], need = new int[LETTERS];
        for (char c : grid.toCharArray())
            have[c - 'a']++;
        for (char c : word.toCharArray())
            if (++need[c - 'a'] > have[c - 'a'])
                return false;
        dead.clear();
        for (int c = 0; c < CELLS; c++)
            if (grid.charAt(c) == word.charAt(0) && walk(c, 1 << c, 1))
                return true;
        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder rows = new StringBuilder();
        for (int r = 0; r < SIDE; r++)
            rows.append(in.readLine().trim());
        grid = rows.toString();
        for (int c = 0; c < CELLS; c++) {
            List<Integer> list = new ArrayList<>();
            int r = c / SIDE, col = c % SIDE;
            if (r > 0)
                list.add(c - SIDE);
            if (r < SIDE - 1)
                list.add(c + SIDE);
            if (col > 0)
                list.add(c - 1);
            if (col < SIDE - 1)
                list.add(c + 1);
            nearCells.add(list);
        }
        int n = Integer.parseInt(in.readLine().trim());
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++) {
            word = in.readLine().trim();
            out.append(word).append(": ").append(found() ? "YES" : "NO").append('\n');
        }
        System.out.print(out);
    }
}
