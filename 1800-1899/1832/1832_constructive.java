import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // m, the least number not dividing n, divides no proper divisor
        // either, so colouring by x mod m separates every two artists d
        // apart; m <= 13 since lcm(1, ..., 13) exceeds 300000
        int m = 2;
        while (n % m == 0) {
            m++;
        }
        int p = 2;
        while (n % p != 0) {
            p++;
        }
        // the wrap-around neighbours are n - d apart, at least n - n/p; the
        // last n/p artists get a second palette, so no gap inside either
        // part is that long and the parts never share a colour
        int front = n - n / p;
        char[] out = new char[n];
        for (int x = 0; x < n; x++) {
            out[x] = (char) ('a' + x % m + (x >= front ? m : 0));
        }
        System.out.println(new String(out));
    }
}
