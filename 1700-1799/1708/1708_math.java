import java.io.IOException;
import java.util.Arrays;

public class Main {
    // This bound covers the obstructions and fixed parts for bases up to 36.
    static final int LONGEST = 15;
    static final int SHIFT = 6;
    static final int DIGIT_MASK = (1 << SHIFT) - 1;
    static final int INITIAL_FORBIDDEN = 1 << 15;
    static final int INITIAL_OUTPUT = 1 << 20;
    static final int INITIAL_LINES = 1 << 16;
    static final int INPUT_BUFFER = 1 << 10;
    static final String DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    static final class Output {
        final int base;
        final int[] counts;
        byte[] bytes = new byte[INITIAL_OUTPUT];
        int[] starts = new int[INITIAL_LINES];
        int size;
        int lines;

        Output(int base) {
            this.base = base;
            counts = new int[base];
        }

        void append(int value) {
            if (size == bytes.length) {
                bytes = Arrays.copyOf(bytes, size * 2);
            }
            bytes[size++] = (byte) value;
        }

        void emit(int word, int first, int second, int[] words) {
            Arrays.fill(counts, 0);
            for (int rest = word; rest != 0; rest = words[rest] >>> SHIFT) {
                counts[words[rest] & DIGIT_MASK]++;
            }
            if (lines + 1 == starts.length) {
                starts = Arrays.copyOf(starts, starts.length * 2);
            }
            starts[lines++] = size;
            for (int digit = 1; digit < base; digit++) {
                if (digit == first || digit == second) {
                    append(DIGITS.charAt(digit));
                    append('*');
                } else {
                    for (int c = 0; c < counts[digit]; c++) {
                        append(DIGITS.charAt(digit));
                    }
                }
            }
            append('\n');
            starts[lines] = size;
        }

        int compare(int a, int b) {
            int i = starts[a];
            int j = starts[b];
            while (bytes[i] == bytes[j]) {
                if (bytes[i] == '\n') {
                    return 0;
                }
                i++;
                j++;
            }
            return bytes[i] - bytes[j];
        }

        // Recurse only into the smaller partition to bound stack space.
        void sort(int[] order, int low, int high) {
            while (low < high) {
                int i = low;
                int j = high;
                int pivot = order[low + (high - low) / 2];
                while (i <= j) {
                    while (compare(order[i], pivot) < 0) {
                        i++;
                    }
                    while (compare(order[j], pivot) > 0) {
                        j--;
                    }
                    if (i <= j) {
                        int swap = order[i];
                        order[i++] = order[j];
                        order[j--] = swap;
                    }
                }
                if (j - low < high - i) {
                    sort(order, low, j);
                    low = i;
                } else {
                    sort(order, i, high);
                    high = j;
                }
            }
        }

        void write() throws IOException {
            int[] order = new int[lines];
            for (int i = 0; i < lines; i++) {
                order[i] = i;
            }
            sort(order, 0, lines - 1);
            byte[] sorted = new byte[size];
            int at = 0;
            for (int line : order) {
                int length = starts[line + 1] - starts[line];
                System.arraycopy(bytes, starts[line], sorted, at, length);
                at += length;
            }
            System.out.write(sorted);
        }
    }

    static Output solve(int base) {
        int maxDigit = base - 1;
        int width = LONGEST * maxDigit * maxDigit + 1;
        int[] offsets = new int[LONGEST * maxDigit + 1];
        int total = 0;
        // Convexity bounds each row's square sums; their parity is fixed.
        for (int sum = 0; sum < offsets.length; sum++) {
            int a = sum / LONGEST;
            int r = sum % LONGEST;
            int low = LONGEST * a * a + r * (2 * a + 1);
            a = sum / maxDigit;
            r = sum % maxDigit;
            int high = a * maxDigit * maxDigit + r * r;
            offsets[sum] = total - low / 2;
            total += (high - low) / 2 + 1;
        }
        int[] where = new int[total];
        Arrays.fill(where, -1);
        where[0] = 0;
        // A word stores its parent index and last digit; runs skips equal digits.
        int[] words = new int[total];
        int[] keys = new int[total];
        int[] runs = new int[total];
        long[] allowed = new long[total];
        long allRays = (1L << base) - 2;
        long allPairs = (1L << maxDigit) - 2;
        allowed[0] = allRays;
        int begin = 0;
        int end = 1;
        int size = 1;
        int[] forbidden = new int[INITIAL_FORBIDDEN];
        int[] forbiddenKeys = new int[INITIAL_FORBIDDEN];
        int forbiddenSize = 0;
        // First visits in breadth first lexicographic order are least words.
        // Deletion masks discard extensions containing a smaller obstruction.
        for (int length = 0; length < LONGEST; length++) {
            for (int r = begin; r < end; r++) {
                int sum = keys[r] / width;
                int square = keys[r] % width;
                int word = words[r];
                int last = word & DIGIT_MASK;
                long mask = allRays;
                if (r != 0) {
                    mask = allowed[word >>> SHIFT] & ~((1L << last) - 1);
                    for (int rest = runs[r]; rest != 0 && mask != 0; rest = runs[rest]) {
                        int drop = words[rest] & DIGIT_MASK;
                        int parent = where[offsets[sum - drop] + (square - drop * drop) / 2];
                        mask &= allowed[parent];
                    }
                }
                long kept = mask;
                while (mask != 0) {
                    int digit = Long.numberOfTrailingZeros(mask);
                    long bit = 1L << digit;
                    mask -= bit;
                    int grownSum = sum + digit;
                    int grownSquare = square + digit * digit;
                    int at = offsets[grownSum] + grownSquare / 2;
                    if (where[at] < 0) {
                        where[at] = size;
                        words[size] = r << SHIFT | digit;
                        keys[size] = grownSum * width + grownSquare;
                        runs[size] = digit == last ? runs[r] : r;
                        size++;
                    } else {
                        kept -= bit;
                        if (forbiddenSize == forbidden.length) {
                            forbidden = Arrays.copyOf(forbidden, forbiddenSize * 2);
                            forbiddenKeys = Arrays.copyOf(forbiddenKeys, forbiddenSize * 2);
                        }
                        forbidden[forbiddenSize] = r << SHIFT | digit;
                        forbiddenKeys[forbiddenSize++] = grownSum * width + grownSquare;
                    }
                }
                allowed[r] = kept;
            }
            begin = end;
            end = size;
        }
        Arrays.fill(allowed, 0);
        long[] rays = allowed;
        long[] pairs = new long[size];
        int[] counts = new int[base];
        // Removing every occurrence of a free digit projects an obstruction
        // onto a finite word that blocks its star. Also project adjacent pairs.
        for (int i = 0; i < forbiddenSize; i++) {
            int sum = forbiddenKeys[i] / width;
            int square = forbiddenKeys[i] % width;
            Arrays.fill(counts, 0);
            int code = forbidden[i];
            int digit = code & DIGIT_MASK;
            counts[digit] = 1;
            long support = 1L << digit;
            for (int rest = code >>> SHIFT; rest != 0; rest = words[rest] >>> SHIFT) {
                digit = words[rest] & DIGIT_MASK;
                counts[digit]++;
                support |= 1L << digit;
            }
            long touched = 0;
            while (support != 0) {
                digit = Long.numberOfTrailingZeros(support);
                support &= support - 1;
                int c = counts[digit];
                int at = where[offsets[sum - digit * c] + (square - digit * digit * c) / 2];
                rays[at] |= 1L << digit;
                touched |= 1L << digit | 1L << (digit - 1);
            }
            touched &= allPairs;
            while (touched != 0) {
                digit = Long.numberOfTrailingZeros(touched);
                long bit = 1L << digit;
                touched -= bit;
                int next = digit + 1;
                int a = counts[digit];
                int b = counts[next];
                int at = where[offsets[sum - digit * a - next * b]
                        + (square - digit * digit * a - next * next * b) / 2];
                pairs[at] |= bit;
            }
        }
        Output output = new Output(base);
        // Blocked stars propagate from immediate subwords. Free sets have at
        // most two digits, and two free digits must be adjacent.
        for (int r = 0; r < size; r++) {
            int word = words[r];
            long badRays = rays[r];
            long badPairs = pairs[r];
            long support = 0;
            if (r != 0) {
                int digit = word & DIGIT_MASK;
                support = 1L << digit;
                int parent = word >>> SHIFT;
                badRays |= rays[parent];
                badPairs |= pairs[parent];
                int sum = keys[r] / width;
                int square = keys[r] % width;
                for (int rest = runs[r]; rest != 0; rest = runs[rest]) {
                    digit = words[rest] & DIGIT_MASK;
                    support |= 1L << digit;
                    parent = where[offsets[sum - digit] + (square - digit * digit) / 2];
                    badRays |= rays[parent];
                    badPairs |= pairs[parent];
                }
            }
            rays[r] = badRays;
            pairs[r] = badPairs;
            long validRays = allRays & ~badRays;
            long validPairs = allPairs & ~badPairs;
            // A larger free set also covers positive fixed counts of its digits.
            long singles = validRays & ~support & ~(validPairs | validPairs << 1);
            long doubles = validPairs & ~(support | support >>> 1);
            if (validRays == 0) {
                output.emit(r, 0, 0, words);
            }
            while (singles != 0) {
                int digit = Long.numberOfTrailingZeros(singles);
                singles &= singles - 1;
                output.emit(r, digit, 0, words);
            }
            while (doubles != 0) {
                int digit = Long.numberOfTrailingZeros(doubles);
                doubles &= doubles - 1;
                output.emit(r, digit, digit + 1, words);
            }
        }
        return output;
    }

    public static void main(String[] args) throws IOException {
        byte[] buffer = new byte[INPUT_BUFFER];
        int base = 0;
        int length;
        while ((length = System.in.read(buffer)) != -1) {
            for (int i = 0; i < length; i++) {
                if (buffer[i] >= '0' && buffer[i] <= '9') {
                    base = base * 10 + buffer[i] - '0';
                }
            }
        }
        solve(base).write();
    }
}
