import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    static final int THREE = 3;
    static final int CARDS = 8, HAND = 3, SLEEVE = 6; // Sasha's, Dima's, then the sleeve
    static final int FIRST_FACE = 11;                 // J, Q, K, A rank from 11 to 14
    static final String FACES = "JQKA";
    // combinations from the lowest: high card, pair, flush, straight,
    // three of a kind, straight flush, three threes
    static final int HIGH = 0, PAIR = 1, FLUSH = 2, STRAIGHT = 3;
    static final int TRIPLE = 4, STRAIGHT_FLUSH = 5, THREE_THREES = 6;

    static int rankOf(String card) {
        String name = card.substring(0, card.length() - 1);
        int face = FACES.indexOf(name);
        return name.length() == 1 && face >= 0 ? FIRST_FACE + face : Integer.parseInt(name);
    }

    static char suit(String card) { return card.charAt(card.length() - 1); }

    // a key that orders hands from the weakest to the strongest
    static int[] value(String[] h) {
        int[] r = {rankOf(h[0]), rankOf(h[1]), rankOf(h[2])};
        Arrays.sort(r);
        int a = r[2], b = r[1], c = r[0];
        boolean flush = suit(h[0]) == suit(h[1]) && suit(h[1]) == suit(h[2]);
        boolean straight = a == b + 1 && b == c + 1;
        if (a == THREE && c == THREE)
            return new int[] {THREE_THREES, 0, 0, 0};
        if (straight && flush)
            return new int[] {STRAIGHT_FLUSH, a, b, c};
        if (a == c)
            return new int[] {TRIPLE, a, b, c};
        if (straight)
            return new int[] {STRAIGHT, a, b, c};
        if (flush)
            return new int[] {FLUSH, a, b, c};
        if (a == b)
            return new int[] {PAIR, a, c, 0};
        if (b == c)
            return new int[] {PAIR, b, a, 0};
        return new int[] {HIGH, a, b, c};
    }

    static int compare(int[] x, int[] y) {
        for (int i = 0; i < x.length; i++)
            if (x[i] != y[i])
                return Integer.compare(x[i], y[i]);
        return 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        List<String> tokens = new ArrayList<>();
        for (String line; (line = in.readLine()) != null;)
            for (String t : line.trim().split("\\s+"))
                if (!t.isEmpty())
                    tokens.add(t);
        StringBuilder out = new StringBuilder();
        for (int g = 0; g + CARDS <= tokens.size(); g += CARDS) {
            String[] card = tokens.subList(g, g + CARDS).toArray(new String[0]);
            String[] sasha = Arrays.copyOfRange(card, 0, HAND);
            String[] dima = Arrays.copyOfRange(card, HAND, SLEEVE);
            List<String> usable = new ArrayList<>();
            for (int i = SLEEVE; i < CARDS; i++)
                if (!Arrays.asList(sasha).contains(card[i]))
                    usable.add(card[i]);
            // Dima's hands: as dealt, one card swapped, or two swapped for both
            List<String[]> hands = new ArrayList<>();
            hands.add(dima);
            for (String c : usable)
                for (int i = 0; i < HAND; i++) {
                    String[] h = dima.clone();
                    h[i] = c;
                    hands.add(h);
                }
            if (usable.size() == 2)
                for (int keep = 0; keep < HAND; keep++)
                    hands.add(new String[] {dima[keep], usable.get(0), usable.get(1)});
            int[] target = value(sasha);
            boolean win = false, draw = false;
            for (String[] h : hands) {
                if (h[0].equals(h[1]) || h[1].equals(h[2]) || h[0].equals(h[2]))
                    continue;
                int c = compare(value(h), target);
                win |= c > 0;
                draw |= c == 0;
            }
            out.append(win ? "Dima" : draw ? "Artyom" : "Sasha").append('\n');
        }
        System.out.print(out);
    }
}
