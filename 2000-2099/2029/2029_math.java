import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
  static final int PEG_SUM = 3;

  static long solve(String state) {
    int source = 0;
    long answer = 0;
    for (int disk = state.length() - 1; disk >= 0; disk--) {
      int target = state.charAt(disk) - 'A';
      if (target != source) {
        answer += 1L << disk;
        source = PEG_SUM - source - target;
      }
    }
    return answer;
  }

  static String readToken(BufferedInputStream in) throws IOException {
    StringBuilder token = new StringBuilder();
    int character;
    do {
      character = in.read();
    } while (character >= 0 && character <= ' ');
    while (character > ' ') {
      token.append((char) character);
      character = in.read();
    }
    return token.toString();
  }

  public static void main(String[] args) throws IOException {
    BufferedInputStream in = new BufferedInputStream(System.in);
    readToken(in);
    System.out.println(solve(readToken(in)));
  }
}
