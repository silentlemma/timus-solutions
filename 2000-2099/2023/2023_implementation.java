import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
  static int solve(String[] names) {
    int position = 0;
    int steps = 0;
    for (String name : names) {
      char initial = name.charAt(0);
      int target = "APOR".indexOf(initial) >= 0 ? 0 : "BMS".indexOf(initial) >= 0 ? 1 : 2;
      steps += Math.abs(target - position);
      position = target;
    }
    return steps;
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
    int count = Integer.parseInt(readToken(in));
    String[] names = new String[count];
    for (int index = 0; index < count; index++) names[index] = readToken(in);
    System.out.println(solve(names));
  }
}
