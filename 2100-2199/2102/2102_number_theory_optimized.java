public class Main {
    static final int TARGET = 20, THREE = 3, FIVE = 5, SIX = 6, DECIMAL = 10;

    static long nextLong() throws java.io.IOException {
        int c = System.in.read();
        while (c >= 0 && c <= ' ')
            c = System.in.read();
        long n = 0;
        while (c >= '0' && c <= '9') {
            n = n * DECIMAL + c - '0';
            c = System.in.read();
        }
        return n;
    }

    static boolean enough(long n, long divisor, int needed) {
        long minimum = 1;
        for (int i = 0; i < needed; i++) {
            // Check before multiplication, so no intermediate can exceed n.
            if (minimum > n / divisor)
                return false;
            minimum *= divisor;
        }
        return true;
    }

    static boolean qualifies(long n) {
        int count = Long.numberOfTrailingZeros(n);
        n >>>= count;
        while (n % THREE == 0) {
            n /= THREE;
            count++;
        }
        if (count >= TARGET)
            return count == TARGET && n == 1;
        int remaining = TARGET - count;
        if (remaining <= 2) {
            long root = (long)Math.sqrt(n);
            if (root * root == n) {
                if (remaining != 2 || root < 2)
                    return false;
                long trial = FIVE, jump = 2;
                while (trial * trial <= root) {
                    if (root % trial == 0)
                        return false;
                    trial += jump;
                    jump = SIX - jump;
                }
                return true;
            }
        }
        long divisor = FIVE, step = 2;
        while (count < TARGET && divisor * divisor <= n) {
            // All remaining prime factors are at least this untested divisor.
            if (TARGET - count > 2 && !enough(n, divisor, TARGET - count))
                break;
            while (n % divisor == 0) {
                n /= divisor;
                count++;
            }
            divisor += step;
            step = SIX - step;
        }
        if (n > 1 && divisor * divisor > n) {
            count++;
            n = 1;
        }
        return count == TARGET && n == 1;
    }

    public static void main(String[] args) throws java.io.IOException {
        if (qualifies(nextLong())) {
            byte[] answer = {'Y', 'e', 's', '\n'};
            System.out.write(answer);
        } else {
            byte[] answer = {'N', 'o', '\n'};
            System.out.write(answer);
        }
    }
}
