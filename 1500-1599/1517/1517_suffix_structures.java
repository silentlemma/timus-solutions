import java.io.*;
import java.util.*;

public class Main {
    static final int ALPHABET = 26;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String s; (s = br.readLine()) != null;)
            all.append(s).append(' ');
        StringTokenizer st = new StringTokenizer(all.toString());
        int n = Integer.parseInt(st.nextToken());
        String a = st.nextToken(), b = st.nextToken();
        // suffix automaton of a: every state is a class of substrings with the
        // same end positions; len is the longest of them, link the suffix link
        int most = 2 * n + 1;
        int[][] next = new int[most][];
        int[] link = new int[most], len = new int[most];
        next[0] = new int[ALPHABET];
        Arrays.fill(next[0], -1);
        link[0] = -1;
        int size = 1, last = 0;
        for (int i = 0; i < n; i++) {
            int c = a.charAt(i) - 'A', cur = size++;
            next[cur] = new int[ALPHABET];
            Arrays.fill(next[cur], -1);
            len[cur] = len[last] + 1;
            int p = last;
            while (p != -1 && next[p][c] == -1) {
                next[p][c] = cur;
                p = link[p];
            }
            if (p != -1) {
                int q = next[p][c];
                if (len[p] + 1 == len[q])
                    link[cur] = q;
                else {
                    int clone = size++;
                    next[clone] = next[q].clone();
                    link[clone] = link[q];
                    len[clone] = len[p] + 1;
                    for (; p != -1 && next[p][c] == q; p = link[p])
                        next[p][c] = clone;
                    link[q] = link[cur] = clone;
                }
            }
            last = cur;
        }
        // walk b through the automaton, keeping the longest suffix of the read
        // part of b that occurs in a
        int state = 0, run = 0, best = 0, end = 0;
        for (int i = 0; i < b.length(); i++) {
            int c = b.charAt(i) - 'A';
            while (state != 0 && next[state][c] == -1) {
                state = link[state];
                run = len[state];
            }
            if (next[state][c] != -1) {
                state = next[state][c];
                run++;
            }
            if (run > best) {
                best = run;
                end = i + 1;
            }
        }
        System.out.println(b.substring(end - best, end));
    }
}
