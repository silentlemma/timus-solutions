import java.util.Scanner;

public class Main {
  private static final int PERCENT_SCALE = 100;
  static int[] construct(int size, int kept, int percentage) {
    int[] weights = new int[size];
    for (int i = 0; i < size; ++i) weights[i] = 1;
    for (int i = size - kept; i < size; ++i)
      weights[i] = weights[(percentage * i - 1) / PERCENT_SCALE] + 1;
    return weights;
  }
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int size = input.nextInt(), kept = input.nextInt(), percentage = input.nextInt();
    int[] weights = construct(size, kept, percentage);
    long total = 0;
    for (int value : weights) total += value;
    StringBuilder output = new StringBuilder();
    output.append(total).append('\n');
    for (int i = 0; i < size; ++i) {
      if (i > 0)
        output.append(' ');
      output.append(weights[i]);
    }
    output.append('\n');
    System.out.print(output);
  }
}
