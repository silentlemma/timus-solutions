import java.io.*;
import java.util.*;

public class Main {
    static final int LETTERS = 26;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line = in.readLine();
        if (line == null)
            return;
        String s = line.trim();
        int most = 2 * s.length() + 1;
        // suffix automaton: every state is a class of substrings with the same
        // end positions, from link-length + 1 up to length characters long
        int[] length = new int[most], link = new int[most];
        int[][] next = new int[most][LETTERS];
        Arrays.fill(link, -1);
        for (int[] row : next)
            Arrays.fill(row, -1);
        int size = 1, last = 0;
        for (int i = 0; i < s.length(); i++) {
            int c = s.charAt(i) - 'a';
            int cur = size++;
            length[cur] = length[last] + 1;
            int p = last;
            while (p != -1 && next[p][c] == -1) {
                next[p][c] = cur;
                p = link[p];
            }
            if (p == -1) {
                link[cur] = 0;
            } else {
                int q = next[p][c];
                if (length[p] + 1 == length[q]) {
                    link[cur] = q;
                } else {
                    // split q: the clone keeps the shorter strings
                    int clone = size++;
                    length[clone] = length[p] + 1;
                    link[clone] = link[q];
                    next[clone] = next[q].clone();
                    while (p != -1 && next[p][c] == q) {
                        next[p][c] = clone;
                        p = link[p];
                    }
                    link[q] = clone;
                    link[cur] = clone;
                }
            }
            last = cur;
        }
        long total = 0;
        for (int v = 1; v < size; v++)
            total += length[v] - length[link[v]];
        System.out.println(total);
    }
}
