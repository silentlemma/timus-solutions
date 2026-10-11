import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line; (line = reader.readLine()) != null;)
            all.append(line).append(' ');
        StringTokenizer in = new StringTokenizer(all.toString());
        int n = Integer.parseInt(in.nextToken());
        List<List<Integer>> children = new ArrayList<>();
        for (int v = 0; v <= n; v++)
            children.add(new ArrayList<>());
        int[] value = new int[n + 1], depth = new int[n + 1];
        for (int v = 2; v <= n; v++) {
            String kind = in.nextToken();
            children.get(Integer.parseInt(in.nextToken())).add(v);
            if (kind.equals("L"))
                value[v] = Integer.parseInt(in.nextToken().replace("+", ""));
        }
        // breadth-first order from the root, then values from the leaves up:
        // the first player moves at even depths and takes the largest result
        List<Integer> order = new ArrayList<>(Arrays.asList(1));
        for (int i = 0; i < order.size(); i++)
            for (int c : children.get(order.get(i))) {
                depth[c] = depth[order.get(i)] + 1;
                order.add(c);
            }
        for (int i = order.size() - 1; i >= 0; i--) {
            int v = order.get(i);
            if (children.get(v).isEmpty())
                continue;
            int best = value[children.get(v).get(0)];
            for (int c : children.get(v))
                best = depth[v] % 2 == 0 ? Math.max(best, value[c]) : Math.min(best, value[c]);
            value[v] = best;
        }
        System.out.println(value[1] > 0 ? "+1" : value[1] < 0 ? "-1" : "0");
    }
}
