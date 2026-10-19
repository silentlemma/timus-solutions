import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;

public class Main {
  // FNV-1a of the whole input seeds splitmix64; the arrangements are never
  // decoded, they only make the seed differ between tests
  private static final long FNV_OFFSET = 0xcbf29ce484222325L;
  private static final long FNV_PRIME = 0x100000001b3L;
  private static final long GOLDEN = 0x9e3779b97f4a7c15L;
  private static final long MIX_A = 0xbf58476d1ce4e5b9L;
  private static final long MIX_B = 0x94d049bb133111ebL;
  private static final int SHIFT_A = 30, SHIFT_B = 27, SHIFT_C = 31;
  private static final int CHUNK = 1 << 16;
  private static final int BYTE = 0xff;
  private static long state;

  private static long nextRandom() {
    state += GOLDEN;
    long z = state;
    z = (z ^ (z >>> SHIFT_A)) * MIX_A;
    z = (z ^ (z >>> SHIFT_B)) * MIX_B;
    return z ^ (z >>> SHIFT_C);
  }

  public static void main(String[] args) throws IOException {
    InputStream in = System.in;
    ByteArrayOutputStream all = new ByteArrayOutputStream();
    byte[] chunk = new byte[CHUNK];
    for (int read; (read = in.read(chunk)) > 0;) all.write(chunk, 0, read);
    byte[] input = all.toByteArray();
    state = FNV_OFFSET;
    for (byte c : input) state = (state ^ (c & BYTE)) * FNV_PRIME;
    int games = Integer.parseInt(new String(input, "US-ASCII").trim().split("\\s+")[0]);
    StringBuilder out = new StringBuilder();
    for (int game = 0; game < games; ++game) {
      int n = game + 2;
      // a bubble sort network: every white ball ends left of every black one
      for (int end = n - 1; end >= 1; --end)
        for (int i = 1; i <= end; ++i)
          out.append("? ").append(i).append(' ').append(i + 1).append('\n');
      int j = 1 + (int) Long.remainderUnsigned(nextRandom(), n - 1);
      out.append("! ").append(j).append(' ').append(j + 1).append('\n');
    }
    System.out.print(out);
  }
}
