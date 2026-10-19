import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    static final int LONGEST = 140;
    static final int PREFIX = "RT @: ".length();

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        String[] names = new String[n];
        List<List<String>> followNames = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            // a description is a name, a count and that many names
            List<String> words = new ArrayList<>();
            while (words.size() < 2 || words.size() < 2 + Integer.parseInt(words.get(1))) {
                for (String w : in.readLine().trim().split("\\s+")) {
                    if (!w.isEmpty()) {
                        words.add(w);
                    }
                }
            }
            names[i] = words.get(0);
            followNames.add(words.subList(2, words.size()));
        }
        String tweet = in.readLine();
        Map<String, Integer> index = new HashMap<>();
        for (int i = 0; i < n; i++) {
            index.put(names[i], i);
        }
        // length[u] is the shortest message u can hold; a retweet of u's message
        // is longer by the prefix and u's name
        int[] length = new int[n];
        Arrays.fill(length, LONGEST + 1);
        length[0] = tweet.length();
        boolean[] done = new boolean[n];
        while (true) {
            int u = -1;
            for (int i = 0; i < n; i++) {
                if (!done[i] && (u < 0 || length[i] < length[u])) {
                    u = i;
                }
            }
            if (u < 0 || length[u] > LONGEST) {
                break;
            }
            done[u] = true;
            int longer = length[u] + PREFIX + names[u].length();
            for (String f : followNames.get(u)) {
                int v = index.get(f);
                length[v] = Math.min(length[v], longer);
            }
        }
        // everybody who holds a message shows it to all followers
        boolean[] knows = new boolean[n];
        for (int u = 0; u < n; u++) {
            if (done[u]) {
                knows[u] = true;
                for (String f : followNames.get(u)) {
                    knows[index.get(f)] = true;
                }
            }
        }
        StringBuilder out = new StringBuilder();
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (knows[i]) {
                count++;
                out.append(names[i]).append('\n');
            }
        }
        System.out.print(count + "\n" + out);
    }
}
