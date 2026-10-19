import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    static final int DIGIT_COUNT = 4;
    static final int HEX_BASE = 16;
    static final int DIGIT_BITS = 4;
    static final int DIGIT_MASK = HEX_BASE - 1;
    static final int PAIR_DOMAIN = HEX_BASE * HEX_BASE;
    static final int TRIPLE_DOMAIN = PAIR_DOMAIN * HEX_BASE;
    static final int PAIR_GROUPS = DIGIT_COUNT * (DIGIT_COUNT - 1) / 2;

    static class FastInput {
        final BufferedInputStream stream = new BufferedInputStream(System.in);

        int nextInt(int radix) throws IOException {
            int character;
            do {
                character = stream.read();
            } while (character <= ' ');
            int value = 0;
            while (character > ' ') {
                int digit = character >= 'a' ? character - 'a' + 10 : character - '0';
                value = value * radix + digit;
                character = stream.read();
            }
            return value;
        }
    }

    static long[] distanceHistogram(int[] numbers) {
        int[][] singles = new int[DIGIT_COUNT][HEX_BASE];
        int[][] pairs = new int[PAIR_GROUPS][PAIR_DOMAIN];
        int[][] triples = new int[DIGIT_COUNT][TRIPLE_DOMAIN];
        long singlePairs = 0;
        long doublePairs = 0;
        long triplePairs = 0;
        for (int number : numbers) {
            int first = number >> (DIGIT_BITS * (DIGIT_COUNT - 1));
            int second = (number >> (2 * DIGIT_BITS)) & DIGIT_MASK;
            int third = (number >> DIGIT_BITS) & DIGIT_MASK;
            int fourth = number & DIGIT_MASK;
            int[] singleKeys = {first, second, third, fourth};
            for (int index = 0; index < DIGIT_COUNT; index++) {
                singlePairs += singles[index][singleKeys[index]]++;
            }
            int[] pairKeys = {number >> (2 * DIGIT_BITS), first * HEX_BASE + third,
                    first * HEX_BASE + fourth, (number >> DIGIT_BITS) & (PAIR_DOMAIN - 1),
                    second * HEX_BASE + fourth, number & (PAIR_DOMAIN - 1)};
            for (int index = 0; index < PAIR_GROUPS; index++) {
                doublePairs += pairs[index][pairKeys[index]]++;
            }
            int[] tripleKeys = {number >> DIGIT_BITS,
                    (number >> (2 * DIGIT_BITS)) * HEX_BASE + fourth,
                    first * PAIR_DOMAIN + (number & (PAIR_DOMAIN - 1)),
                    number & (TRIPLE_DOMAIN - 1)};
            for (int index = 0; index < DIGIT_COUNT; index++) {
                triplePairs += triples[index][tripleKeys[index]]++;
            }
        }
        long count = numbers.length;
        long distanceOne = triplePairs;
        long distanceTwo = doublePairs - (DIGIT_COUNT - 1) * distanceOne;
        long distanceThree = singlePairs - 2 * distanceTwo - (DIGIT_COUNT - 1) * distanceOne;
        long distanceFour = count * (count - 1) / 2 - distanceOne - distanceTwo - distanceThree;
        return new long[] {distanceOne, distanceTwo, distanceThree, distanceFour};
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int count = input.nextInt(10);
        int[] numbers = new int[count];
        for (int index = 0; index < count; index++) {
            numbers[index] = input.nextInt(HEX_BASE);
        }
        long[] answer = distanceHistogram(numbers);
        StringBuilder output = new StringBuilder();
        for (int index = 0; index < DIGIT_COUNT; index++) {
            if (index > 0) {
                output.append(' ');
            }
            output.append(answer[index]);
        }
        System.out.println(output);
    }
}
