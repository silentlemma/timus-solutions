import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static final int SUITS = 3;
    private static final int RANKS = 9;
    private static final int TYPES = SUITS * RANKS;
    private static final int HAND_SIZE = 14;
    private static final int TRIPLE_SIZE = 3;
    private static final int PAIR_SIZE = 2;

    private static boolean triples(int[] counts) {
        counts = counts.clone();
        for (int tile = 0; tile < TYPES; ++tile) {
            // Three equal sequences can be replaced with three triplets.
            int runs = counts[tile] % TRIPLE_SIZE;
            if (runs == 0) {
                continue;
            }
            if (tile % RANKS > RANKS - TRIPLE_SIZE || counts[tile + 1] < runs
                    || counts[tile + 2] < runs) {
                return false;
            }
            counts[tile + 1] -= runs;
            counts[tile + 2] -= runs;
        }
        return true;
    }

    private static boolean winning(int[] counts) {
        int pairSuit = -1;
        for (int suit = 0; suit < SUITS; ++suit) {
            int total = 0;
            for (int rank = 0; rank < RANKS; ++rank) {
                total += counts[suit * RANKS + rank];
            }
            int remainder = total % TRIPLE_SIZE;
            if (remainder == PAIR_SIZE && pairSuit == -1) {
                pairSuit = suit;
            } else if (remainder != 0) {
                return false;
            }
        }
        if (pairSuit == -1) {
            return false;
        }
        for (int rank = 0; rank < RANKS; ++rank) {
            int tile = pairSuit * RANKS + rank;
            if (counts[tile] >= PAIR_SIZE) {
                counts[tile] -= PAIR_SIZE;
                boolean complete = triples(counts);
                counts[tile] += PAIR_SIZE;
                if (complete) {
                    return true;
                }
            }
        }
        return false;
    }

    private static String classify(int[] counts) {
        if (winning(counts)) {
            return "Tsumo";
        }
        for (int removed = 0; removed < TYPES; ++removed) {
            if (counts[removed] == 0) {
                continue;
            }
            --counts[removed];
            for (int added = 0; added < TYPES; ++added) {
                if (added == removed) {
                    continue;
                }
                // A replacement may produce five identical tiles.
                ++counts[added];
                boolean ready = winning(counts);
                --counts[added];
                if (ready) {
                    return "Tenpai";
                }
            }
            ++counts[removed];
        }
        return "Noten";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokens = new StringTokenizer(input.readLine());
        int[] counts = new int[TYPES];
        for (int i = 0; i < HAND_SIZE; ++i) {
            String tile = tokens.nextToken();
            int rank = tile.charAt(0) - '1';
            int suit = tile.charAt(1) - 'a';
            ++counts[suit * RANKS + rank];
        }
        System.out.println(classify(counts));
    }
}
