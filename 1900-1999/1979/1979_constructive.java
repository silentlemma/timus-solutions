import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Main {
  private static final int FACE_COUNT = 6;
  private static final int HALF_FACES = 3;
  private static final int BAND_COUNT = 3;
  private static final int BELT_FACES = 4;

  private static int label(int n, int band, int row, int col) {
    int area = n * n;
    int complement = FACE_COUNT * area + 1;
    if (band == 0)
      return 2 * area + row * n + col + 1;
    if (band == 2)
      return complement - (HALF_FACES * area - row * n - n + col + 1);
    int face = col / n;
    col %= n;
    if (face < 2)
      return face * area + row * n + col + 1;
    return complement - ((face - 2) * area + row * n + n - col);
  }

  private static void writeCube(int n, BufferedWriter out) throws IOException {
    for (int band = 0; band < BAND_COUNT; band++) {
      int width = band == 1 ? BELT_FACES * n : n;
      for (int row = 0; row < n; row++) {
        StringBuilder line = new StringBuilder();
        for (int col = 0; col < width; col++) {
          if (col > 0)
            line.append(' ');
          line.append(label(n, band, row, col));
        }
        out.write(line.toString());
        out.newLine();
      }
    }
  }

  private static int readN() throws IOException {
    int c;
    do {
      c = System.in.read();
    } while (c >= 0 && c <= ' ');
    if (c < 0)
      return -1;
    int n = 0;
    while (c > ' ') {
      n = n * 10 + c - '0';
      c = System.in.read();
    }
    return n;
  }

  public static void main(String[] args) throws IOException {
    int n = readN();
    if (n < 0)
      return;
    BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
    writeCube(n, out);
    out.flush();
  }
}
