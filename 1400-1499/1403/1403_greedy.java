import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        int[] deadline = new int[n], reward = new int[n];
        Integer[] orders = new Integer[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            deadline[i] = (int)in.nval;
            in.nextToken();
            reward[i] = (int)in.nval;
            orders[i] = i;
        }
        Arrays.sort(orders, (a, b) -> Integer.compare(deadline[a], deadline[b]));
        // by deadline: keep the best orders that fit, dropping the cheapest when
        // there are more orders than days so far
        PriorityQueue<Integer> kept =
            new PriorityQueue<>((a, b) -> Integer.compare(reward[a], reward[b]));
        for (int i : orders) {
            kept.add(i);
            if (kept.size() > deadline[i])
                kept.poll();
        }
        List<Integer> chosen = new ArrayList<>(kept);
        chosen.sort((a, b) -> Integer.compare(deadline[a], deadline[b]));
        StringBuilder out = new StringBuilder();
        out.append(chosen.size()).append('\n');
        for (int k = 0; k < chosen.size(); k++)
            out.append(k > 0 ? " " : "").append(chosen.get(k) + 1);
        System.out.println(out);
    }
}
