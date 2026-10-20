import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int BUFFER_SIZE = 65536;

    private static final class FastInput {
        private final byte[] data;
        private int position;

        FastInput() throws IOException {
            ByteArrayOutputStream bytes = new ByteArrayOutputStream();
            byte[] buffer = new byte[BUFFER_SIZE];
            int length;
            while ((length = System.in.read(buffer)) != -1) {
                bytes.write(buffer, 0, length);
            }
            data = bytes.toByteArray();
        }

        private void skipSpace() {
            while (position < data.length && data[position] <= ' ') {
                position++;
            }
        }

        int integer() {
            skipSpace();
            int value = 0;
            while (position < data.length && data[position] > ' ') {
                value = value * 10 + data[position++] - '0';
            }
            return value;
        }

        byte[] word() {
            skipSpace();
            int start = position;
            while (position < data.length && data[position] > ' ') {
                position++;
            }
            byte[] result = new byte[position - start];
            for (int i = 0; i < result.length; i++) {
                result[i] = data[position - i - 1];
            }
            return result;
        }
    }

    private static final class Query implements Comparable<Query> {
        final int u;
        final int v;
        final int cut;
        final int index;

        Query(int first, int second, int removed, int order) {
            u = Math.min(first, second);
            v = Math.max(first, second);
            cut = removed;
            index = order;
        }

        @Override
        public int compareTo(Query other) {
            int first = Integer.compare(u, other.u);
            return first != 0 ? first : Integer.compare(v, other.v);
        }
    }

    private static String fraction(long numerator, long denominator) {
        StringBuilder result = new StringBuilder();
        result.append(numerator / denominator);
        long remainder = numerator % denominator;
        if (remainder != 0) {
            result.append('.');
            while (remainder != 0) {
                remainder *= 10;
                result.append((char) ('0' + remainder / denominator));
                remainder %= denominator;
            }
        }
        return result.toString();
    }

    private static String solve(int[] next, int length, int cut) {
        long bestNumerator = 0;
        long bestDenominator = 1;
        long denominator = 1;
        int position = cut;
        long remaining = length - cut;
        while (true) {
            position = next[position];
            long numerator = position - cut;
            if (numerator * bestDenominator > bestNumerator * denominator) {
                bestNumerator = numerator;
                bestDenominator = denominator;
            }
            if (position == length) {
                break;
            }
            position++;
            denominator *= 2;
            // An answer is at least 1/2, so at most 18 mismatches need consideration.
            // Even the whole remaining word cannot improve the current answer.
            if (remaining * bestDenominator <= bestNumerator * denominator) {
                break;
            }
        }
        return fraction(bestNumerator, bestDenominator);
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int count = input.integer();
        int queryCount = input.integer();
        byte[][] words = new byte[count][];
        int maximumLength = 0;
        for (int i = 0; i < count; i++) {
            words[i] = input.word();
            maximumLength = Math.max(maximumLength, words[i].length);
        }
        Query[] queries = new Query[queryCount];
        for (int i = 0; i < queryCount; i++) {
            queries[i] = new Query(input.integer() - 1, input.integer() - 1, input.integer(), i);
        }
        Arrays.sort(queries);
        String[] answers = new String[queryCount];
        int[] next = new int[maximumLength + 1];
        int begin = 0;
        while (begin < queryCount) {
            int end = begin + 1;
            int u = queries[begin].u;
            int v = queries[begin].v;
            while (end < queryCount && queries[end].u == u && queries[end].v == v) {
                end++;
            }
            int length = Math.min(words[u].length, words[v].length);
            if (u != v) {
                // Reuse one mismatch table for every query of this word pair.
                next[length] = length;
                for (int i = length - 1; i >= 0; i--) {
                    next[i] = words[u][i] == words[v][i] ? next[i + 1] : i;
                }
            }
            for (int i = begin; i < end; i++) {
                Query current = queries[i];
                answers[current.index] = u == v
                        ? Integer.toString(length - current.cut)
                        : solve(next, length, current.cut);
            }
            begin = end;
        }
        StringBuilder output = new StringBuilder();
        for (String answer : answers) {
            output.append(answer).append('\n');
        }
        System.out.print(output);
    }
}
