import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    private static final int MAX_MINUTES = 300;
    private static final int MAX_DIVISOR = MAX_MINUTES + 1;
    private static final int WHEEL_PRIMES = 6;
    private static final int USED_BITS = 6;
    private static final int INITIAL_CAPACITY = 1024;
    private static final int WORD_BITS = 32;
    private static final long HASH_MULTIPLIER = 0x9E3779B97F4A7C15L;
    private final int[] primeCounts = new int[MAX_DIVISOR * MAX_DIVISOR + 1];
    private final ArrayList<Integer> primes = new ArrayList<>();
    private final int[][] wheels = new int[WHEEL_PRIMES + 1][];
    private long[] keys = new long[INITIAL_CAPACITY];
    private int[] values = new int[INITIAL_CAPACITY];
    private int size;
    private int base;

    Main() {
        int limit = MAX_DIVISOR * MAX_DIVISOR;
        boolean[] composite = new boolean[limit + 1];
        composite[0] = composite[1] = true;
        for (int divisor = 2; divisor * divisor <= limit; ++divisor) {
            if (!composite[divisor]) {
                for (int number = divisor * divisor; number <= limit; number += divisor) {
                    composite[number] = true;
                }
            }
        }
        for (int number = 1; number <= limit; ++number) {
            primeCounts[number] = primeCounts[number - 1] + (composite[number] ? 0 : 1);
            if (number <= MAX_DIVISOR && !composite[number])
                primes.add(number);
        }
        wheels[0] = new int[] {0, 1};
        int period = 1;
        for (int used = 1; used <= WHEEL_PRIMES; ++used) {
            period *= primes.get(used - 1);
            boolean[] blocked = new boolean[period + 1];
            for (int index = 0; index < used; ++index) {
                int divisor = primes.get(index);
                for (int number = divisor; number <= period; number += divisor) {
                    blocked[number] = true;
                }
            }
            int[] prefix = new int[period + 1];
            for (int number = 1; number <= period; ++number) {
                prefix[number] = prefix[number - 1] + (blocked[number] ? 0 : 1);
            }
            wheels[used] = prefix;
        }
    }

    private int slot(long key) {
        long mixed = key * HASH_MULTIPLIER;
        int index = (int)(mixed ^ (mixed >>> WORD_BITS)) & (keys.length - 1);
        while (keys[index] != 0 && keys[index] != key)
            index = (index + 1) & (keys.length - 1);
        return index;
    }

    private void put(long key, int value) {
        if (2 * (size + 1) > keys.length) {
            long[] oldKeys = keys;
            int[] oldValues = values;
            keys = new long[oldKeys.length * 2];
            values = new int[keys.length];
            size = 0;
            for (int index = 0; index < oldKeys.length; ++index) {
                if (oldKeys[index] != 0)
                    put(oldKeys[index], oldValues[index]);
            }
        }
        int index = slot(key);
        if (keys[index] == 0)
            ++size;
        keys[index] = key;
        values[index] = value;
    }

    private int phi(int value, int remaining) {
        if (remaining == base) {
            int[] prefix = wheels[base];
            int period = prefix.length - 1;
            return value / period * prefix[period] + prefix[value % period];
        }
        if (value == 0)
            return 0;
        int last = primes.get(remaining - 1);
        if (value < last)
            return 1;
        if (value < last * last)
            return 1 + primeCounts[value] - remaining;
        long key = ((long)value << USED_BITS) | remaining;
        int index = slot(key);
        if (keys[index] != 0)
            return values[index];
        int result = phi(value, remaining - 1) - phi(value / last, remaining - 1);
        put(key, result);
        return result;
    }

    int countYears(int start, int duration, int minutes) {
        int limit = minutes + 1;
        int used = primeCounts[limit];
        base = Math.min(used, WHEEL_PRIMES);
        Arrays.fill(keys, 0);
        size = 0;
        int finish = start + duration;
        int result = phi(finish, used) - phi(start, used);
        return result + primeCounts[Math.min(finish, limit)] - primeCounts[Math.min(start, limit)];
    }

    static int nextInt(BufferedInputStream in) throws IOException {
        int ch;
        do {
            ch = in.read();
        } while (ch <= ' ' && ch != -1);
        int value = 0;
        while (ch > ' ') {
            value = value * 10 + ch - '0';
            ch = in.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream in = new BufferedInputStream(System.in);
        int start = nextInt(in), duration = nextInt(in), minutes = nextInt(in);
        Main counter = new Main();
        System.out.println(counter.countYears(start, duration, minutes));
    }
}
