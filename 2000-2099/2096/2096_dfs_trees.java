import java.io.IOException;

public class Main {
    private static final int MAX_QUERIES = 100000;
    private static final int MAX_CHANGES = 100000;
    private static final int BUFFER_SIZE = 65536;
    private static final int DIGIT_CAPACITY = 10;
    private static final int SPACE = ' ';
    private static final int LINE_FEED = '\n';
    private static final int DIGIT_ZERO = '0';

    private static class FastInput {
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = System.in.read(buffer);
                position = 0;
                if (length < 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int nextInt() throws IOException {
            int current = read();
            while (current <= SPACE) {
                current = read();
            }
            int value = 0;
            while (current > SPACE) {
                value = value * 10 + current - DIGIT_ZERO;
                current = read();
            }
            return value;
        }
    }

    private static class FastOutput {
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private final byte[] digits = new byte[DIGIT_CAPACITY];
        private int size;

        void write(int value) throws IOException {
            if (size == buffer.length) {
                flush();
            }
            buffer[size++] = (byte) value;
        }

        void writeInt(int value) throws IOException {
            int length = 0;
            do {
                digits[length++] = (byte) (DIGIT_ZERO + value % 10);
                value /= 10;
            } while (value != 0);
            while (length != 0) {
                write(digits[--length]);
            }
        }

        void flush() throws IOException {
            System.out.write(buffer, 0, size);
            size = 0;
        }
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int days = input.nextInt();
        int friends = input.nextInt();
        int[] activity = new int[days];
        for (int day = 0; day < days; ++day) {
            activity[day] = input.nextInt();
        }

        int[] childHead = new int[friends + 1];
        int[] childNext = new int[friends + 1];
        int[] queryHead = new int[friends + 1];
        int[] queryNext = new int[MAX_QUERIES];
        int[] queryDay = new int[MAX_QUERIES];
        int[] queryEnd = new int[friends + 1];
        int[] changeStart = new int[friends + 2];
        int[] firstDay = new int[MAX_CHANGES];
        int[] dayCount = new int[MAX_CHANGES];
        int[] period = new int[MAX_CHANGES];
        int[] newActivity = new int[MAX_CHANGES];
        int queries = 0;
        int changes = 0;
        int totalAssignments = 0;

        for (int friend = 1; friend <= friends; ++friend) {
            int count = input.nextInt();
            for (int query = 0; query < count; ++query) {
                int version = input.nextInt();
                queryDay[queries] = input.nextInt() - 1;
                queryNext[queries] = queryHead[version];
                queryHead[version] = ++queries;
            }
            queryEnd[friend] = queries;
            int parent = input.nextInt();
            childNext[friend] = childHead[parent];
            childHead[parent] = friend;
            count = input.nextInt();
            for (int change = 0; change < count; ++change) {
                firstDay[changes] = input.nextInt() - 1;
                dayCount[changes] = input.nextInt();
                period[changes] = input.nextInt();
                newActivity[changes] = input.nextInt();
                totalAssignments += dayCount[changes++];
            }
            changeStart[friend + 1] = changes;
        }

        int[] answer = new int[queries];
        int[] history = new int[totalAssignments];
        int historySize = 0;
        int[] events = new int[2 * friends + 1];
        int eventCount = 1;
        while (eventCount != 0) {
            int event = events[--eventCount];
            if (event >= 0) {
                int version = event;
                for (int change = changeStart[version]; change < changeStart[version + 1];
                        ++change) {
                    int day = firstDay[change];
                    for (int left = dayCount[change]; left != 0; --left) {
                        history[historySize++] = activity[day];
                        activity[day] = newActivity[change];
                        day += period[change];
                    }
                }
                for (int query = queryHead[version]; query != 0; query = queryNext[query - 1]) {
                    answer[query - 1] = activity[queryDay[query - 1]];
                }
                if (version != 0) {
                    events[eventCount++] = -version;
                }
                for (int child = childHead[version]; child != 0; child = childNext[child]) {
                    events[eventCount++] = child;
                }
            } else {
                int version = -event;
                // Undo assignments in reverse order, including overlaps within one plan.
                for (int change = changeStart[version + 1]; change > changeStart[version];) {
                    --change;
                    int day = firstDay[change] + (dayCount[change] - 1) * period[change];
                    for (int left = dayCount[change]; left != 0; --left) {
                        activity[day] = history[--historySize];
                        day -= period[change];
                    }
                }
            }
        }

        FastOutput output = new FastOutput();
        for (int friend = 1; friend <= friends; ++friend) {
            for (int query = queryEnd[friend - 1]; query < queryEnd[friend]; ++query) {
                if (query != queryEnd[friend - 1]) {
                    output.write(SPACE);
                }
                output.writeInt(answer[query]);
            }
            output.write(LINE_FEED);
        }
        output.flush();
    }
}
