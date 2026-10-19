import java.io.IOException;

public class Main {
    private static final int BUFFER_SIZE = 1 << 16;
    private static final int MEMORY_THRESHOLD = 1 << 16;
    private static final int STREAM_COUNT = 3;
    private static final long UNSIGNED_MASK = (1L << Integer.SIZE) - 1;
    private static final byte[] INPUT_BUFFER = new byte[BUFFER_SIZE];
    private static int inputPosition;
    private static int inputLength;

    private static int bitLength(long value) {
        return Math.max(1, Long.SIZE - Long.numberOfLeadingZeros(value));
    }

    private static class Frontier {
        private final int[] compact;
        private final long[] wide;
        final int size;
        final int massBits;
        final long mask;
        long maxCount;

        Frontier(int size, long remaining, long countBound) {
            this.size = size;
            massBits = bitLength(remaining);
            mask = (1L << massBits) - 1;
            // Large frontiers often need only one 32-bit word per state.
            if (massBits + bitLength(countBound) <= Integer.SIZE) {
                compact = new int[size];
                wide = null;
            } else {
                compact = null;
                wide = new long[size];
            }
        }

        long get(int index) {
            return compact == null ? wide[index] : compact[index] & UNSIGNED_MASK;
        }

        void set(int index, long mass, long count) {
            long packed = (count << massBits) | mass;
            if (compact == null) {
                wide[index] = packed;
            } else {
                compact[index] = (int) packed;
            }
            maxCount = Math.max(maxCount, count);
        }
    }

    private static int readInput() throws IOException {
        if (inputPosition == inputLength) {
            inputLength = System.in.read(INPUT_BUFFER);
            inputPosition = 0;
            if (inputLength < 0) {
                return -1;
            }
        }
        return INPUT_BUFFER[inputPosition++];
    }

    private static long nextLong() throws IOException {
        int character = readInput();
        while (character >= 0 && character <= ' ') {
            character = readInput();
        }
        long value = 0;
        while (character > ' ') {
            value = value * 10 + character - '0';
            character = readInput();
        }
        return value;
    }

    private static int lowerBound(Frontier values, long target) {
        int left = 0;
        int right = values.size;
        while (left < right) {
            int middle = left + (right - left) / 2;
            if ((values.get(middle) & values.mask) < target) {
                left = middle + 1;
            } else {
                right = middle;
            }
        }
        return left;
    }

    private static long merge(Frontier states, long mass, long remaining, Frontier next) {
        int currentSize = states.size;
        int massBits = states.massBits;
        long mask = states.mask;
        int baseEnd = lowerBound(states, remaining + 1);
        int reverseStart = lowerBound(states, mass - remaining);
        int forward = lowerBound(states, mass + 1);
        int reverse = forward - 1;
        int base = 0;
        int nextSize = 0;
        long answer = 0;
        boolean write = next != null;
        long sentinel = mass + remaining + 1;
        // Folding negative residuals gives three sorted streams.
        while (base < baseEnd || reverse >= reverseStart || forward < currentSize) {
            long key = sentinel;
            if (base < baseEnd) {
                key = states.get(base) & mask;
            }
            if (reverse >= reverseStart && mass - (states.get(reverse) & mask) < key) {
                key = mass - (states.get(reverse) & mask);
            }
            if (forward < currentSize && (states.get(forward) & mask) - mass < key) {
                key = (states.get(forward) & mask) - mass;
            }
            long count = 0;
            if (base < baseEnd && (states.get(base) & mask) == key) {
                if (write) {
                    count += states.get(base) >>> massBits;
                }
                base++;
            }
            if (reverse >= reverseStart && mass - (states.get(reverse) & mask) == key) {
                if (write) {
                    count += states.get(reverse) >>> massBits;
                }
                reverse--;
            }
            if (forward < currentSize && (states.get(forward) & mask) - mass == key) {
                if (write) {
                    count += states.get(forward) >>> massBits;
                }
                forward++;
            }
            if (key == 0) {
                answer += count;
            } else {
                if (write) {
                    next.set(nextSize, key, count);
                }
                nextSize++;
            }
        }
        return write ? answer : nextSize;
    }

    public static void main(String[] args) throws IOException {
        int size = (int) nextLong();
        long target = nextLong();
        long[] weights = new long[size];
        long remaining = 0;
        for (int index = 0; index < size; index++) {
            weights[index] = nextLong();
            remaining += weights[index];
        }
        target = target < remaining ? remaining - target : target - remaining;
        if (target > remaining) {
            System.out.println(0);
            return;
        }
        if (target == 0) {
            System.out.println(1);
            return;
        }

        Frontier states = new Frontier(1, remaining, 1);
        states.set(0, target, 1);
        long answer = 0;
        for (int index = size - 1; index >= 0; index--) {
            long mass = weights[index];
            remaining -= mass;
            // Count first so the next frontier needs no spare capacity.
            int nextSize = (int) merge(states, mass, remaining, null);
            Frontier next = new Frontier(nextSize, remaining, STREAM_COUNT * states.maxCount);
            answer += merge(states, mass, remaining, next);
            states = next;
            if (nextSize >= MEMORY_THRESHOLD) {
                System.gc();
            }
            if (nextSize == 0) {
                break;
            }
        }
        System.out.println(answer);
    }
}
