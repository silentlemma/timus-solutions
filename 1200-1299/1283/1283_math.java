import java.math.BigInteger;
import java.util.*;

public class Main {
    static final int PERCENT = 100;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long gold = in.nextLong(), limit = in.nextLong();
        int fee = in.nextInt();
        // after k years the gold is gold * ((100 - fee) / 100)^k exactly, so
        // compare gold * (100 - fee)^k with limit * 100^k in whole numbers
        BigInteger left = BigInteger.valueOf(gold), right = BigInteger.valueOf(limit);
        BigInteger keep = BigInteger.valueOf(PERCENT - fee), all = BigInteger.valueOf(PERCENT);
        int years = 0;
        while (left.compareTo(right) > 0) {
            left = left.multiply(keep);
            right = right.multiply(all);
            years++;
        }
        System.out.println(years);
    }
}
