import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.math.BigInteger;

public class Main {
    static final int EDGES = 30;
    static final int COLOURS = 30;
    static final int ROTATIONS = 60;
    // the rotations other than the identity: how many there are and the cycle
    // length on the edges; a half-turn also keeps two edges in place
    static final int FACE_TURNS = 24;
    static final int FACE_CYCLE = 5;
    static final int VERTEX_TURNS = 20;
    static final int VERTEX_CYCLE = 3;
    static final int HALF_TURNS = 15;
    static final int HALF_CYCLE = 2;

    // colourings of cycles of this length that use each colour counts[c]
    // times, or 0 if some count does not split into whole cycles
    static BigInteger cycles(int[] counts, int length) {
        BigInteger ways = BigInteger.ONE;
        int used = 0;
        for (int c : counts) {
            if (c % length != 0) {
                return BigInteger.ZERO;
            }
            for (int i = 1; i <= c / length; i++) {
                used++;
                ways = ways.multiply(BigInteger.valueOf(used)).divide(BigInteger.valueOf(i));
            }
        }
        return ways;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        int[] counts = new int[COLOURS + 1];
        for (int i = 0; i < EDGES; i++) {
            in.nextToken();
            counts[(int) in.nval]++;
        }
        BigInteger total = cycles(counts, 1);
        total = total.add(BigInteger.valueOf(FACE_TURNS).multiply(cycles(counts, FACE_CYCLE)));
        total = total.add(BigInteger.valueOf(VERTEX_TURNS).multiply(cycles(counts, VERTEX_CYCLE)));
        // a half-turn: colour the two kept edges first, in order
        BigInteger kept = BigInteger.ZERO;
        for (int a = 0; a <= COLOURS; a++) {
            for (int b = 0; b <= COLOURS; b++) {
                int[] rest = counts.clone();
                rest[a]--;
                rest[b]--;
                if (rest[a] >= 0 && rest[b] >= 0) {
                    kept = kept.add(cycles(rest, HALF_CYCLE));
                }
            }
        }
        total = total.add(BigInteger.valueOf(HALF_TURNS).multiply(kept));
        System.out.println(total.divide(BigInteger.valueOf(ROTATIONS)));
    }
}
