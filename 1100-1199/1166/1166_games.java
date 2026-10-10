import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    // the cards after which the second player loses the turn: 6, 7, ace,
    // king of spades; the face-up card before the first move gets the next
    // index
    static List<String> skips = new ArrayList<>();
    static List<String> real = new ArrayList<>();
    static String last = "";
    static int jokers;
    static boolean[] failed;

    // value, suit, announced suit (0 unless a queen) and index of the top
    static class Top {
        char value, suit, announced;
        int index;

        Top(char value, char suit, char announced, int index) {
            this.value = value;
            this.suit = suit;
            this.announced = announced;
            this.index = index;
        }
    }

    static boolean covers(String card, Top top) {
        if (top.announced != 0) {
            return card.charAt(1) == top.announced;
        }
        return card.charAt(1) == top.suit || card.charAt(0) == top.value;
    }

    static Top topOf(int k) {
        return new Top(skips.get(k).charAt(0), skips.get(k).charAt(1), (char)0, k);
    }

    // lays the cards still left after top, or reports false; every card but
    // the last must make the opponent skip, and the last may be anything
    static boolean finish(int mask, int used, Top top, List<String> out) {
        int rest = real.size() - Integer.bitCount(mask) + jokers - used + (last.isEmpty() ? 0 : 1);
        if (rest == 1) {
            if (!last.isEmpty()) {
                if (!covers(last, top)) {
                    return false;
                }
                out.add(last.charAt(0) == 'Q' ? last + last.charAt(1) : last);
                return true;
            }
            if (used < jokers) {
                out.add("*2" + (top.announced != 0 ? top.announced : top.suit));
                return true;
            }
            for (int k = 0; k < real.size(); k++) {
                if ((mask >> k & 1) == 0) {
                    if (!covers(real.get(k), top)) {
                        return false;
                    }
                    out.add(real.get(k));
                    return true;
                }
            }
        }
        int key = (mask * (jokers + 1) + used) * (skips.size() + 1) + top.index;
        if (failed[key]) {
            return false;
        }
        for (int k = 0; k < real.size(); k++) {
            if ((mask >> k & 1) == 0 && covers(real.get(k), top)) {
                out.add(real.get(k));
                if (finish(mask | 1 << k, used, topOf(skips.indexOf(real.get(k))), out)) {
                    return true;
                }
                out.remove(out.size() - 1);
            }
        }
        if (used < jokers) {
            for (int s = 0; s < skips.size(); s++) {
                if (covers(skips.get(s), top)) {
                    out.add("*" + skips.get(s));
                    if (finish(mask, used + 1, topOf(s), out)) {
                        return true;
                    }
                    out.remove(out.size() - 1);
                }
            }
        }
        failed[key] = true;
        return false;
    }

    public static void main(String[] args) throws Exception {
        for (char v : "67A".toCharArray()) {
            for (char s : "SCDH".toCharArray()) {
                skips.add("" + v + s);
            }
        }
        skips.add("KS");
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String[] hand = in.readLine().trim().split("\\s+");
        String faceUp = in.readLine().trim().replaceFirst("^\\*+", "");
        char announced = faceUp.charAt(0) == 'Q' ? faceUp.charAt(2) : 0;
        Top top = new Top(faceUp.charAt(0), faceUp.charAt(1), announced, skips.size());
        int others = 0;
        for (String word : hand) {
            if (word.equals("*")) {
                jokers++;
            } else if (skips.contains(word)) {
                real.add(word);
            } else {
                last = word;
                others++;
            }
        }
        if (others > 1) {
            System.out.println("NO");
            return;
        }
        failed = new boolean[(1 << real.size()) * (jokers + 1) * (skips.size() + 1)];
        List<String> order = new ArrayList<>();
        if (!finish(0, 0, top, order)) {
            System.out.println("NO");
            return;
        }
        System.out.println("YES");
        System.out.println(String.join(" ", order));
    }
}
