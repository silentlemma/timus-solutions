import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        long[] a = new long[n], b = new long[n], c = new long[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            a[i] = (long)in.nval;
            in.nextToken();
            b[i] = (long)in.nval;
            in.nextToken();
            c[i] = (long)in.nval;
        }
        // machine B never holds the line, so the line behaves like two machines
        // with times a + b and b + c, where Johnson's rule is optimal: toys
        // faster on the first come first, by its time, the rest by the second
        List<Integer> early = new ArrayList<>(), late = new ArrayList<>();
        for (int i = 0; i < n; i++)
            (a[i] + b[i] < b[i] + c[i] ? early : late).add(i);
        early.sort((x, y) -> Long.compare(a[x] + b[x], a[y] + b[y]));
        late.sort((x, y) -> Long.compare(b[y] + c[y], b[x] + c[x]));
        early.addAll(late);
        long doneA = 0, doneB = 0, doneC = 0;
        for (int i : early) {
            doneA += a[i];
            doneB = Math.max(doneB, doneA) + b[i];
            doneC = Math.max(doneC, doneB) + c[i];
        }
        StringBuilder sb = new StringBuilder();
        sb.append(doneC).append('\n');
        for (int k = 0; k < n; k++)
            sb.append(early.get(k) + 1).append(k + 1 < n ? ' ' : '\n');
        System.out.print(sb);
    }
}
