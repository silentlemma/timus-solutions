import java.util.Scanner;

public class Main {
  static long minimumCommon(long population, long[] lowerBounds) {
    long answer = population;
    for (long lower : lowerBounds) answer -= population - lower;
    return Math.max(0, answer);
  }

  public static void main(String[] args) {
    try (Scanner input = new Scanner(System.in)) {
      long population = input.nextLong();
      int count = input.nextInt();
      long[] lowerBounds = new long[count];
      for (int i = 0; i < count; i++) lowerBounds[i] = input.nextLong();
      System.out.println(minimumCommon(population, lowerBounds));
    }
  }
}
