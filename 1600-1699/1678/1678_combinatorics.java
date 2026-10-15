import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    static final String RANKS = "23456789TJQKA";
    static final int RANK_COUNT = 13;

    static int n;
    static int m;
    static int k;
    static List<int[]> combos = new ArrayList<>();
    static Map<String, Integer> bestCache = new HashMap<>();
    static Map<String, double[]> rivalCache = new HashMap<>();
    static double[] fact;
    static double answer;
    static int[] own = new int[RANK_COUNT];
    static int[] shown = new int[RANK_COUNT];
    static int[] common = new int[RANK_COUNT];
    static double scale;

    // a shape (sorted counts, all below 256) as a map key
    static String key(int[] shape) {
        StringBuilder b = new StringBuilder();
        for (int x : shape) {
            b.append((char) x);
        }
        return b.toString();
    }

    static int[] sortedDown(int[] a, boolean dropZeros) {
        int[] b = Arrays.stream(a).filter(x -> !dropZeros || x > 0).sorted().toArray();
        for (int i = 0, j = b.length - 1; i < j; i++, j--) {
            int t = b[i];
            b[i] = b[j];
            b[j] = t;
        }
        return b;
    }

    // the most valuable combination a hand with these sorted counts holds,
    // or -1: (v1, ..., vL) fits when the i-th largest count is at least the i-th v
    static int best(int[] hand) {
        String h = key(hand);
        Integer known = bestCache.get(h);
        if (known != null) {
            return known;
        }
        int found = -1;
        for (int c = combos.size() - 1; c >= 0 && found < 0; c--) {
            int[] need = combos.get(c);
            boolean fits = need.length <= hand.length;
            for (int i = 0; fits && i < need.length; i++) {
                fits = hand[i] >= need[i];
            }
            if (fits) {
                found = c;
            }
        }
        bestCache.put(h, found);
        return found;
    }

    // the partitions of total into at most parts positive parts, decreasing
    static void partitions(int rest, int top, int parts, List<Integer> cur, List<int[]> out) {
        if (rest == 0) {
            out.add(cur.stream().mapToInt(Integer::intValue).toArray());
            return;
        }
        if (cur.size() == parts) {
            return;
        }
        for (int x = Math.min(rest, top); x > 0; x--) {
            cur.add(x);
            partitions(rest - x, x, parts, cur, out);
            cur.remove(cur.size() - 1);
        }
    }

    // the chance, for each combination, that a rival's best one is cheaper,
    // shifted by one place. Ranks with equal common counts are interchangeable,
    // so each group takes a partition of its share of the rival's cards
    static double[] rival(int[] sortedCommon) {
        String ck = key(sortedCommon);
        if (rivalCache.containsKey(ck)) {
            return rivalCache.get(ck);
        }
        Map<Integer, Integer> groups = new LinkedHashMap<>();
        for (int v : sortedCommon) {
            groups.merge(v, 1, Integer::sum);
        }
        // a state is the sorted shape so far plus, as its last character, the cards used
        Map<String, Double> states = new HashMap<>();
        states.put(String.valueOf((char) 0), 1.0);
        for (Map.Entry<Integer, Integer> group : groups.entrySet()) {
            int v = group.getKey();
            int g = group.getValue();
            Map<String, Double> next = new HashMap<>();
            for (Map.Entry<String, Double> st : states.entrySet()) {
                String code = st.getKey();
                int used = code.charAt(code.length() - 1);
                for (int s = 0; s + used <= m; s++) {
                    List<int[]> parts = new ArrayList<>();
                    partitions(s, s, g, new ArrayList<>(), parts);
                    for (int[] p : parts) {
                        double ways = fact[g] / fact[g - p.length];
                        Map<Integer, Integer> mult = new HashMap<>();
                        for (int x : p) {
                            mult.merge(x, 1, Integer::sum);
                            ways /= fact[x];
                        }
                        for (int c : mult.values()) {
                            ways /= fact[c];
                        }
                        int extra = v > 0 ? g - p.length : 0;
                        int[] merged = new int[code.length() - 1 + p.length + extra];
                        int at = 0;
                        for (int i = 0; i + 1 < code.length(); i++) {
                            merged[at++] = code.charAt(i);
                        }
                        for (int x : p) {
                            merged[at++] = v + x;
                        }
                        for (int i = 0; i < extra; i++) {
                            merged[at++] = v;
                        }
                        String nk = key(sortedDown(merged, false)) + (char) (used + s);
                        next.merge(nk, st.getValue() * ways, Double::sum);
                    }
                }
            }
            states = next;
        }
        double sc = fact[m] / Math.pow(RANK_COUNT, m);
        double[] dist = new double[combos.size() + 1];
        for (Map.Entry<String, Double> st : states.entrySet()) {
            String code = st.getKey();
            if (code.charAt(code.length() - 1) == m) {
                int[] shape = new int[code.length() - 1];
                for (int i = 0; i < shape.length; i++) {
                    shape[i] = code.charAt(i);
                }
                dist[best(shape) + 1] += st.getValue() * sc;
            }
        }
        double[] below = new double[combos.size() + 1];
        for (int c = 0; c < combos.size(); c++) {
            below[c + 1] = below[c] + dist[c];
        }
        rivalCache.put(ck, below);
        return below;
    }

    // the hidden common cards: every way to spread them over the ranks
    static void spread(int r, int left, double weight) {
        if (r == RANK_COUNT - 1) {
            common[r] = shown[r] + left;
            weight /= fact[left];
            int[] hand = new int[RANK_COUNT];
            for (int i = 0; i < RANK_COUNT; i++) {
                hand[i] = common[i] + own[i];
            }
            int top = best(sortedDown(hand, true));
            if (top >= 0) {
                double beat = rival(sortedDown(common, false))[top + 1];
                answer += weight * scale * Math.pow(beat, n - 1);
            }
            return;
        }
        for (int x = 0; x <= left; x++) {
            common[r] = shown[r] + x;
            spread(r + 1, left - x, weight / fact[x]);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer head = new StringTokenizer(in.readLine());
        n = Integer.parseInt(head.nextToken());
        m = Integer.parseInt(head.nextToken());
        k = Integer.parseInt(head.nextToken());
        for (char c : in.readLine().toCharArray()) {
            if (RANKS.indexOf(c) >= 0) {
                own[RANKS.indexOf(c)]++;
            }
        }
        int shownCount = 0;
        String shownLine = in.readLine();
        for (char c : (shownLine == null ? "" : shownLine).toCharArray()) {
            if (RANKS.indexOf(c) >= 0) {
                shown[RANKS.indexOf(c)]++;
                shownCount++;
            }
        }
        StringBuilder rest = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            rest.append(line).append(' ');
        }
        StringTokenizer words = new StringTokenizer(rest.toString());
        int count = Integer.parseInt(words.nextToken());
        for (int c = 0; c < count; c++) {
            int size = Integer.parseInt(words.nextToken());
            int[] need = new int[size];
            for (int i = 0; i < size; i++) {
                need[i] = Integer.parseInt(words.nextToken());
            }
            combos.add(sortedDown(need, false));
        }
        fact = new double[m + k + RANK_COUNT + 1];
        fact[0] = 1;
        for (int i = 1; i < fact.length; i++) {
            fact[i] = fact[i - 1] * i;
        }
        int hidden = k - shownCount;
        scale = fact[hidden] / Math.pow(RANK_COUNT, hidden);
        spread(0, hidden, 1.0);
        System.out.println(String.format(Locale.US, "%.10f", answer));
    }
}
