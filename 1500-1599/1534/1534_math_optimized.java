import java.io.IOException;

public class Main {
    private static final int DECIMAL = 10;
    private static final int INPUT_SIZE = 64;

    private static class Input {
        private final byte[] data = new byte[INPUT_SIZE];
        private int position;
        private int length;

        Input() throws IOException {
            while (length < data.length) {
                int count = System.in.read(data, length, data.length - length);
                if (count < 0) {
                    break;
                }
                length += count;
            }
        }

        long next() {
            long number = 0;
            while (position < length && (data[position] < '0' || data[position] > '9')) {
                position++;
            }
            while (position < length && data[position] >= '0' && data[position] <= '9') {
                number = number * DECIMAL + data[position++] - '0';
            }
            return number;
        }
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        long scored = input.next();
        long conceded = input.next();
        long matches = input.next();
        long margin = scored - conceded;
        long best;
        long worst;
        if (margin >= 0) {
            best = matches + 2 * Math.min(margin, matches);
            worst = margin == 0 ? matches : matches + 2;
        } else {
            best = matches - 1;
            worst = matches - Math.min(-margin, matches);
        }
        if (scored > 0 && conceded > 0 && matches > 1) {
            best = Math.max(best, matches - 1 + 2 * Math.min(scored, matches - 1));
            worst = Math.min(worst, matches + 2 - Math.min(conceded, matches - 1));
        }
        System.out.print(best + " " + worst + "\n");
    }
}
