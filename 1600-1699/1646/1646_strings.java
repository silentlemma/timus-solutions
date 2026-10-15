import java.util.*;

public class Main {
    static final long MOD = 1000000007;
    static String pattern;
    static int edge; // letters kept at each end of a sample

    static long occurrences(String text) {
        long found = 0;
        for (int i = 0; i + pattern.length() <= text.length(); i++)
            if (text.startsWith(pattern, i))
                found++;
        return found;
    }

    static String head(String s) {
        return s.length() > edge ? s.substring(0, edge) : s;
    }

    static String tail(String s) {
        return s.length() > edge ? s.substring(s.length() - edge) : s;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        pattern = in.next();
        edge = pattern.length() - 1;
        // a sample: its count mod MOD and its first and last letters; the full
        // string can be 2^100 long
        List<long[]> counts = new ArrayList<>();
        List<String[]> ends = new ArrayList<>();
        for (int s = 0; s < 2; s++) {
            String dna = in.next();
            counts.add(new long[] {occurrences(dna)});
            ends.add(new String[] {head(dna), tail(dna)});
        }
        int m = in.nextInt();
        for (int k = 0; k < m; k++) {
            int i = in.nextInt() - 1, j = in.nextInt() - 1;
            String[] a = ends.get(i), b = ends.get(j);
            // every new occurrence crosses the seam, so it lies in these letters
            long seam = occurrences(a[1] + b[0]);
            counts.add(new long[] {(counts.get(i)[0] + counts.get(j)[0] + seam) % MOD});
            ends.add(new String[] {head(a[0] + b[0]), tail(a[1] + b[1])});
        }
        System.out.println(counts.get(counts.size() - 1)[0]);
    }
}
