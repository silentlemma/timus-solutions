public class Main {
    static int read() throws java.io.IOException { return System.in.read(); }
    static int number() throws java.io.IOException {
        int character = read();
        while (character >= 0 && character <= ' ')
            character = read();
        boolean negative = character == '-';
        if (negative || character == '+')
            character = read();
        int result = 0;
        while (character >= '0' && character <= '9') {
            result = result * 10 + character - '0';
            character = read();
        }
        return negative ? -result : result;
    }

    public static void main(String[] args) throws java.io.IOException {
        int count = number(), parity = 0;
        for (int i = 0; i < count; i++)
            parity ^= ((number() - 1) / 2) & 1;
        byte[] answer = parity == 0 ? new byte[] {'S', 't', 'a', 'n', 'n', 'i', 's', '\n'}
                                    : new byte[] {'D', 'a', 'e', 'n', 'e', 'r', 'y', 's', '\n'};
        System.out.write(answer);
        System.out.flush();
    }
}
