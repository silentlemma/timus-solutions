import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StringTokenizer st =
            new StringTokenizer(new BufferedReader(new InputStreamReader(System.in)).readLine());
        int n = Integer.parseInt(st.nextToken()), k = Integer.parseInt(st.nextToken());
        // a Fenwick tree over the circle: 1 for a soldier still marching
        int[] tree = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            tree[i]++;
            if (i + (i & -i) <= n)
                tree[i + (i & -i)] += tree[i];
        }
        int top = Integer.highestOneBit(n);
        StringBuilder sb = new StringBuilder();
        for (int rank = 0, left = n; left > 0; left--) {
            // the soldier k places ahead, counting among those still marching
            rank = (rank + k - 1) % left;
            // descend to the (rank + 1)-th remaining soldier
            int pos = 0, need = rank + 1;
            for (int step = top; step > 0; step /= 2)
                if (pos + step <= n && tree[pos + step] < need) {
                    pos += step;
                    need -= tree[pos];
                }
            pos++;
            sb.append(pos).append(left > 1 ? ' ' : '\n');
            for (int i = pos; i <= n; i += i & -i)
                tree[i]--;
        }
        System.out.print(sb);
    }
}
