import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Main {
    private static final int DIRECTION_COUNT = 4;
    private static final int LEFT_TURN = 3;
    private static final int BUFFER_SIZE = 65536;
    private static final int[] ROW_STEP = {-1, 0, 1, 0};
    private static final int[] COLUMN_STEP = {0, 1, 0, -1};

    private static final class FastInput {
        private final InputStream stream = System.in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position;
        private int length;

        private int read() throws IOException {
            if (position == length) {
                length = stream.read(buffer);
                position = 0;
                if (length < 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int nextInt() throws IOException {
            int value = read();
            while (value <= ' ') {
                value = read();
            }
            int answer = 0;
            while (value > ' ') {
                answer = answer * 10 + value - '0';
                value = read();
            }
            return answer;
        }

        char[] nextRow(int width) throws IOException {
            int value = read();
            while (value <= ' ') {
                value = read();
            }
            char[] row = new char[width];
            for (int column = 0; column < width; ++column) {
                row[column] = (char) value;
                value = read();
            }
            return row;
        }
    }

    private static final class SegmentTree {
        private final int base;
        private final int[] tree;

        SegmentTree(int count) {
            int size = 1;
            while (size < count) {
                size *= 2;
            }
            base = size;
            tree = new int[base * 2];
        }

        void update(int position, int value) {
            int node = base + position;
            tree[node] = value;
            while (node > 1) {
                node /= 2;
                tree[node] = Math.max(tree[node * 2], tree[node * 2 + 1]);
            }
        }

        int query(int left, int right) {
            int answer = 0;
            left += base;
            right += base;
            while (left < right) {
                if ((left & 1) != 0) {
                    answer = Math.max(answer, tree[left++]);
                }
                if ((right & 1) != 0) {
                    answer = Math.max(answer, tree[--right]);
                }
                left /= 2;
                right /= 2;
            }
            return answer;
        }
    }

    private static final class Event implements Comparable<Event> {
        private final int time;
        private final int row;
        private final int column;
        private final char turn;

        Event(int time, int row, int column, char turn) {
            this.time = time;
            this.row = row;
            this.column = column;
            this.turn = turn;
        }

        @Override
        public int compareTo(Event other) {
            if (time != other.time) {
                return Integer.compare(time, other.time);
            }
            if (row != other.row) {
                return Integer.compare(row, other.row);
            }
            if (column != other.column) {
                return Integer.compare(column, other.column);
            }
            return Character.compare(turn, other.turn);
        }
    }

    private static int lca(int first, int second, int[] parent, int[] depth, int[] head) {
        while (head[first] != head[second]) {
            if (depth[head[first]] > depth[head[second]]) {
                first = parent[head[first]];
            } else {
                second = parent[head[second]];
            }
        }
        return depth[first] < depth[second] ? first : second;
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int rows = input.nextInt();
        int columns = input.nextInt();
        int height = rows * 2 - 1;
        int width = columns * 2 - 1;
        char[][] map = new char[height][];
        int root = -1;
        for (int row = 0; row < height; ++row) {
            map[row] = input.nextRow(width);
            if ((row & 1) == 0) {
                for (int column = 0; column < width; column += 2) {
                    if (map[row][column] == 'S') {
                        root = row / 2 * columns + column / 2;
                    }
                }
            }
        }

        int capacity = rows * columns;
        int[] parent = new int[capacity];
        int[] depth = new int[capacity];
        int[] incoming = new int[capacity];
        int[] firstChild = new int[capacity];
        int[] nextSibling = new int[capacity];
        int[] preorder = new int[capacity];
        int[] position = new int[capacity];
        int[] stack = new int[capacity];
        char[] desired = new char[capacity];
        Arrays.fill(firstChild, -1);
        Arrays.fill(nextSibling, -1);
        parent[root] = root;
        stack[0] = root;
        int stackSize = 1;
        int count = 0;
        while (stackSize > 0) {
            int node = stack[--stackSize];
            position[node] = count;
            preorder[count++] = node;
            int row = node / columns;
            int column = node % columns;
            for (int direction = 0; direction < DIRECTION_COUNT; ++direction) {
                int nextRow = row + ROW_STEP[direction];
                int nextColumn = column + COLUMN_STEP[direction];
                if (nextRow < 0 || nextRow >= rows || nextColumn < 0 || nextColumn >= columns) {
                    continue;
                }
                char edge = map[row * 2 + ROW_STEP[direction]]
                    [column * 2 + COLUMN_STEP[direction]];
                char expected = (direction & 1) == 0 ? '|' : '-';
                if (edge != expected) {
                    continue;
                }
                int child = nextRow * columns + nextColumn;
                if (child == parent[node]) {
                    continue;
                }
                parent[child] = node;
                depth[child] = depth[node] + 1;
                incoming[child] = direction;
                int turn = (direction - incoming[node] + DIRECTION_COUNT) % DIRECTION_COUNT;
                desired[child] = turn == 0 ? 'F' : turn == LEFT_TURN ? 'L' : 'R';
                nextSibling[child] = firstChild[node];
                firstChild[node] = child;
                stack[stackSize++] = child;
            }
        }

        int[] subtreeSize = new int[capacity];
        int[] heavy = new int[capacity];
        int[] preferred = new int[capacity];
        int[] head = new int[capacity];
        Arrays.fill(heavy, -1);
        for (int index = count - 1; index >= 0; --index) {
            int node = preorder[index];
            subtreeSize[node] = 1;
            preferred[node] = node;
            char initial = map[node / columns * 2][node % columns * 2];
            for (int child = firstChild[node]; child != -1; child = nextSibling[child]) {
                subtreeSize[node] += subtreeSize[child];
                if (heavy[node] == -1 || subtreeSize[child] > subtreeSize[heavy[node]]) {
                    heavy[node] = child;
                }
                if (node == root || desired[child] == initial) {
                    preferred[node] = preferred[child];
                }
            }
        }
        head[root] = root;
        for (int index = 1; index < count; ++index) {
            int node = preorder[index];
            int previous = parent[node];
            head[node] = heavy[previous] == node ? head[previous] : node;
        }

        SegmentTree latest = new SegmentTree(count);
        int trains = input.nextInt();
        int[] destination = new int[trains + 1];
        List<Event> events = new ArrayList<Event>();
        int previousDestination = -1;
        for (int train = 1; train <= trains; ++train) {
            int time = input.nextInt();
            int row = input.nextInt() - 1;
            int column = input.nextInt() - 1;
            int target = row * columns + column;
            destination[train] = target;
            if (target == previousDestination) {
                continue;
            }
            previousDestination = target;
            int scope = root;
            while (true) {
                int last = latest.query(position[scope], position[scope] + subtreeSize[scope]);
                int endpoint = last == 0 ? preferred[scope] : destination[last];
                if (endpoint == target) {
                    break;
                }
                // The two paths agree until the first switch that needs changing.
                int junction = lca(target, endpoint, parent, depth, head);
                int child = firstChild[junction];
                while (position[target] < position[child]
                    || position[target] >= position[child] + subtreeSize[child]) {
                    child = nextSibling[child];
                }
                events.add(new Event(time + depth[junction], junction / columns + 1,
                    junction % columns + 1, desired[child]));
                scope = child;
            }
            latest.update(position[target], train);
        }

        Collections.sort(events);
        StringBuilder output = new StringBuilder();
        output.append(events.size()).append('\n');
        for (Event event : events) {
            output.append(event.time).append(' ').append(event.row).append(' ')
                .append(event.column).append(' ').append(event.turn).append('\n');
        }
        System.out.print(output);
    }
}
