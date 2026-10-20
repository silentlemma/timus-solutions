import java.io.IOException;
import java.io.InputStream;

public class Main {
    private static final int BUFFER_SIZE = 1 << 16;

    private static final class FastInput {
        private final InputStream input = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = input.read(buffer);
                position = 0;
                if (length < 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int nextInt() throws IOException {
            int character;
            do {
                character = read();
            } while (character <= ' ' && character != -1);
            int value = 0;
            while (character >= '0' && character <= '9') {
                value = value * 10 + character - '0';
                character = read();
            }
            return value;
        }
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int floors = input.nextInt();
        int elevators = input.nextInt();
        int[] difference = new int[floors + 1];
        for (int i = 0; i < elevators; ++i) {
            int left = input.nextInt();
            int right = input.nextInt();
            ++difference[left];
            --difference[right];
        }
        if (floors == 1) {
            System.out.println(-1);
            return;
        }

        int crossing = 0;
        int answer = elevators;
        // Every route crosses each gap; cover all elevators crossing the cheapest gap.
        for (int floor = 1; floor < floors; ++floor) {
            crossing += difference[floor];
            answer = Math.min(answer, crossing);
        }
        System.out.println(answer);
    }
}
