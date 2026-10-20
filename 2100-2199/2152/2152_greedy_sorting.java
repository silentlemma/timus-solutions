import java.io.IOException;
import java.io.InputStream;

public class Main {
    private static final int MAX_DIGIT = 9;
    private static final int CENTS_PER_UNIT = 100;
    private static final long TOTAL_BASE = 1000000000L;
    private static final int TOTAL_DIGITS = 9;
    private static final int BUFFER_SIZE = 65536;
    private static final int OUTPUT_PER_ITEM = 24;

    private static final class FastInput {
        private final InputStream stream = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = stream.read(buffer);
                position = 0;
                if (length < 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        long next() throws IOException {
            int current;
            do {
                current = read();
            } while (current <= ' ');
            long value = 0;
            while (current > ' ') {
                value = value * 10 + current - '0';
                current = read();
            }
            return value;
        }
    }

    private static long excess(long value, long limit) {
        return value > limit ? value - limit : 0;
    }

    private static long largestChange(long value) {
        long place = 1;
        while (value / place >= 10) {
            place *= 10;
        }
        while (place > 0) {
            long digit = value / place % 10;
            if (digit < MAX_DIGIT) {
                return value + (MAX_DIGIT - digit) * place;
            }
            place /= 10;
        }
        return value;
    }

    private static int[] sortedOrder(long[] whole, int[] cents) {
        int size = whole.length;
        int[] order = new int[size];
        int[] temporary = new int[size];
        for (int i = 0; i < size; i++) {
            order[i] = i;
        }
        for (int width = 1; width < size; width *= 2) {
            for (int start = 0; start < size; start += width * 2) {
                int middle = Math.min(start + width, size);
                int end = Math.min(start + width * 2, size);
                int left = start;
                int right = middle;
                for (int destination = start; destination < end; destination++) {
                    boolean takeLeft = right == end;
                    if (left < middle && right < end) {
                        int a = order[left];
                        int b = order[right];
                        takeLeft = whole[a] > whole[b]
                                || whole[a] == whole[b] && cents[a] >= cents[b];
                    }
                    if (left < middle && takeLeft) {
                        temporary[destination] = order[left++];
                    } else {
                        temporary[destination] = order[right++];
                    }
                }
            }
            int[] swap = order;
            order = temporary;
            temporary = swap;
        }
        return order;
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int n = (int) input.next();
        int k = (int) input.next();
        long maxWeight = input.next();
        long maxPrice = input.next();
        long weightRate = input.next();
        long priceRate = input.next();
        long[] weights = new long[n];
        long[] prices = new long[n];
        long[] replacements = new long[n];
        long[] whole = new long[n];
        int[] cents = new int[n];
        boolean[] changeWeight = new boolean[n];
        for (int i = 0; i < n; i++) {
            long weight = input.next();
            long price = input.next();
            weights[i] = weight;
            prices[i] = price;
            long newWeight = largestChange(weight);
            long newPrice = largestChange(price);
            long weightGain = (excess(newWeight, maxWeight) - excess(weight, maxWeight))
                    * weightRate;
            long priceGain = (excess(newPrice, maxPrice) - excess(price, maxPrice)) * priceRate;
            whole[i] = priceGain / CENTS_PER_UNIT;
            cents[i] = (int) (priceGain % CENTS_PER_UNIT);
            if (weightGain > whole[i] || weightGain == whole[i] && cents[i] == 0) {
                replacements[i] = newWeight;
                whole[i] = weightGain;
                cents[i] = 0;
                changeWeight[i] = true;
            } else {
                replacements[i] = newPrice;
            }
        }
        if (k > 0) {
            int[] order = sortedOrder(whole, cents);
            for (int selected = 0; selected < k; selected++) {
                int i = order[selected];
                if (whole[i] == 0 && cents[i] == 0) {
                    break;
                }
                if (changeWeight[i]) {
                    weights[i] = replacements[i];
                } else {
                    prices[i] = replacements[i];
                }
            }
        }
        // Split the total because the sum of weight charges can exceed long.
        long totalHigh = 0;
        long totalLow = 0;
        long priceCents = 0;
        for (int i = 0; i < n; i++) {
            long fee = excess(weights[i], maxWeight) * weightRate;
            totalHigh += fee / TOTAL_BASE;
            totalLow += fee % TOTAL_BASE;
            priceCents += excess(prices[i], maxPrice) * priceRate;
        }
        totalLow += priceCents / CENTS_PER_UNIT;
        totalHigh += totalLow / TOTAL_BASE;
        totalLow %= TOTAL_BASE;
        StringBuilder output = new StringBuilder(n * OUTPUT_PER_ITEM);
        if (totalHigh > 0) {
            output.append(totalHigh);
            String lowText = Long.toString(totalLow);
            for (int i = lowText.length(); i < TOTAL_DIGITS; i++) {
                output.append('0');
            }
            output.append(lowText);
        } else {
            output.append(totalLow);
        }
        output.append('.');
        long fraction = priceCents % CENTS_PER_UNIT;
        if (fraction < 10) {
            output.append('0');
        }
        output.append(fraction).append('\n');
        for (int i = 0; i < n; i++) {
            output.append(weights[i]).append(' ').append(prices[i]).append('\n');
        }
        System.out.print(output);
    }
}
