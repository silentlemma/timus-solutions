import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  static final int CYCLE = 400, CENTURY = 100, LEAP_STEP = 4;
  static final int WEEK = 7, FRIDAY = 4, TARGET_DAY = 13;
  static final int MONTHS = 12, BUCKETS = MONTHS + 1;
  static final int[] MONTH_LENGTHS = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

  static int[] calendarTypes() {
    int weekday = 0;
    int[] types = new int[CYCLE];
    for (int year = 1; year <= CYCLE; year++) {
      boolean leap = year % CYCLE == 0 || (year % LEAP_STEP == 0 && year % CENTURY != 0);
      int count = 0;
      for (int month = 0; month < MONTHS; month++) {
        if ((weekday + TARGET_DAY - 1) % WEEK == FRIDAY)
          count++;
        int days = MONTH_LENGTHS[month] + (month == 1 && leap ? 1 : 0);
        weekday = (weekday + days) % WEEK;
      }
      types[year - 1] = count;
    }
    return types;
  }

  static long[] prefix(long year, int[] types, long[] cycleCounts) {
    long[] answer = new long[BUCKETS];
    for (int k = 0; k < BUCKETS; k++) answer[k] = year / CYCLE * cycleCounts[k];
    for (int i = 0; i < year % CYCLE; i++) answer[types[i]]++;
    return answer;
  }

  static long[] solve(long first, long last, int[] types, long[] cycleCounts) {
    long[] high = prefix(last, types, cycleCounts);
    long[] low = prefix(first - 1, types, cycleCounts);
    for (int k = 0; k < BUCKETS; k++) high[k] -= low[k];
    return high;
  }

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer fields = new StringTokenizer(in.readLine());
    long first = Long.parseLong(fields.nextToken()), last = Long.parseLong(fields.nextToken());
    int[] types = calendarTypes();
    long[] cycleCounts = new long[BUCKETS];
    for (int count : types) cycleCounts[count]++;
    long[] answer = solve(first, last, types, cycleCounts);
    StringBuilder out = new StringBuilder();
    for (int k = 0; k < BUCKETS; k++) out.append(k).append(": ").append(answer[k]).append('\n');
    System.out.print(out);
  }
}
