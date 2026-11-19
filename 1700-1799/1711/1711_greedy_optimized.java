public class Main {
    private static final int CHOICES = 3;
    private static final int NAME_WIDTH = 20;
    private static byte[] names, nameLengths;

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

    static void word(int index) throws java.io.IOException {
        int character = read(), size = 0;
        while (character >= 0 && character <= ' ')
            character = read();
        while (character > ' ') {
            names[index * NAME_WIDTH + size++] = (byte)character;
            character = read();
        }
        nameLengths[index] = (byte)size;
    }

    static int compare(int left, int right) {
        int size = nameLengths[left] < nameLengths[right] ? nameLengths[left] : nameLengths[right];
        for (int i = 0; i < size; i++) {
            int difference = names[left * NAME_WIDTH + i] - names[right * NAME_WIDTH + i];
            if (difference != 0)
                return difference;
        }
        return nameLengths[left] - nameLengths[right];
    }

    public static void main(String[] args) throws java.io.IOException {
        int count = number();
        names = new byte[CHOICES * count * NAME_WIDTH];
        nameLengths = new byte[CHOICES * count];
        for (int i = 0; i < nameLengths.length; i++)
            word(i);
        byte[] answer = new byte[count * (NAME_WIDTH + 1)];
        int last = -1, used = 0;
        java.io.PrintStream output = System.out;
        for (int i = 0; i < count; i++) {
            int start = CHOICES * (number() - 1), best = -1;
            for (int candidate = start; candidate < start + CHOICES; candidate++) {
                if ((last < 0 || compare(candidate, last) > 0) &&
                    (best < 0 || compare(candidate, best) < 0))
                    best = candidate;
            }
            if (best < 0) {
                output.write(new byte[] {'I', 'M', 'P', 'O', 'S', 'S', 'I', 'B', 'L', 'E', '\n'});
                output.flush();
                return;
            }
            System.arraycopy(names, best * NAME_WIDTH, answer, used, nameLengths[best]);
            used += nameLengths[best];
            answer[used++] = '\n';
            last = best;
        }
        output.write(answer, 0, used);
        output.flush();
    }
}
