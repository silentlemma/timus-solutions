import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        if (in.nextToken() == StreamTokenizer.TT_EOF)
            return;
        int k = (int)in.nval;
        // (signs left, kind), the most signs first
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> b[0] - a[0]);
        for (int t = 1; t <= k; t++) {
            in.nextToken();
            heap.add(new int[] {(int)in.nval, t});
        }
        StringBuilder out = new StringBuilder();
        int prev = 0;
        while (!heap.isEmpty()) {
            int[] s = heap.poll();
            if (s[1] == prev && !heap.isEmpty()) {
                // the most plentiful kind was just used: take the next one
                int[] other = heap.poll();
                heap.add(s);
                s = other;
            }
            if (out.length() > 0)
                out.append(' ');
            out.append(s[1]);
            prev = s[1];
            if (s[0] > 1)
                heap.add(new int[] {s[0] - 1, s[1]});
        }
        System.out.println(out);
    }
}
