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
        // a plain comparator avoids lambda initialization on the judge runtime.
        PriorityQueue<int[]> heap = new PriorityQueue<>(k, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) { return b[0] - a[0]; }
        });
        for (int t = 1; t <= k; t++) {
            in.nextToken();
            heap.add(new int[] {(int)in.nval, t});
        }
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        boolean first = true;
        int prev = 0;
        while (!heap.isEmpty()) {
            int[] s = heap.poll();
            if (s[1] == prev && !heap.isEmpty()) {
                // the most plentiful kind was just used: take the next one
                int[] other = heap.poll();
                heap.add(s);
                s = other;
            }
            if (!first)
                out.write(' ');
            first = false;
            out.write(Integer.toString(s[1]));
            prev = s[1];
            // the polled array is outside the heap, so decrement and reuse it safely.
            if (s[0] > 1) {
                s[0]--;
                heap.add(s);
            }
        }
        out.newLine();
        out.flush();
    }
}
