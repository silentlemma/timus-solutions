import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    private static final int DIVISOR = 7;
    private static final int KEY_SHIFT = 10000;
    private static final int MAX_DIGITS = 20;
    private static final String[] SUFFIXES = {"3241", "1324", "1234", "2341",
                                              "1243", "1342", "2134"};

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));
        int count = Integer.parseInt(input.readLine().trim());
        char[] answer = new char[MAX_DIGITS];
        for (int i = 0; i < count; ++i) {
            String number = input.readLine().trim();
            int size = 0, zeros = 0, remainder = 0, removed = 0;
            for (int j = 0; j < number.length(); ++j) {
                char digit = number.charAt(j);
                if (digit == '0') {
                    ++zeros;
                } else if (digit >= '1' && digit <= '4' && (removed & (1 << (digit - '1'))) == 0) {
                    removed |= 1 << (digit - '1');
                } else {
                    answer[size++] = digit;
                    remainder = (10 * remainder + digit - '0') % DIVISOR;
                }
            }
            // Choose the four digits that cancel the shifted head remainder.
            int needed = (DIVISOR - remainder * KEY_SHIFT % DIVISOR) % DIVISOR;
            output.write(answer, 0, size);
            output.write(SUFFIXES[needed]);
            for (int j = 0; j < zeros; ++j) {
                output.write('0');
            }
            output.newLine();
        }
        output.flush();
    }
}
