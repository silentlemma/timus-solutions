import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long n = in.nextLong(), m = in.nextLong();
        // every full lap turns four times and peels two rows and two columns; the
        // spiral ends in the middle of the shorter side, so only that side counts
        System.out.println(n <= m ? 2 * (n - 1) : 2 * m - 1);
    }
}
