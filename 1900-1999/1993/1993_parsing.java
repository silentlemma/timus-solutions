import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Locale;

public class Main {
  private static final int ROLE_COUNT = 3;
  static String transform(String sentence) {
    String opening = "{([", closing = "})]";
    StringBuilder answer = new StringBuilder();
    for (String clause : sentence.toLowerCase(Locale.ROOT).split(",")) {
      String[] phrases = new String[ROLE_COUNT];
      String prefix = "";
      int i = 0;
      while (i < clause.length()) {
        int role = opening.indexOf(clause.charAt(i));
        if (role >= 0) {
          int end = clause.indexOf(closing.charAt(role), i + 1);
          phrases[role] = clause.substring(i + 1, end);
          i = end + 1;
        } else if (clause.charAt(i) >= 'a' && clause.charAt(i) <= 'z') {
          int begin = i;
          while (i < clause.length() && clause.charAt(i) >= 'a' && clause.charAt(i) <= 'z') ++i;
          prefix = clause.substring(begin, i);
        } else
          ++i;
      }
      if (answer.length() > 0)
        answer.append(", ");
      if (!prefix.isEmpty())
        answer.append(prefix).append(' ');
      answer.append(String.join(" ", phrases));
    }
    answer.setCharAt(0, Character.toUpperCase(answer.charAt(0)));
    return answer.toString();
  }
  public static void main(String[] args) throws Exception {
    BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    System.out.println(transform(input.readLine()));
  }
}
