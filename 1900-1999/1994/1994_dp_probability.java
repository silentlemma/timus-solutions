import java.util.Locale;
import java.util.Scanner;

public class Main {
  static double[][] build(int limit, int maximumSpies) {
    double[][] choose = new double[limit + 1][];
    for (int size = 0; size <= limit; ++size) {
      choose[size] = new double[size + 1];
      choose[size][0] = choose[size][size] = 1;
      for (int j = 1; j < size; ++j)
        choose[size][j] = choose[size - 1][j - 1] + choose[size - 1][j];
    }
    double[][] table = new double[limit + 1][maximumSpies + 1];
    for (int size = 1; size <= limit; ++size) {
      table[size][0] = size;
      for (int spies = 1; spies <= Math.min(maximumSpies, size - 1); ++spies) {
        int loyal = size - spies;
        double best = 0;
        for (int retained = 1; retained < size; ++retained) {
          int lower = Math.max(0, retained - loyal), upper = Math.min(spies, (retained - 1) / 2);
          double weighted = 0;
          for (int remaining = lower; remaining <= upper; ++remaining) {
            weighted += choose[spies][remaining] * choose[loyal][retained - remaining]
                * table[retained - remaining][remaining];
          }
          best = Math.max(best, weighted / choose[size][retained]);
        }
        table[size][spies] = best;
      }
    }
    return table;
  }
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int total = input.nextInt(), spies = input.nextInt();
    double answer = total <= 2 * spies ? 0 : build(total - spies, spies)[total - spies][spies];
    System.out.printf(Locale.US, "%.12f%n", answer);
  }
}
