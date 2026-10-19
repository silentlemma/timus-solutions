import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {
  private static final int RECORDS = 6;

  static class Record {
    final String model;
    final int price;
    Record(String name, int amount) {
      model = name;
      price = amount;
    }
  }

  static String solve(Record[] records) {
    Map<String, int[]> groups = new HashMap<>();
    for (Record record : records) {
      int[] stats = groups.get(record.model);
      if (stats == null) {
        stats = new int[] {0, record.price};
        groups.put(record.model, stats);
      }
      stats[0]++;
      stats[1] = Math.min(stats[1], record.price);
    }
    String answer = "";
    int bestCount = -1, bestPrice = 0;
    for (Map.Entry<String, int[]> entry : groups.entrySet()) {
      String model = entry.getKey();
      int count = entry.getValue()[0], price = entry.getValue()[1];
      if (count > bestCount || count == bestCount && price < bestPrice
          || count == bestCount && price == bestPrice && model.compareTo(answer) < 0) {
        answer = model;
        bestCount = count;
        bestPrice = price;
      }
    }
    return answer;
  }

  public static void main(String[] args) throws IOException {
    BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    Record[] records = new Record[RECORDS];
    for (int i = 0; i < RECORDS; i++) {
      if (input.readLine() == null)
        return;
      String model = input.readLine();
      int price = Integer.parseInt(input.readLine().trim());
      records[i] = new Record(model, price);
    }
    System.out.println(solve(records));
  }
}
