import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    private static final long FIRST_ODD_PRIME = 3;

    private static long coprimeCount(long bound, int index, List<Long> primes, boolean oddOnly) {
        if (bound == 0) {
            return 0;
        }
        if (index == primes.size()) {
            return oddOnly ? (bound + 1) / 2 : bound;
        }
        return coprimeCount(bound, index + 1, primes, oddOnly)
                - coprimeCount(bound / primes.get(index), index + 1, primes, oddOnly);
    }

    private static long countSizes(long first, long limit) {
        long oddPart = first;
        while (oddPart % 2 == 0) {
            oddPart /= 2;
        }
        List<Long> primes = new ArrayList<>();
        for (long divisor = FIRST_ODD_PRIME; divisor * divisor <= oddPart; divisor += 2) {
            if (oddPart % divisor == 0) {
                primes.add(divisor);
                while (oddPart % divisor == 0) {
                    oddPart /= divisor;
                }
            }
        }
        if (oddPart > 1) {
            primes.add(oddPart);
        }
        boolean oddOnly = first % 2 == 0;
        long bound = oddOnly ? limit : limit / 2;
        return limit - coprimeCount(bound, 0, primes, oddOnly);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long first = in.nextLong();
        long limit = in.nextLong();
        System.out.println(countSizes(first, limit));
    }
}
