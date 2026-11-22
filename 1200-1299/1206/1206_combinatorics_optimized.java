public class Main {
    static final int FIRST = 36, OTHER = 55, DECIMAL = 10;

    static int nextInt() throws java.io.IOException {
        int c = System.in.read();
        while (c >= 0 && c <= ' ')
            c = System.in.read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * DECIMAL + c - '0';
            c = System.in.read();
        }
        return value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int k = nextInt();
        // The same 36*55^(k-1) has fewer than 2*k decimal digits, with k <= 50.
        int[] digits = new int[2 * k];
        digits[0] = FIRST % DECIMAL;
        digits[1] = FIRST / DECIMAL;
        int length = 2;
        for (int power = 1; power < k; power++) {
            int carry = 0;
            for (int i = 0; i < length; i++) {
                int value = digits[i] * OTHER + carry;
                digits[i] = value % DECIMAL;
                carry = value / DECIMAL;
            }
            while (carry > 0) {
                digits[length++] = carry % DECIMAL;
                carry /= DECIMAL;
            }
        }
        byte[] answer = new byte[length + 1];
        for (int i = 0; i < length; i++)
            answer[i] = (byte)('0' + digits[length - 1 - i]);
        answer[length] = '\n';
        System.out.write(answer);
    }
}
