import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static final int PLAYERS = 3, SUITS = 4, RANKS = 8;
    static final int HAND = 10;       // cards per player
    static final int SUIT_BITS = 14;  // an owner string of a suit fits in this many bits
    static final int CACHE_BITS = 19; // 4 MB of remembered positions, inside 16 MB with the JVM
    static final int FULL_SUIT = (1 << RANKS) - 1;
    static final long GOLDEN = 0x9E3779B97F4A7C15L;
    static final String RANK_NAMES = "7 8 9 10 J Q K A";

    // hand[p] holds player p's cards, suit s in bits 8 s .. 8 s + 7, rank upwards
    static int[] hand = new int[PLAYERS];
    static long[] cache = new long[1 << CACHE_BITS];

    // the suits play alike and only the order of the cards inside a suit
    // matters, so a position is the sorted owner strings of the suits
    static long key(int leader) {
        long[] codes = new long[SUITS];
        for (int s = 0; s < SUITS; s++) {
            long v = 1;
            for (int c = s * RANKS; c < (s + 1) * RANKS; c++)
                for (int p = 0; p < PLAYERS; p++)
                    if ((hand[p] >> c & 1) == 1)
                        v = v * PLAYERS + p;
            codes[s] = v;
        }
        Arrays.sort(codes);
        long k = leader + 1;
        for (long v : codes)
            k = k << SUIT_BITS | v;
        return k;
    }

    // one card from each run of touching cards, where no other player's card
    // lies between two cards of a run
    static int choices(int p, int allowed, int everyone) {
        int out = 0;
        for (int c = 0; c < SUITS * RANKS; c++) {
            if ((allowed >> c & 1) == 0)
                continue;
            int s = c / RANKS;
            int below = everyone & ((1 << c) - 1) & (FULL_SUIT << (s * RANKS));
            if (below == 0 || (hand[p] & Integer.highestOneBit(below)) == 0)
                out |= 1 << c;
        }
        return out;
    }

    // the first player looks for any good card, the other two for any card
    // that makes the first player take the trick
    static boolean play(int leader, int step, int suit, int best, int bestPlayer, int everyone) {
        int p = (leader + step) % PLAYERS;
        int allowed = hand[p];
        if (step > 0 && (allowed & (FULL_SUIT << (suit * RANKS))) != 0)
            allowed &= FULL_SUIT << (suit * RANKS);
        int options = choices(p, allowed, everyone);
        for (int c = 0; c < SUITS * RANKS; c++) {
            if ((options >> c & 1) == 0)
                continue;
            int s = suit, b = best, bp = bestPlayer;
            if (step == 0) {
                s = c / RANKS;
                b = c;
                bp = p;
            } else if (c / RANKS == suit && c > best) {
                b = c;
                bp = p;
            }
            hand[p] &= ~(1 << c);
            boolean ok = step + 1 < PLAYERS ? play(leader, step + 1, s, b, bp, everyone)
                                            : bp != 0 && survive(bp);
            hand[p] |= 1 << c;
            if (ok == (p == 0))
                return ok;
        }
        return p != 0;
    }

    // can the first player take no trick from here, whatever the others do
    static boolean survive(int leader) {
        if (hand[0] == 0)
            return true;
        long k = key(leader);
        int slot = (int)((k * GOLDEN) >>> (Long.SIZE - CACHE_BITS));
        if (cache[slot] >>> 1 == k)
            return (cache[slot] & 1) == 1;
        boolean result = play(leader, 0, 0, -1, -1, hand[0] | hand[1] | hand[2]);
        cache[slot] = k << 1 | (result ? 1 : 0);
        return result;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String[] names = RANK_NAMES.split(" ");
        for (int p = 0; p < PLAYERS; p++)
            for (int i = 0; i < HAND; i++) {
                String t = in.next();
                int s = "SCDH".indexOf(t.charAt(t.length() - 1));
                int r = Arrays.asList(names).indexOf(t.substring(0, t.length() - 1));
                hand[p] |= 1 << (s * RANKS + r);
            }
        int leader = in.nextInt();
        System.out.println(survive(leader - 1) ? ";)" : ";(");
    }
}
