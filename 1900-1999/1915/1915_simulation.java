import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.IOException;

public class Main {
    private static final int DECIMAL_DIGITS = 10;

    static int[] poppedCoins(int[] operations) {
        int remaining = 0;
        for (int operation : operations) {
            if (operation == -1) {
                remaining++;
            }
        }
        int[] answer = new int[remaining];
        if (remaining == 0) {
            return answer;
        }
        int capacity = remaining;
        int[] coins = new int[capacity];
        int bottom = 0;
        int size = 0;
        int output = 0;
        for (int operation : operations) {
            if (remaining == 0) {
                break;
            }
            if (operation > 0) {
                if (size == remaining) {
                    bottom = (bottom + 1) % capacity;
                    size--;
                }
                coins[(bottom + size) % capacity] = operation;
                size++;
            } else if (operation == -1) {
                remaining--;
                size--;
                answer[output++] = coins[(bottom + size) % capacity];
            } else {
                int extra = Math.min(size, remaining - size);
                int newBottom = (bottom + capacity - extra) % capacity;
                int source = (bottom + size - extra) % capacity;
                int destination = newBottom;
                for (int index = 0; index < extra; index++) {
                    coins[destination] = coins[source];
                    if (++source == capacity) {
                        source = 0;
                    }
                    if (++destination == capacity) {
                        destination = 0;
                    }
                }
                bottom = newBottom;
                size += extra;
            }
        }
        return answer;
    }

    private static final class Input {
        final BufferedInputStream stream = new BufferedInputStream(System.in);

        int next() throws IOException {
            int current;
            do {
                current = stream.read();
            } while (current <= ' ');
            int sign = 1;
            if (current == '-') {
                sign = -1;
                current = stream.read();
            }
            int value = 0;
            while (current > ' ') {
                value = value * 10 + current - '0';
                current = stream.read();
            }
            return value * sign;
        }
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        int count = input.next();
        int[] operations = new int[count];
        for (int index = 0; index < count; index++) {
            operations[index] = input.next();
        }
        BufferedOutputStream output = new BufferedOutputStream(System.out);
        byte[] digits = new byte[DECIMAL_DIGITS];
        for (int coin : poppedCoins(operations)) {
            int start = digits.length;
            do {
                digits[--start] = (byte) ('0' + coin % 10);
                coin /= 10;
            } while (coin != 0);
            output.write(digits, start, digits.length - start);
            output.write('\n');
        }
        output.flush();
    }
}
