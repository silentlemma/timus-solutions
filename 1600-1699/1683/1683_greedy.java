import java.util.Scanner;
import java.util.StringJoiner;

public class Main {
    public static void main(String[] args) {
        long n = new Scanner(System.in).nextLong();
        // a fold of x cm needs x <= length - x, so a strip shrinks at best to
        // half its length, rounded up; folding exactly half each time reaches that
        StringJoiner folds = new StringJoiner(" ");
        int count = 0;
        while (n > 1) {
            folds.add(Long.toString(n / 2));
            n -= n / 2;
            count++;
        }
        System.out.println(count);
        System.out.println(folds);
    }
}
