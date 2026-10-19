import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
  static final int WIDTH = 10;
  static final int ROWS = 4;
  static final String[] DAYS = {"Tuesday", "Thursday", "Saturday"};

  static List<String> wrap(String name) {
    List<String> lines = new ArrayList<>();
    lines.add("");
    for (String word : name.split(" ")) {
      int last = lines.size() - 1;
      String current = lines.get(last);
      if (current.isEmpty())
        lines.set(last, word);
      else if (current.length() + 1 + word.length() <= WIDTH)
        lines.set(last, current + " " + word);
      else
        lines.add(word);
    }
    return lines;
  }

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(in.readLine());
    List<List<List<String>>> grid = new ArrayList<>();
    for (int row = 0; row < ROWS; row++) {
      List<List<String>> cells = new ArrayList<>();
      for (int column = 0; column < DAYS.length; column++) cells.add(new ArrayList<>());
      grid.add(cells);
    }
    for (int course = 0; course < n; course++) {
      String name = in.readLine();
      String[] slot = in.readLine().split(" ");
      int lesson = Integer.parseInt(slot[1]);
      for (int column = 0; column < DAYS.length; column++)
        if (DAYS[column].equals(slot[0]))
          grid.get(lesson - 1).set(column, wrap(name));
    }
    StringBuilder boundary = new StringBuilder("+");
    for (int column = 0; column < DAYS.length; column++) {
      for (int at = 0; at < WIDTH; at++) boundary.append('-');
      boundary.append('+');
    }
    String border = boundary.toString();
    StringBuilder output = new StringBuilder(border).append('\n');
    for (List<List<String>> row : grid) {
      int height = 1;
      for (List<String> cell : row) height = Math.max(height, cell.size());
      for (int level = 0; level < height; level++) {
        output.append('|');
        for (List<String> cell : row) {
          String line = level < cell.size() ? cell.get(level) : "";
          output.append(line);
          for (int at = line.length(); at < WIDTH; at++) output.append(' ');
          output.append('|');
        }
        output.append('\n');
      }
      output.append(border).append('\n');
    }
    System.out.print(output);
  }
}
