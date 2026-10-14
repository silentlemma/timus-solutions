import java.io.*;
import java.util.*;

public class Main {
    static final int SHOWN = 10; // suggestions per query

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        String[] word = new String[n];
        int[] count = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            word[i] = in.sval;
            in.nextToken();
            count[i] = (int)in.nval;
        }
        in.nextToken();
        int m = (int)in.nval;
        String[] queries = new String[m];
        Map<String, List<Integer>> found = new HashMap<>(); // query -> indices of its words
        for (int j = 0; j < m; j++) {
            in.nextToken();
            queries[j] = in.sval;
            found.put(queries[j], new ArrayList<>());
        }
        // the best words come first, so every queried prefix simply keeps the
        // first ten words that start with it
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++)
            order[i] = i;
        Arrays.sort(order,
                    (a, b)
                        -> count[a] != count[b] ? Integer.compare(count[b], count[a])
                                                : word[a].compareTo(word[b]));
        for (int i : order)
            for (int end = 1; end <= word[i].length(); end++) {
                List<Integer> box = found.get(word[i].substring(0, end));
                if (box != null && box.size() < SHOWN)
                    box.add(i);
            }
        StringBuilder out = new StringBuilder();
        for (int j = 0; j < m; j++) {
            if (j > 0)
                out.append('\n');
            for (int i : found.get(queries[j]))
                out.append(word[i]).append('\n');
        }
        System.out.print(out);
    }
}
