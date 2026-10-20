import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int MAX_GEOMETRIC = 30;
    private static final int SEED_LIMIT = MAX_GEOMETRIC + 2;
    private static final int MAJORITY_SIZE = 2 * (2 * MAX_GEOMETRIC + 1);

    private static class Answer {
        final long[] arithmetic;
        final long[] geometric;

        Answer(long[] arithmetic, long[] geometric) {
            this.arithmetic = arithmetic;
            this.geometric = geometric;
        }
    }

    private static boolean isArithmetic(long[] values) {
        for (int i = 2; i < values.length; i++) {
            if (values[i] - values[i - 1] != values[1] - values[0]) {
                return false;
            }
        }
        return true;
    }

    private static boolean isGeometric(long[] values, int size) {
        if (size == 0) {
            return false;
        }
        if (values[0] == 0) {
            return values[size - 1] == 0;
        }
        for (int i = 2; i < size; i++) {
            if (values[i] * values[0] != values[i - 1] * values[1]) {
                return false;
            }
        }
        return true;
    }

    private static void insert(long[] values, int size, long value) {
        int index = size;
        while (index > 0 && values[index - 1] > value) {
            values[index] = values[index - 1];
            index--;
        }
        values[index] = value;
    }

    private static Answer extract(long[] values, long start, long step) {
        long[] arithmetic = new long[values.length];
        long[] geometric = new long[MAX_GEOMETRIC + 2];
        int arithmeticSize = 0;
        int geometricSize = 0;
        long expected = start;
        for (long value : values) {
            if (value == expected) {
                arithmetic[arithmeticSize++] = value;
                expected += step;
            } else {
                geometric[geometricSize++] = value;
                if (geometricSize > MAX_GEOMETRIC) {
                    return null;
                }
            }
        }
        // Three distinct geometric terms cannot form an arithmetic progression.
        for (int removed = 0; removed <= 2; removed++) {
            if (arithmeticSize > 0 && isGeometric(geometric, geometricSize)) {
                return new Answer(Arrays.copyOf(arithmetic, arithmeticSize),
                        Arrays.copyOf(geometric, geometricSize));
            }
            if (removed == 2 || arithmeticSize <= 1) {
                break;
            }
            insert(geometric, geometricSize++, arithmetic[--arithmeticSize]);
        }
        return null;
    }

    private static Answer solve(long[] values) {
        Arrays.sort(values);
        int distinct = 0;
        int repeated = 0;
        long constant = 0;
        for (int i = 0; i < values.length; i++) {
            if (i == 0 || values[i] != values[i - 1]) {
                distinct++;
            } else if (i == 1 || values[i] != values[i - 2]) {
                repeated++;
                constant = values[i];
            }
        }
        if (distinct == 1) {
            return new Answer(Arrays.copyOf(values, 1),
                    Arrays.copyOfRange(values, 1, values.length));
        }
        if (distinct == 2) {
            int cut = 1;
            while (values[cut] == values[0]) {
                cut++;
            }
            return new Answer(Arrays.copyOf(values, cut),
                    Arrays.copyOfRange(values, cut, values.length));
        }
        if (repeated == 1) {
            int copies = 0;
            for (long value : values) {
                if (value == constant) {
                    copies++;
                }
            }
            long[] other = new long[values.length - copies];
            int index = 0;
            for (long value : values) {
                if (value != constant) {
                    other[index++] = value;
                }
            }
            for (int moved = 0; moved < 2; moved++) {
                long[] rest = Arrays.copyOf(other, other.length + moved);
                if (moved == 1) {
                    insert(rest, other.length, constant);
                }
                long[] equal = new long[copies - moved];
                Arrays.fill(equal, constant);
                if (isGeometric(rest, rest.length)) {
                    return new Answer(equal, rest);
                }
                if (isArithmetic(rest)) {
                    return new Answer(rest, equal);
                }
            }
        }
        if (values.length <= MAX_GEOMETRIC + 1) {
            for (int i = 0; i < values.length; i++) {
                long[] rest = new long[values.length - 1];
                System.arraycopy(values, 0, rest, 0, i);
                System.arraycopy(values, i + 1, rest, i, values.length - i - 1);
                if (isGeometric(rest, rest.length)) {
                    return new Answer(new long[] {values[i]}, rest);
                }
            }
        }
        if (values.length >= MAJORITY_SIZE) {
            long[] gaps = new long[values.length - 1];
            for (int i = 1; i < values.length; i++) {
                gaps[i - 1] = values[i] - values[i - 1];
            }
            Arrays.sort(gaps);
            long step = gaps[gaps.length / 2];
            if (step != 0) {
                for (int i = 0; i <= MAX_GEOMETRIC; i++) {
                    Answer answer = extract(values, values[i], step);
                    if (answer != null) {
                        return answer;
                    }
                }
            }
        } else {
            int limit = Math.min(values.length, SEED_LIMIT);
            for (int i = 0; i < limit; i++) {
                for (int j = i + 1; j < limit; j++) {
                    long step = values[j] - values[i];
                    if (step != 0) {
                        Answer answer = extract(values, values[i], step);
                        if (answer != null) {
                            return answer;
                        }
                    }
                }
            }
        }
        return null;
    }

    private static long nextLong(BufferedInputStream input) throws IOException {
        int character = input.read();
        while (character <= ' ' && character != -1) {
            character = input.read();
        }
        long value = 0;
        while (character > ' ') {
            value = value * 10 + character - '0';
            character = input.read();
        }
        return value;
    }

    private static void appendValues(StringBuilder output, long[] values) {
        for (int i = 0; i < values.length; i++) {
            if (i > 0) {
                output.append(' ');
            }
            output.append(values[i]);
        }
        output.append('\n');
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int size = (int) nextLong(input);
        long[] values = new long[size];
        for (int i = 0; i < size; i++) {
            values[i] = nextLong(input);
        }
        Answer answer = solve(values);
        if (answer == null) {
            System.out.println(-1);
            return;
        }
        StringBuilder output = new StringBuilder();
        output.append(answer.arithmetic.length).append('\n');
        appendValues(output, answer.arithmetic);
        appendValues(output, answer.geometric);
        System.out.print(output);
    }
}
