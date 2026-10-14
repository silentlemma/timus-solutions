import java.io.*;
import java.util.*;

public class Main {
    static final int SCALE = 1000;       // satiety has at most three digits after the point
    static final long MOST_DISHES = 128; // more than the number of different dishes
    static final long NONE = 1L << 62;
    static final int DIGITS = 3;

    static int thousandths(String text) {
        int point = text.indexOf('.');
        String whole = point < 0 ? text : text.substring(0, point);
        String part = point < 0 ? "" : text.substring(point + 1);
        return Integer.parseInt(whole) * SCALE +
            Integer.parseInt((part + "000").substring(0, DIGITS));
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        String line;
        while ((line = in.readLine()) != null)
            all.append(line).append(' ');
        StringTokenizer words = new StringTokenizer(all.toString());
        int n = Integer.parseInt(words.nextToken()), m = Integer.parseInt(words.nextToken());
        String[] names = new String[n];
        int[] price = new int[n], fill = new int[n];
        for (int i = 0; i < n; i++) {
            names[i] = words.nextToken();
            price[i] = Integer.parseInt(words.nextToken());
            fill[i] = thousandths(words.nextToken());
        }
        int top = m * SCALE;
        // best[s]: the least cost, then the most different dishes, of an order with
        // satiety s, where s = top stands for top or more; one number holds both,
        // cost * MOST_DISHES - dishes, so that smaller is better
        long[] best = new long[top + 1], mine = new long[top + 1];
        Arrays.fill(best, NONE);
        best[0] = 0;
        // per dish: whether the best order at s takes it, and in the orders
        // that take it, the satiety before the last plate and if that plate was the
        // first one, which leaves the orders without the dish
        boolean[][] took = new boolean[n][top + 1], first = new boolean[n][top + 1];
        int[][] back = new int[n][top + 1];
        for (int i = 0; i < n; i++) {
            long step = price[i] * MOST_DISHES;
            Arrays.fill(mine, NONE);
            for (int s = 0; s <= top; s++) {
                int t = Math.min(top, s + fill[i]);
                if (best[s] < NONE && best[s] + step - 1 < mine[t]) {
                    mine[t] = best[s] + step - 1;
                    back[i][t] = s;
                    first[i][t] = true;
                }
            }
            // more plates of the same dish, from lower satiety up
            for (int s = 0; s < top; s++) {
                int t = Math.min(top, s + fill[i]);
                if (mine[s] < NONE && mine[s] + step < mine[t]) {
                    mine[t] = mine[s] + step;
                    back[i][t] = s;
                    first[i][t] = false;
                }
            }
            for (int s = 0; s <= top; s++)
                if (mine[s] < best[s]) {
                    best[s] = mine[s];
                    took[i][s] = true;
                }
        }
        // walk back from the full order, dish by dish from the last one
        int[] plates = new int[n];
        int s = top;
        for (int i = n - 1; i >= 0; i--)
            if (took[i][s]) {
                boolean done = false;
                while (!done) {
                    plates[i]++;
                    done = first[i][s];
                    s = back[i][s];
                }
            }
        long cost = 0;
        for (int i = 0; i < n; i++)
            cost += (long)price[i] * plates[i];
        StringBuilder out = new StringBuilder();
        out.append(cost).append('\n');
        for (int i = 0; i < n; i++)
            if (plates[i] > 0)
                out.append(names[i]).append(' ').append(plates[i]).append('\n');
        System.out.print(out);
    }
}
