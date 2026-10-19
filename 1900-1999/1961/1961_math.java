import java.util.Scanner;

public class Main {
  static long bestCount(long sample, long successes, long population) {
    return Math.min(population, successes * (population + 1) / sample);
  }

  public static void main(String[] args) {
    try (Scanner input = new Scanner(System.in)) {
      long sample = input.nextLong();
      long successes = input.nextLong();
      long population = input.nextLong();
      System.out.println(bestCount(sample, successes, population));
    }
  }
}
