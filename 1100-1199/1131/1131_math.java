import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long n = in.nextLong(), k = in.nextLong();
        // as long as fewer computers than cables have the program, each hour doubles
        // the count; after that k computers get it each hour
        long have = 1, hours = 0;
        while (have < n && have < k) {
            have *= 2;
            hours++;
        }
        if (have < n) {
            hours += (n - have + k - 1) / k;
        }
        System.out.println(hours);
    }
}
