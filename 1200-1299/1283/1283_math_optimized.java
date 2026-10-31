import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int BASE = 1000000000;
    private static final int PERCENT = 100;

    private static class Number {
        // mutable base-billion limbs avoid allocating a big integer every year.
        int[] digits = new int[2];
        int size;

        Number(long value) {
            do {
                digits[size++] = (int)(value % BASE);
                value /= BASE;
            } while (value != 0);
        }

        void multiply(int factor) {
            // each limb is below 10^9 and the multiplier is at most 100.
            long carry = 0;
            for (int i = 0; i < size; i++) {
                long value = (long)digits[i] * factor + carry;
                digits[i] = (int)(value % BASE);
                carry = value / BASE;
            }
            if (carry != 0) {
                if (size == digits.length) {
                    digits = Arrays.copyOf(digits, size * 2);
                }
                digits[size++] = (int)carry;
            }
        }

        boolean greater(Number other) {
            if (size != other.size) {
                return size > other.size;
            }
            for (int i = size - 1; i >= 0; i--) {
                if (digits[i] != other.digits[i]) {
                    return digits[i] > other.digits[i];
                }
            }
            return false;
        }
    }

    private static int readInt() throws IOException {
        // three integers need no scanner or token allocations.
        int c;
        do {
            c = System.in.read();
        } while (c >= 0 && c <= ' ');
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        // after k years the gold is gold * ((100 - fee) / 100)^k exactly, so
        // compare gold * (100 - fee)^k with limit * 100^k in whole numbers
        Number left = new Number(readInt()), right = new Number(readInt());
        int fee = readInt();
        int years = 0;
        while (left.greater(right)) {
            left.multiply(PERCENT - fee);
            right.multiply(PERCENT);
            years++;
        }
        System.out.println(years);
    }
}
