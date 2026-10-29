public class Main {
    static final int DISKS = 4, PETALS = 3, BITS = DISKS + PETALS;

    // petal j lies in every disk except disk j
    static boolean valid(int[] word) {
        int total = 0;
        for (int d = 0; d < DISKS; d++)
            total += word[d];
        for (int j = 0; j < PETALS; j++) {
            if ((total - word[j]) % 2 != word[DISKS + j])
                return false;
        }
        return true;
    }

    public static void main(String[] args) throws java.io.IOException {
        int[] word = new int[BITS];
        // every bit is a single character, read from System.in
        for (int i = 0; i < BITS; i++) {
            int ch;
            do {
                ch = System.in.read();
            } while (ch != -1 && ch <= ' ');
            word[i] = ch - '0';
        }
        // try the word as it is, then each single change
        for (int k = -1; k < BITS; k++) {
            if (k >= 0)
                word[k] ^= 1;
            if (valid(word))
                break;
            if (k >= 0)
                word[k] ^= 1;
        }
        // the answer goes out as one byte array, without a String
        byte[] output = new byte[2 * BITS];
        for (int i = 0; i < BITS; i++) {
            output[2 * i] = (byte)('0' + word[i]);
            output[2 * i + 1] = ' ';
        }
        output[output.length - 1] = '\n';
        System.out.write(output, 0, output.length);
    }
}
