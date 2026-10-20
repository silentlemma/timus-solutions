import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class Main {
    private static final int UNSEEN = -1;
    private static final int BUFFER_SIZE = 1 << 16;

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
                    return UNSEEN;
                }
            }
            return buffer[position++];
        }

        int nextInt() throws IOException {
            int character = read();
            while (character <= ' ') {
                character = read();
            }
            int sign = 1;
            if (character == '-') {
                sign = UNSEEN;
                character = read();
            }
            int value = 0;
            while (character >= '0' && character <= '9') {
                value = value * 10 + character - '0';
                character = read();
            }
            return value * sign;
        }
    }

    private static final class Endpoint implements Comparable<Endpoint> {
        private final int position;
        private final int chord;

        Endpoint(int position, int chord) {
            this.position = position;
            this.chord = chord;
        }

        @Override
        public int compareTo(Endpoint other) {
            return Integer.compare(position, other.position);
        }
    }

    private static final class SegmentTree {
        private final int size;
        private final int missing;
        private final int[] minimum;
        private final int[] maximum;

        SegmentTree(int[] mate) {
            int base = 1;
            while (base < mate.length) {
                base *= 2;
            }
            size = base;
            missing = mate.length;
            minimum = new int[2 * size];
            maximum = new int[2 * size];
            Arrays.fill(minimum, missing);
            Arrays.fill(maximum, UNSEEN);
            for (int rank = 0; rank < mate.length; rank++) {
                minimum[size + rank] = mate[rank];
                maximum[size + rank] = mate[rank];
            }
            for (int node = size - 1; node > 0; node--) {
                pull(node);
            }
        }

        private void pull(int node) {
            minimum[node] = Math.min(minimum[2 * node], minimum[2 * node + 1]);
            maximum[node] = Math.max(maximum[2 * node], maximum[2 * node + 1]);
        }

        void remove(int position) {
            int node = size + position;
            minimum[node] = missing;
            maximum[node] = UNSEEN;
            for (node /= 2; node > 0; node /= 2) {
                pull(node);
            }
        }

        private int witness(int node, int left, int right) {
            if (minimum[node] < left) {
                return minimum[node];
            }
            if (maximum[node] > right) {
                return maximum[node];
            }
            return UNSEEN;
        }

        int crossing(int left, int right) {
            int start = size + left + 1;
            int finish = size + right;
            while (start < finish) {
                if (start % 2 == 1) {
                    int found = witness(start++, left, right);
                    if (found >= 0) {
                        return found;
                    }
                }
                if (finish % 2 == 1) {
                    int found = witness(--finish, left, right);
                    if (found >= 0) {
                        return found;
                    }
                }
                start /= 2;
                finish /= 2;
            }
            return UNSEEN;
        }
    }

    private static int location(int x, int y, int width, int height) {
        if (x < 0 || x > width || y < 0 || y > height) {
            return UNSEEN;
        }
        if (x == 0 || x == width || y == 0 || y == height) {
            return 0;
        }
        return 1;
    }

    private static int perimeter(int x, int y, int width, int height) {
        if (y == 0) {
            return x;
        }
        if (x == width) {
            return width + y;
        }
        if (y == height) {
            return width + height + width - x;
        }
        return 2 * width + height + height - y;
    }

    private static boolean solve(FastInput input) throws IOException {
        int count = input.nextInt();
        int width = input.nextInt();
        int height = input.nextInt();
        Endpoint[] points = new Endpoint[2 * count];
        int chords = 0;
        for (int pair = 0; pair < count; pair++) {
            int x1 = input.nextInt();
            int y1 = input.nextInt();
            int x2 = input.nextInt();
            int y2 = input.nextInt();
            int first = location(x1, y1, width, height);
            int second = location(x2, y2, width, height);
            if (first * second == UNSEEN) {
                return false;
            }
            if (first == 0 && second == 0) {
                points[2 * chords] = new Endpoint(perimeter(x1, y1, width, height), chords);
                points[2 * chords + 1] = new Endpoint(perimeter(x2, y2, width, height), chords);
                chords++;
            }
        }
        int endpoints = 2 * chords;
        Arrays.sort(points, 0, endpoints);
        int[] owner = new int[endpoints];
        int[] mate = new int[endpoints];
        int[] left = new int[chords];
        int[] right = new int[chords];
        int[] color = new int[chords];
        Arrays.fill(left, UNSEEN);
        Arrays.fill(color, UNSEEN);
        for (int rank = 0; rank < endpoints; rank++) {
            int chord = points[rank].chord;
            owner[rank] = chord;
            if (left[chord] == UNSEEN) {
                left[chord] = rank;
            } else {
                right[chord] = rank;
                mate[rank] = left[chord];
                mate[left[chord]] = rank;
            }
        }
        SegmentTree tree = new SegmentTree(mate);
        int[] queue = new int[chords];
        for (int root = 0; root < chords; root++) {
            if (color[root] != UNSEEN) {
                continue;
            }
            color[root] = 0;
            tree.remove(left[root]);
            tree.remove(right[root]);
            int tail = 0;
            queue[tail++] = root;
            for (int head = 0; head < tail; head++) {
                int chord = queue[head];
                while (true) {
                    int other = tree.crossing(left[chord], right[chord]);
                    if (other == UNSEEN) {
                        break;
                    }
                    int next = owner[other];
                    color[next] = color[chord] ^ 1;
                    tree.remove(left[next]);
                    tree.remove(right[next]);
                    queue[tail++] = next;
                }
            }
        }
        // Chords of one color must form properly nested pairs of endpoints.
        int[][] stacks = new int[2][chords];
        int[] sizes = new int[2];
        for (int rank = 0; rank < endpoints; rank++) {
            int chord = owner[rank];
            int side = color[chord];
            if (rank == left[chord]) {
                stacks[side][sizes[side]++] = chord;
            } else {
                if (sizes[side] == 0 || stacks[side][sizes[side] - 1] != chord) {
                    return false;
                }
                sizes[side]--;
            }
        }
        return true;
    }

    public static void main(String[] arguments) throws IOException {
        System.out.println(solve(new FastInput()) ? "YES" : "NO");
    }
}
