public class Main {
    private static final int SPLIT = 3;

    public static void main(String[] args) throws java.io.IOException {
        // the digits are summed as they are read, the number is never stored
        int ch;
        do {
            ch = System.in.read();
        } while (ch != -1 && ch <= ' ');
        int digitSum = 0;
        while (ch >= '0' && ch <= '9') {
            digitSum += ch - '0';
            ch = System.in.read();
        }
        // no power of two is divisible by 3, so from a multiple of 3 every
        // move leaves a non-multiple, and from a non-multiple taking 1 or 2
        // stones leaves a multiple; the remainder is also the smallest move
        int remainder = digitSum % SPLIT;
        if (remainder == 0) {
            System.out.write('2');
            System.out.write('\n');
        } else {
            byte[] answer = {'1', '\n', (byte)('0' + remainder), '\n'};
            System.out.write(answer, 0, answer.length);
        }
    }
}
