import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        int[] cars = new int[n], where = new int[n + 1], run = new int[n + 1];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            cars[i] = (int)in.nval;
            where[cars[i]] = i;
        }
        // cut 1..n into the fewest runs of numbers that already stand in order, and a
        // new run starts where car v + 1 stands before car v
        for (int car = 2; car <= n; car++)
            run[car] = run[car - 1] + (where[car] < where[car - 1] ? 1 : 0);
        int passes = 0;
        while ((1 << passes) <= run[n])
            passes++;
        StringBuilder out = new StringBuilder();
        out.append(passes).append('\n');
        for (int bit = 0;; bit++) {
            for (int i = 0; i < n; i++)
                out.append(i > 0 ? " " : "").append(cars[i]);
            out.append('\n');
            if (bit == passes)
                break;
            // pass b sends the cars whose run number has bit b set to the right, and
            // like a radix sort from the low bit up, the passes leave the runs in order
            int[] next = new int[n];
            int k = 0;
            for (int side = 0; side < 2; side++)
                for (int car : cars)
                    if ((run[car] >> bit & 1) == side)
                        next[k++] = car;
            cars = next;
        }
        System.out.print(out);
    }
}
