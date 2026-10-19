import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  static final int WORD_BITS = Long.SIZE;

  static long intervalMask(int from, int to, int word) {
    int lo = Math.max(from - word * WORD_BITS, 0);
    int hi = Math.min(to - word * WORD_BITS, WORD_BITS);
    return (-1L << lo) & (hi == WORD_BITS ? -1L : (1L << hi) - 1);
  }

  static boolean same(long[] a, long[] b, int from, int to) {
    if (from == to)
      return true;
    for (int word = from / WORD_BITS; word <= (to - 1) / WORD_BITS; word++)
      if (((a[word] ^ b[word]) & intervalMask(from, to, word)) != 0)
        return false;
    return true;
  }

  static int firstOne(long[] bits, int from, int to) {
    for (int word = from / WORD_BITS; word <= (to - 1) / WORD_BITS; word++) {
      long present = bits[word] & intervalMask(from, to, word);
      if (present != 0)
        return word * WORD_BITS + Long.numberOfTrailingZeros(present);
    }
    return -1;
  }

  static int ones(long[] bits, int from, int to) {
    int count = 0;
    for (int word = from / WORD_BITS; word <= (to - 1) / WORD_BITS; word++)
      count += Long.bitCount(bits[word] & intervalMask(from, to, word));
    return count;
  }

  static long solve(String[] grid, int k) {
    int n = grid.length, m = grid[0].length();
    if (k > Math.min(n, m))
      return 0;
    long[][] rows = new long[n][(m + WORD_BITS - 1) / WORD_BITS];
    long[][] columns = new long[m][(n + WORD_BITS - 1) / WORD_BITS];
    short[][] rowZero = new short[n][m + 1], colZero = new short[m][n + 1];
    for (int r = 0; r < n; r++) {
      for (int c = 0; c < m; c++) {
        boolean black = grid[r].charAt(c) == '1';
        rowZero[r][c + 1] = black ? rowZero[r][c] : (short) (c + 1);
        colZero[c][r + 1] = black ? colZero[c][r] : (short) (r + 1);
        if (black) {
          rows[r][c / WORD_BITS] |= 1L << (c % WORD_BITS);
          columns[c][r / WORD_BITS] |= 1L << (r % WORD_BITS);
        }
      }
    }
    long answer = 0;
    for (int diagonal = 1 - n; diagonal < m; diagonal++) {
      int r0 = Math.max(0, -diagonal), c0 = Math.max(0, diagonal);
      int start = 0, pr = -1, pc = -1, br = 0, bc = 0;
      for (int at = 0; at < Math.min(n - r0, m - c0); at++) {
        int r = r0 + at, c = c0 + at;
        while (true) {
          int rs = r0 + start, cs = c0 + start;
          int last = rowZero[r][c] - 1;
          if (last < cs)
            last = -1;
          boolean valid = last < 0 || pr < 0 || same(rows[r], rows[pr], cs, c);
          if (valid) {
            int nrp = pr, ncp = pc;
            if (last >= 0) {
              nrp = r;
              if (pr < 0)
                ncp = last;
            }
            int lastRow = colZero[c][r + 1] - 1;
            if (lastRow < rs)
              lastRow = -1;
            valid = lastRow < 0 || nrp < 0 || same(columns[c], columns[ncp], rs, r + 1);
            if (valid) {
              if (lastRow >= 0) {
                nrp = lastRow;
                ncp = c;
              }
              int length = at - start + 1, nr, nc;
              if (pr >= 0) {
                nr = br + (grid[r].charAt(ncp) == '1' ? 1 : 0);
                nc = bc + (grid[nrp].charAt(c) == '1' ? 1 : 0);
              } else if (nrp < 0) {
                nr = nc = length;
              } else if (last >= 0) {
                nr = length - 1;
                nc = ones(rows[r], cs, c + 1);
              } else {
                nr = ones(columns[c], rs, r + 1);
                nc = length - 1;
              }
              if (nr <= k && nc <= k) {
                pr = nrp;
                pc = ncp;
                br = nr;
                bc = nc;
                break;
              }
            }
          }
          int oldSize = at - start;
          if (pr < 0 || pr == rs || pc == cs) {
            pr = pc = -1;
            br = bc = oldSize - 1;
          } else {
            if (grid[rs].charAt(pc) == '1')
              br--;
            if (grid[pr].charAt(cs) == '1')
              bc--;
          }
          start++;
        }
        int bound = at - start + 1;
        if (bound >= k && (pr < r - k + 1 || pc < c - k + 1))
          answer++;
        if (bound > k && br == k && bc == k && pr >= 0) {
          int firstR = firstOne(columns[pc], r0 + start, r + 1);
          int firstC = firstOne(rows[pr], c0 + start, c + 1);
          int high = Math.min(at - k, Math.min(firstR - r0, firstC - c0));
          high = Math.min(high, Math.min(pr - r0, pc - c0));
          if (high >= start)
            answer += high - start + 1;
        }
      }
    }
    return answer;
  }

  public static void main(String[] args) throws IOException {
    BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer header = new StringTokenizer(input.readLine());
    int n = Integer.parseInt(header.nextToken());
    header.nextToken();
    int k = Integer.parseInt(header.nextToken());
    String[] grid = new String[n];
    for (int i = 0; i < n; i++) grid[i] = input.readLine().trim();
    System.out.println(solve(grid, k));
  }
}
