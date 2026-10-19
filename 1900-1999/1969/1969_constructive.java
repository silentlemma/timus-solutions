import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
  static final int SECONDS_PER_MINUTE = 60;
  static final int MINUTES_PER_HOUR = 60;
  static final int SECONDS_PER_HOUR = SECONDS_PER_MINUTE * MINUTES_PER_HOUR;
  static final int DECIMAL_BASE = 10;

  static class Schedule {
    final int duration, trips;
    final int[] departures;
    Schedule(int duration, int trips, int[] departures) {
      this.duration = duration;
      this.trips = trips;
      this.departures = departures;
    }
  }

  static Schedule recover(int first, int[] passages) {
    int count = passages.length, offset = passages[0] - first, last = passages[count - 1];
    int totalSpan = last - first + offset;
    boolean[] present = new boolean[last + 1];
    int[] marked = new int[last + 1];
    for (int time : passages) present[time] = true;
    int epoch = 0;
    for (int index = 1; index <= count / 2; index++) {
      int period = passages[index] - first + offset;
      if (period % 2 != 0 || period <= 2 * offset)
        continue;
      int trips = totalSpan / period;
      if (trips == 0 || count % (2 * trips) != 0)
        continue;
      int tramCount = count / (2 * trips), gap = period - 2 * offset;
      epoch++;
      int[] departures = new int[tramCount];
      int found = 0;
      boolean failed = false;
      for (int time : passages) {
        if (marked[time] == epoch)
          continue;
        int departure = time - offset;
        if (departure >= first + period || found == tramCount) {
          failed = true;
          break;
        }
        int outward = time;
        for (int trip = 0; trip < trips; trip++) {
          int returning = outward + gap;
          if (outward > last || returning > last || !present[outward] || !present[returning]
              || marked[outward] == epoch || marked[returning] == epoch) {
            failed = true;
            break;
          }
          marked[outward] = marked[returning] = epoch;
          outward += period;
        }
        if (failed)
          break;
        departures[found++] = departure;
      }
      if (!failed && found == tramCount)
        return new Schedule(period / 2, trips, departures);
    }
    throw new IllegalArgumentException("The guaranteed schedule was not found");
  }

  static int parseTime(String text) {
    String[] parts = text.split(":");
    return Integer.parseInt(parts[0]) * SECONDS_PER_HOUR
        + Integer.parseInt(parts[1]) * SECONDS_PER_MINUTE + Integer.parseInt(parts[2]);
  }

  static void appendPair(StringBuilder output, int value) {
    output.append((char) ('0' + value / DECIMAL_BASE));
    output.append((char) ('0' + value % DECIMAL_BASE));
  }

  static void appendTime(StringBuilder output, int value) {
    appendPair(output, value / SECONDS_PER_HOUR);
    output.append(':');
    appendPair(output, value / SECONDS_PER_MINUTE % MINUTES_PER_HOUR);
    output.append(':');
    appendPair(output, value % SECONDS_PER_MINUTE);
  }

  public static void main(String[] args) {
    try (Scanner input = new Scanner(System.in)) {
      int first = parseTime(input.next());
      List<Integer> times = new ArrayList<>();
      while (input.hasNext()) times.add(parseTime(input.next()));
      int[] passages = new int[times.size()];
      for (int i = 0; i < passages.length; i++) passages[i] = times.get(i);
      Schedule schedule = recover(first, passages);
      StringBuilder output = new StringBuilder();
      for (int departure : schedule.departures) {
        for (int step = 0; step <= 2 * schedule.trips; step++) {
          if (step > 0)
            output.append(' ');
          appendTime(output, departure + step * schedule.duration);
        }
        output.append('\n');
      }
      System.out.print(output);
    }
  }
}
