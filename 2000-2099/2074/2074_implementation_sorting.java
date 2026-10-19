import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.TreeSet;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    List<String> path = new ArrayList<>(); // names of the current topic and its ancestors
    Map<Integer, TreeSet<String>> topics = new TreeMap<>(); // problem -> its topics
    String current = "";
    for (String line = in.readLine(); line != null; line = in.readLine()) {
      String trimmed = line.trim();
      if (trimmed.isEmpty()) continue;
      String[] words = trimmed.split("\\s+");
      if (words[0].endsWith(".")) {
        // a heading "1.2. name": its depth is the number of dots
        int depth = words[0].length() - words[0].replace(".", "").length();
        while (path.size() >= depth) path.remove(path.size() - 1);
        StringBuilder name = new StringBuilder();
        for (int i = 1; i < words.length; i++) name.append(i > 1 ? " " : "").append(words[i]);
        path.add(name.toString());
        current = String.join(".", path);
      } else {
        for (String w : words) {
          topics.computeIfAbsent(Integer.parseInt(w), k -> new TreeSet<>()).add(current);
        }
      }
    }
    // problems are visited in increasing order
    Map<String, List<Integer>> groups = new TreeMap<>();
    for (Map.Entry<Integer, TreeSet<String>> e : topics.entrySet()) {
      String key = String.join(", ", e.getValue());
      groups.computeIfAbsent(key, k -> new ArrayList<>()).add(e.getKey());
    }
    List<String> lines = new ArrayList<>();
    for (Map.Entry<String, List<Integer>> e : groups.entrySet()) {
      StringBuilder s = new StringBuilder();
      for (int p : e.getValue()) s.append(s.length() > 0 ? ", " : "").append(p);
      lines.add(s + " : " + e.getKey());
    }
    Collections.sort(lines);
    StringBuilder out = new StringBuilder();
    for (String s : lines) out.append(s).append('\n');
    System.out.print(out);
  }
}
