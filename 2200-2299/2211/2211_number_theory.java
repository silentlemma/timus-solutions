import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    private static final long MIN_SUM_FACTOR = 3;
    private static final long QUADRATIC_FACTOR = 4;
    private static final long AREA_MULTIPLE = 6;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        long area = input.nextLong();
        if (area % AREA_MULTIPLE != 0) {
            System.out.println(0);
            return;
        }
        ArrayList<Long> values = new ArrayList<>();
        values.add(1L);
        long remaining = area;
        for (long prime = 2; prime * prime <= remaining; prime += prime == 2 ? 1 : 2) {
            int exponent = 0;
            while (remaining % prime == 0) {
                remaining /= prime;
                exponent += 2;
            }
            int size = values.size();
            long power = 1;
            for (int step = 0; step < exponent; ++step) {
                power *= prime;
                for (int i = 0; i < size; ++i) {
                    values.add(values.get(i) * power);
                }
            }
        }
        if (remaining > 1) {
            int size = values.size();
            for (int i = 0; i < size; ++i) {
                values.add(values.get(i) * remaining);
                values.add(values.get(i) * remaining * remaining);
            }
        }
        long[] divisors = new long[values.size()];
        for (int i = 0; i < divisors.length; ++i) {
            divisors[i] = values.get(i);
        }
        Arrays.sort(divisors);
        long square = area * area;
        long answer = 0;
        // Heron's variables satisfy x <= y <= z and xyz(x + y + z) = area squared.
        for (int i = 0; i < divisors.length; ++i) {
            long x = divisors[i];
            if (x > square / x / x / x / MIN_SUM_FACTOR) {
                break;
            }
            remaining = square / x;
            int left = i;
            int right = divisors.length;
            while (left < right) {
                int middle = (left + right) / 2;
                long y = divisors[middle];
                if (y <= remaining / y / (x + 2 * y)) {
                    left = middle + 1;
                } else {
                    right = middle;
                }
            }
            for (int j = i; j < left; ++j) {
                long y = divisors[j];
                if (remaining % y != 0) {
                    continue;
                }
                long total = x + y;
                long discriminant = total * total + QUADRATIC_FACTOR * (remaining / y);
                long root = (long) Math.sqrt(discriminant);
                while (root * root > discriminant) {
                    --root;
                }
                while ((root + 1) * (root + 1) <= discriminant) {
                    ++root;
                }
                if (root * root == discriminant && (root - total) % 2 == 0) {
                    ++answer;
                }
            }
        }
        System.out.println(answer);
    }
}
