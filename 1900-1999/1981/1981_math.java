import java.io.IOException;

public class Main {
  private static final long FORBIDDEN_CHOICES = 3;

  private static long[] count(long n) {
    if (n % 2 != 0) {
      long size = (n - FORBIDDEN_CHOICES) / 2;
      return new long[] {size >= 2 ? n * size : 0, 0};
    }
    long half = n / 2, first = half - 1, second = half - 2;
    long parallel = half * ((first >= 2 ? first : 0) + (second >= 2 ? second : 0));
    return new long[] {parallel, half * (n - FORBIDDEN_CHOICES)};
  }

  private static long readN() throws IOException {
    int c;
    do {
      c = System.in.read();
    } while (c >= 0 && c <= ' ');
    if (c < 0)
      return -1;
    long n = 0;
    while (c > ' ') {
      n = n * 10 + c - '0';
      c = System.in.read();
    }
    return n;
  }

  public static void main(String[] args) throws IOException {
    long n = readN();
    if (n < 0)
      return;
    long[] answer = count(n);
    System.out.println(answer[0] + " " + answer[1]);
  }
}
