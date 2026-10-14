import java.io.*;
import java.util.*;

public class Main {
    static final int LETTER_BITS = 5; // letters 1 to 26
    static final int HEAD_LEN = 12;
    static final int GAP_BITS = 4; // a place in the rest, at most 14
    static final int CUT_BITS = 2; // 0, 1 or 2 letters deleted
    static final int ID_SHIFT = CUT_BITS + 2 * GAP_BITS;
    static final int ID_BITS = 13; // word numbers below 8192
    static final int LOW_BITS = ID_BITS + ID_SHIFT;
    static final int TAIL_BITS = LOW_BITS + 3 * LETTER_BITS; // letters after the head
    static final int GAP_MASK = (1 << GAP_BITS) - 1;
    static final int CUT_MASK = (1 << CUT_BITS) - 1;
    static final int PAIR_MASK = (1 << (2 * GAP_BITS)) - 1;

    static long[] heads, tails;
    static int count;

    // the rest of a word without letters skip1 and skip2: its first HEAD_LEN
    // letters go to heads, the others above low to tails
    static void pack(String w, int skip1, int skip2, int low) {
        long hi = 0, lo = 0;
        int pos = 0;
        for (int i = 0; i < w.length(); i++) {
            if (i == skip1 || i == skip2)
                continue;
            long c = w.charAt(i) - 'a' + 1;
            if (pos++ < HEAD_LEN)
                hi = hi << LETTER_BITS | c;
            else
                lo = lo << LETTER_BITS | c;
        }
        heads[count] = hi;
        tails[count++] = lo << LOW_BITS | low;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer st = new StreamTokenizer(in);
        st.nextToken();
        int k = (int)st.nval;
        String[] words = new String[k];
        int total = 0;
        for (int i = 0; i < k; i++) {
            st.nextToken();
            words[i] = st.sval;
            int n = words[i].length();
            total += 1 + n + n * (n - 1) / 2;
        }
        // two words are at most two edits apart when deleting at most two
        // letters from each leaves the same rest and, gap by gap of the rest,
        // the larger number of deleted letters adds up to at most two
        heads = new long[total];
        tails = new long[total];
        for (int id = 0; id < k; id++) {
            String w = words[id];
            int n = w.length(), tag = id << ID_SHIFT;
            pack(w, -1, -1, tag);
            for (int i = 0; i < n; i++) {
                pack(w, i, -1, tag | 1 << (2 * GAP_BITS) | i);
                // the second deleted letter, w[j + 1], sits in gap j of the rest
                for (int j = i; j < n - 1; j++)
                    pack(w, i, j + 1, tag | 2 << (2 * GAP_BITS) | i << GAP_BITS | j);
            }
        }
        // heads are replaced by their ranks so that one long holds a key
        long[] distinct = heads.clone();
        Arrays.sort(distinct);
        long[] keys = new long[total];
        for (int t = 0; t < total; t++)
            keys[t] = (long)Arrays.binarySearch(distinct, heads[t]) << TAIL_BITS | tails[t];
        heads = tails = distinct = null;
        Arrays.sort(keys);
        boolean[] found = new boolean[k];
        int start = 0;
        while (start < total) {
            int end = start + 1;
            while (end < total && keys[end] >> LOW_BITS == keys[start] >> LOW_BITS)
                end++;
            if (end - start > 1)
                markGroup(keys, start, end, found);
            start = end;
        }
        List<String> chosen = new ArrayList<>();
        for (int id = 0; id < k; id++)
            if (found[id])
                chosen.add(words[id]);
        Collections.sort(chosen);
        StringBuilder out = new StringBuilder().append(chosen.size()).append('\n');
        for (String w : chosen)
            out.append(w).append('\n');
        System.out.print(out);
    }

    // marks the words of one rest that have a close word in it; the keys of
    // one word differ in their gaps, so equal pairs come from different words
    static void markGroup(long[] keys, int start, int end, boolean[] found) {
        int[] lows = new int[end - start];
        for (int t = start; t < end; t++)
            lows[t - start] = (int)(keys[t] & ((1L << LOW_BITS) - 1));
        for (int l : lows)
            if ((l >> (2 * GAP_BITS) & CUT_MASK) == 0) {
                // the rest is a word itself, at most two deletions from every other
                for (int m : lows)
                    found[m >> ID_SHIFT] = true;
                return;
            }
        boolean[] gapsWith = new boolean[GAP_MASK + 1], nearGap = new boolean[GAP_MASK + 1];
        int firstSingle = -1;
        boolean many = false;
        List<Integer> doubles = new ArrayList<>();
        for (int l : lows) {
            if ((l >> (2 * GAP_BITS) & CUT_MASK) == 1) {
                gapsWith[l & GAP_MASK] = true;
                if (firstSingle < 0)
                    firstSingle = l >> ID_SHIFT;
                else if (firstSingle != l >> ID_SHIFT)
                    many = true;
            } else {
                doubles.add(l);
            }
        }
        // one deletion from each costs at most two edits
        if (many)
            for (int l : lows)
                if ((l >> (2 * GAP_BITS) & CUT_MASK) == 1)
                    found[l >> ID_SHIFT] = true;
        doubles.sort(Comparator.comparingInt(l -> l & PAIR_MASK));
        for (int a = 0; a < doubles.size(); a++) {
            int l = doubles.get(a), g1 = l >> GAP_BITS & GAP_MASK, g2 = l & GAP_MASK;
            // the same two gaps from another word: two substitutions
            boolean same =
                a > 0 && (doubles.get(a - 1) & PAIR_MASK) == (l & PAIR_MASK) ||
                a + 1 < doubles.size() && (doubles.get(a + 1) & PAIR_MASK) == (l & PAIR_MASK);
            // one more letter in a gap shared with a single deletion
            boolean near = gapsWith[g1] || gapsWith[g2];
            if (same || near)
                found[l >> ID_SHIFT] = true;
            if (near)
                nearGap[g1] = nearGap[g2] = true;
        }
        for (int l : lows)
            if ((l >> (2 * GAP_BITS) & CUT_MASK) == 1 && nearGap[l & GAP_MASK])
                found[l >> ID_SHIFT] = true;
    }
}
