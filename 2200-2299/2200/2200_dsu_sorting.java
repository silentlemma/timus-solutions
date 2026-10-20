import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    private static final int MINIMUM_SIDE = 3;
    private static final int INPUT_BUFFER_SIZE = 65536;

    private static class FastReader {
        private final InputStream input = System.in;
        private final byte[] buffer = new byte[INPUT_BUFFER_SIZE];
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
            int current = read();
            while (current <= ' ') {
                current = read();
            }
            int sign = 1;
            if (current == '-') {
                sign = -1;
                current = read();
            }
            int value = 0;
            while (current > ' ') {
                value = value * 10 + current - '0';
                current = read();
            }
            return sign * value;
        }
    }

    private static class Board {
        final int xLow;
        final int yLow;
        final int xHigh;
        final int yHigh;

        Board(int xLow, int yLow, int xHigh, int yHigh) {
            this.xLow = xLow;
            this.yLow = yLow;
            this.xHigh = xHigh;
            this.yHigh = yHigh;
        }
    }

    private static class Event {
        int coordinate;
        int low;
        int high;
        int board;
        int kind;

        Event(int coordinate, int low, int high, int board, int kind) {
            this.coordinate = coordinate;
            this.low = low;
            this.high = high;
            this.board = board;
            this.kind = kind;
        }
    }

    private static class DisjointSet {
        final int[] parent;
        final int[] size;

        DisjointSet(int count) {
            parent = new int[count];
            size = new int[count];
            for (int i = 0; i < count; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        int find(int vertex) {
            while (parent[vertex] != vertex) {
                parent[vertex] = parent[parent[vertex]];
                vertex = parent[vertex];
            }
            return vertex;
        }

        void unite(int first, int second) {
            first = find(first);
            second = find(second);
            if (first == second) {
                return;
            }
            if (size[first] < size[second]) {
                int temporary = first;
                first = second;
                second = temporary;
            }
            parent[second] = first;
            size[first] += size[second];
        }
    }

    private static void connect(Event[] events, DisjointSet dsu) {
        Arrays.sort(events, new Comparator<Event>() {
            @Override
            public int compare(Event first, Event second) {
                int order = Integer.compare(first.coordinate, second.coordinate);
                return order != 0 ? order : Integer.compare(first.low, second.low);
            }
        });
        int[] last = {-1, -1};
        for (int i = 0; i < events.length; i++) {
            Event current = events[i];
            if (i == 0 || current.coordinate != events[i - 1].coordinate) {
                last[0] = -1;
                last[1] = -1;
            }
            int opposite = last[1 - current.kind];
            // Same-side intervals are disjoint, so only the latest one can overlap.
            if (opposite != -1 && events[opposite].high >= current.low) {
                dsu.unite(current.board, events[opposite].board);
            }
            last[current.kind] = i;
        }
    }

    public static void main(String[] args) throws IOException {
        FastReader input = new FastReader();
        int count = input.nextInt();
        input.nextInt();
        int startX = input.nextInt();
        int startY = input.nextInt();
        Board[] boards = new Board[count];
        int start = 0;
        boolean trapped = false;
        for (int i = 0; i < count; i++) {
            Board current = new Board(input.nextInt(), input.nextInt(),
                    input.nextInt(), input.nextInt());
            boards[i] = current;
            if (current.xLow <= startX && startX < current.xHigh
                    && current.yLow <= startY && startY < current.yHigh) {
                start = i;
                trapped = current.xHigh - current.xLow == MINIMUM_SIDE
                        && current.yHigh - current.yLow == MINIMUM_SIDE
                        && startX == current.xLow + 1 && startY == current.yLow + 1;
            }
        }
        if (trapped) {
            System.out.println(1);
            return;
        }
        DisjointSet dsu = new DisjointSet(count);
        Event[] events = new Event[2 * count];
        for (int i = 0; i < count; i++) {
            Board current = boards[i];
            events[2 * i] = new Event(current.xHigh + 1, current.yLow, current.yHigh, i, 0);
            events[2 * i + 1] = new Event(current.xLow, current.yLow, current.yHigh, i, 1);
        }
        connect(events, dsu);
        for (int i = 0; i < count; i++) {
            Board current = boards[i];
            events[2 * i] = new Event(current.yHigh + 1, current.xLow, current.xHigh, i, 0);
            events[2 * i + 1] = new Event(current.yLow, current.xLow, current.xHigh, i, 1);
        }
        connect(events, dsu);
        System.out.println(dsu.size[dsu.find(start)]);
    }
}
