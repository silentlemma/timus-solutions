import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;
import java.util.TreeSet;

public class Main {
    // the cells a ship may not use: rows top..bottom, columns left..right
    static class Zone implements Comparable<Zone> {
        final long top, bottom, left, right;

        Zone(long top, long bottom, long left, long right) {
            this.top = top;
            this.bottom = bottom;
            this.left = left;
            this.right = right;
        }

        public int compareTo(Zone o) { return Long.compare(left, o.left); }
    }

    // Places for a ship lying along the rows of a rows x cols board.
    static long countLines(long rows, long cols, List<Zone> zones, long k) {
        TreeSet<Long> cuts = new TreeSet<>();
        cuts.add(1L);
        cuts.add(rows + 1);
        for (Zone z : zones) {
            for (long e : new long[] {z.top, z.bottom + 1}) {
                if (e > 1 && e <= rows) {
                    cuts.add(e);
                }
            }
        }
        Long[] c = cuts.toArray(new Long[0]);
        long total = 0;
        // rows between two cuts meet the same zones, so they count the same
        for (int i = 0; i + 1 < c.length; i++) {
            long top = c[i];
            List<Zone> spans = new ArrayList<>();
            for (Zone z : zones) {
                if (z.top <= top && top <= z.bottom) {
                    spans.add(z);
                }
            }
            Collections.sort(spans);
            spans.add(new Zone(0, 0, cols + 1, cols + 1));
            long free = 0, start = 1;
            for (Zone s : spans) {
                if (s.left > start) {
                    free += Math.max(0, s.left - start - k + 1);
                }
                start = Math.max(start, s.right + 1);
            }
            total += free * (c[i + 1] - top);
        }
        return total;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long n = in.nextLong(), m = in.nextLong();
        int ships = in.nextInt();
        List<Zone> zones = new ArrayList<>(), flipped = new ArrayList<>();
        for (int i = 0; i < ships; i++) {
            long col = in.nextLong(), row = in.nextLong(), size = in.nextLong();
            boolean vertical = in.next().equals("V");
            long bottom = vertical ? row + size - 1 : row;
            long right = vertical ? col : col + size - 1;
            // no other ship may touch this one, even at a corner
            zones.add(new Zone(row - 1, bottom + 1, col - 1, right + 1));
            flipped.add(new Zone(col - 1, right + 1, row - 1, bottom + 1));
        }
        long k = in.nextLong();
        long total = countLines(n, m, zones, k);
        if (k > 1) {
            total += countLines(m, n, flipped, k);
        }
        System.out.println(total);
    }
}
