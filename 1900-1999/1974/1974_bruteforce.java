import java.io.IOException;
import java.io.InputStream;

public class Main {
  static final int OCTAVE_SIZE = 12;
  static final int PITCH_COUNT = 96;
  static final int DECIMAL_BASE = 10;
  static final int BUFFER_SIZE = 65536;
  static final String NATURAL_SCALE = "C D EF G A B";

  static class FastInput {
    final InputStream input = System.in;
    final byte[] buffer = new byte[BUFFER_SIZE];
    int position, length;

    int read() throws IOException {
      if (position == length) {
        length = input.read(buffer);
        position = 0;
        if (length < 0)
          return -1;
      }
      return buffer[position++];
    }

    int first() throws IOException {
      int c;
      do {
        c = read();
      } while (c >= 0 && c <= ' ');
      return c;
    }

    int nextInt() throws IOException {
      int c = first(), result = 0;
      while (c > ' ') {
        result = result * DECIMAL_BASE + c - '0';
        c = read();
      }
      return result;
    }

    int nextPitch() throws IOException {
      int octave = first() - '1';
      int pitch = octave * OCTAVE_SIZE + NATURAL_SCALE.indexOf(read());
      int accidental = read();
      if (accidental > ' ') {
        pitch += accidental == '+' ? 1 : -1;
        read();
      }
      return pitch;
    }
  }

  static int[][] sourcePositions(int[] source) {
    int[] sizes = new int[PITCH_COUNT];
    for (int pitch : source) sizes[pitch]++;
    int[][] positions = new int[PITCH_COUNT][];
    for (int pitch = 0; pitch < PITCH_COUNT; pitch++) positions[pitch] = new int[sizes[pitch]];
    int[] cursor = new int[PITCH_COUNT];
    for (int i = 0; i < source.length; i++) {
      int pitch = source[i];
      positions[pitch][cursor[pitch]++] = i;
    }
    return positions;
  }

  static int absoluteSimilarity(int[][] positions, int sourceLength, int[] song) {
    int[] counts = new int[sourceLength + song.length - 1];
    for (int j = 0; j < song.length; j++) {
      int offset = song.length - 1 - j;
      for (int i : positions[song[j]]) counts[i + offset]++;
    }
    int best = 0;
    for (int count : counts) best = Math.max(best, count);
    return best;
  }

  public static void main(String[] args) throws IOException {
    FastInput in = new FastInput();
    int n = in.nextInt();
    int[] source = new int[n];
    for (int i = 0; i < n; i++) source[i] = in.nextPitch();
    int[][] positions = sourcePositions(source);
    int melodies = in.nextInt();
    StringBuilder out = new StringBuilder();
    for (int melody = 0; melody < melodies; melody++) {
      int length = in.nextInt();
      int[] song = new int[length];
      for (int i = 0; i < length; i++) song[i] = in.nextPitch();
      int best = absoluteSimilarity(positions, n, song);
      out.append((double) best / length).append('\n');
    }
    System.out.print(out);
  }
}
