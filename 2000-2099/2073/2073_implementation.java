import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
  private static final int NAME_WIDTH = 30;
  private static final int DATE_WIDTH = 8;
  private static final String LETTERS = "ABCDEFGHIJKLM";

  private static String repeat(char c, int count) {
    char[] chars = new char[count];
    Arrays.fill(chars, c);
    return new String(chars);
  }

  private static String pad(String s, int width) {
    return s + repeat(' ', width - s.length());
  }

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder out = new StringBuilder();
    String border = "+" + repeat('-', NAME_WIDTH) + "+" + repeat('-', DATE_WIDTH) + "+"
        + repeat('-', LETTERS.length()) + "+\n";
    out.append(border);
    out.append('|').append(pad("Contest name", NAME_WIDTH)).append('|')
        .append(pad("Date", DATE_WIDTH)).append('|').append(LETTERS).append("|\n");
    out.append(border);
    int n = Integer.parseInt(in.readLine().trim());
    for (int c = 0; c < n; c++) {
      String name = in.readLine().trim();
      String date = in.readLine().trim();
      String[] counts = in.readLine().trim().split("\\s+");
      int p = Integer.parseInt(counts[0]);
      int s = Integer.parseInt(counts[1]);
      // '.' for a given problem, 'x' once submitted, 'o' once accepted
      char[] marks = (repeat('.', p) + repeat(' ', LETTERS.length() - p)).toCharArray();
      for (int k = 0; k < s; k++) {
        String submit = in.readLine().trim();
        int i = submit.charAt(0) - 'A';
        if (submit.substring(2).equals("Accepted")) marks[i] = 'o';
        else if (marks[i] != 'o') marks[i] = 'x';
      }
      out.append('|').append(pad(name, NAME_WIDTH)).append('|').append(date).append('|')
          .append(marks).append("|\n");
      out.append(border);
    }
    System.out.print(out);
  }
}
