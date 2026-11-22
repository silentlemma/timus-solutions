public class Main {
    static final int COUNT = 10, DECIMAL = 10;

    public static void main(String[] args) throws java.io.IOException {
        int[] values = new int[COUNT];
        int maximum = 1;
        for (int i = 0; i < COUNT; i++) {
            int c = System.in.read();
            while (c >= 0 && c <= ' ')
                c = System.in.read();
            if (c == '+')
                c = System.in.read();
            int value = 0;
            while (c >= '0' && c <= '9') {
                value = value * DECIMAL + c - '0';
                c = System.in.read();
            }
            values[i] = value;
            if (value > maximum)
                maximum = value;
        }
        int answer = 1;
        for (int divisor = 2; divisor * divisor <= maximum && answer != 0;
             divisor += divisor == 2 ? 1 : 2) {
            int exponent = 0;
            maximum = 1;
            for (int i = 0; i < COUNT; i++) {
                while (values[i] % divisor == 0) {
                    values[i] /= divisor;
                    exponent++;
                }
                if (values[i] > maximum)
                    maximum = values[i];
            }
            answer = answer * (exponent + 1) % DECIMAL;
            // This prime's exponent is final across all ten values: zero stays zero.
        }
        for (int i = 0; i < COUNT && answer != 0; i++) {
            int prime = values[i];
            if (prime == 1)
                continue;
            int exponent = 0;
            for (int j = i; j < COUNT; j++) {
                if (values[j] == prime) {
                    values[j] = 1;
                    exponent++;
                }
            }
            answer = answer * (exponent + 1) % DECIMAL;
        }
        System.out.write(new byte[] {(byte)('0' + answer), '\n'});
        System.out.flush();
    }
}
