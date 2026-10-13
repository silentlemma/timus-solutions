import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

public class Main {
    // the previous tail, the new piece of text, and whether the tail starts a search
    static class Link {
        final String from, piece;
        final boolean first;

        Link(String from, String piece, boolean first) {
            this.from = from;
            this.piece = piece;
            this.first = first;
        }
    }

    static class Item {
        final int cost;
        final String tail;

        Item(int cost, String tail) {
            this.cost = cost;
            this.tail = tail;
        }
    }

    static Map<String, Integer> dist = new HashMap<>();
    static Map<String, Link> back = new HashMap<>();
    static PriorityQueue<Item> heap =
        new PriorityQueue<>((a, b) -> Integer.compare(a.cost, b.cost));

    static void relax(String tail, int cost, Link link) {
        Integer d = dist.get(tail);
        if (d != null && d <= cost)
            return;
        dist.put(tail, cost);
        back.put(tail, link);
        heap.add(new Item(cost, tail));
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        String[] words = new String[n];
        for (int i = 0; i < n; i++)
            words[i] = in.readLine().trim();
        // a state is the tail by which one parse runs ahead of the other; the
        // cost is the length of the text so far, and Dijkstra finds the shortest text
        for (String u : words)
            for (String v : words)
                if (!u.equals(v) && v.startsWith(u))
                    relax(v.substring(u.length()), v.length(), new Link("", v, true));
        while (!heap.isEmpty()) {
            Item top = heap.poll();
            if (top.cost > dist.get(top.tail))
                continue;
            String tail = top.tail;
            for (String w : words) {
                if (w.equals(tail)) { // both parses end together: rebuild the text from its pieces
                    List<String> pieces = new ArrayList<>();
                    for (String t = tail;; t = back.get(t).from) {
                        pieces.add(back.get(t).piece);
                        if (back.get(t).first)
                            break;
                    }
                    StringBuilder text = new StringBuilder();
                    for (int i = pieces.size() - 1; i >= 0; i--)
                        text.append(pieces.get(i));
                    System.out.println("YES");
                    System.out.println(text);
                    return;
                }
                if (w.startsWith(tail)) {
                    String rest = w.substring(tail.length());
                    relax(rest, top.cost + rest.length(), new Link(tail, rest, false));
                } else if (tail.startsWith(w)) {
                    relax(tail.substring(w.length()), top.cost, new Link(tail, "", false));
                }
            }
        }
        System.out.println("NO");
    }
}
