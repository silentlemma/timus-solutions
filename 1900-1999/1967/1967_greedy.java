import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {
  static final int DECIMAL_BASE = 10;

  static String timesTen(String value) {
    int carry = 0;
    StringBuilder result = new StringBuilder();
    for (int i = value.length() - 1; i >= 0; i--) {
      carry += (value.charAt(i) - '0') * DECIMAL_BASE;
      result.append((char) ('0' + carry % 2));
      carry /= 2;
    }
    while (carry > 0) {
      result.append((char) ('0' + carry % 2));
      carry /= 2;
    }
    return result.reverse().toString();
  }

  static boolean lessSuffix(String bits, int start, String threshold) {
    for (int i = 0; i < threshold.length(); i++) {
      char actual = bits.charAt(start + i), limit = threshold.charAt(i);
      if (actual != limit)
        return actual < limit;
    }
    return false;
  }

  static List<Integer> optimalLengths(String bits) {
    List<String> powers = new ArrayList<>();
    List<Integer> lengths = new ArrayList<>();
    String power = "1";
    int end = bits.length();
    while (end > 0) {
      int index = 0;
      while (true) {
        if (index == powers.size()) {
          power = timesTen(power);
          powers.add(power);
        }
        String threshold = powers.get(index);
        int length = threshold.length();
        if (length >= end) {
          lengths.add(end);
          Collections.reverse(lengths);
          return lengths;
        }
        int start = end - length;
        if (bits.charAt(start) == '1' && lessSuffix(bits, start, threshold)) {
          lengths.add(length);
          end = start;
          break;
        }
        index++;
      }
    }
    Collections.reverse(lengths);
    return lengths;
  }

  static String makeBits(int maximum) {
    StringBuilder bits = new StringBuilder();
    for (int value = 1; value <= maximum; value++) {
      for (int bit = Integer.highestOneBit(value); bit > 0; bit >>= 1) {
        bits.append((value & bit) == 0 ? '0' : '1');
      }
    }
    return bits.toString();
  }

  public static void main(String[] args) {
    try (Scanner input = new Scanner(System.in)) {
      int maximum = input.nextInt();
      List<Integer> lengths = optimalLengths(makeBits(maximum));
      StringBuilder output = new StringBuilder();
      output.append(lengths.size()).append('\n');
      for (int length : lengths) output.append(length).append(' ');
      output.append('\n');
      System.out.print(output);
    }
  }
}
