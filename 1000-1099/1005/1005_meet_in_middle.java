public class Main {
    private static final int INPUT_BUFFER_SIZE = 4096;
    private static final byte[] input = new byte[INPUT_BUFFER_SIZE];
    private static int position;
    private static int length;

    // the numbers are parsed by hand from a small buffer, faster than Scanner
    private static int readByte() throws java.io.IOException {
        if (position == length) {
            length = System.in.read(input);
            position = 0;
            if (length < 0) {
                return -1;
            }
        }
        return input[position++];
    }

    private static long nextLong() throws java.io.IOException {
        int c;
        do {
            c = readByte();
        } while (c >= 0 && c <= ' ');
        int sign = 1;
        if (c == '-') {
            sign = -1;
            c = readByte();
        }
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = readByte();
        }
        return value * sign;
    }

    // the sums of all subsets of weights[from..to), sorted
    private static int[] subsetSums(int[] weights, int from, int to) {
        int[] sums = new int[1 << (to - from)];
        int count = 1;
        for (int index = from; index < to; index++) {
            for (int i = 0; i < count; i++) {
                sums[count + i] = sums[i] + weights[index];
            }
            count *= 2;
        }
        java.util.Arrays.sort(sums);
        return sums;
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = (int)nextLong();
        int[] weights = new int[n];
        int total = 0;
        for (int i = 0; i < n; i++) {
            weights[i] = (int)nextLong();
            total += weights[i];
        }
        int[] left = subsetSums(weights, 0, n / 2);
        int[] right = subsetSums(weights, n / 2, n);
        // a pile is a subset of each half; walk the left sums up and the right
        // sums down, moving the side that brings the pile closer to total / 2
        int best = total;
        int i = 0, j = right.length - 1;
        while (i < left.length && j >= 0) {
            int difference = total - 2 * (left[i] + right[j]);
            best = Math.min(best, Math.abs(difference));
            // the difference has the parity of the total, so it cannot be smaller
            if (best == total % 2) {
                break;
            }
            if (difference > 0) {
                i++;
            } else {
                j--;
            }
        }
        System.out.println(best);
    }
}
