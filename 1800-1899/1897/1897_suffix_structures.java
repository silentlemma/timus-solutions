import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    private static final int ALPHABET = 26;
    private static final int KEY_BITS = 60;
    private static final int NODE_FACTOR = 4;
    private static final int ROOT_SLACK = 30;

    private static void countSort(int[] order, int[] rank, int offset, int[] buffer,
                                  int[] count, int largest) {
        Arrays.fill(count, 0, largest + 2, 0);
        int n = order.length;
        for (int position : order) {
            int key = position + offset < n ? rank[position + offset] + 1 : 0;
            ++count[key];
        }
        int total = 0;
        for (int i = 0; i < largest + 2; ++i) {
            int amount = count[i];
            count[i] = total;
            total += amount;
        }
        for (int position : order) {
            int key = position + offset < n ? rank[position + offset] + 1 : 0;
            buffer[count[key]++] = position;
        }
    }

    private static int[][] suffixArray(char[] text) {
        int n = text.length;
        int[] order = new int[n];
        int[] rank = new int[n];
        int largest = 0;
        for (int i = 0; i < n; ++i) {
            order[i] = i;
            rank[i] = text[i];
            largest = Math.max(largest, rank[i]);
        }
        int[] count = new int[Math.max(n, largest) + 2];
        int[] buffer = new int[n];
        int[] following = new int[n];
        for (int distance = 1; ; distance *= 2) {
            countSort(order, rank, distance, buffer, count, largest);
            int[] swap = order;
            order = buffer;
            buffer = swap;
            countSort(order, rank, 0, buffer, count, largest);
            swap = order;
            order = buffer;
            buffer = swap;
            int classes = 0;
            following[order[0]] = 0;
            for (int i = 1; i < n; ++i) {
                int a = order[i - 1];
                int b = order[i];
                int tailA = a + distance < n ? rank[a + distance] + 1 : 0;
                int tailB = b + distance < n ? rank[b + distance] + 1 : 0;
                if (rank[a] != rank[b] || tailA != tailB) {
                    ++classes;
                }
                following[b] = classes;
            }
            swap = rank;
            rank = following;
            following = swap;
            if (classes + 1 == n) {
                return new int[][] {order, rank};
            }
            largest = classes;
        }
    }

    private static final class GameIndex {
        private final String text;
        private final char[] letters;
        private final int n;
        private final int[] suffixOrder;
        private final int[] rank;
        private final int[][] table;
        private final int[] logs;
        private final int[] depth;
        private final int[] parent;
        private final int[] firstChild;
        private final int[] nextSibling;
        private final int[] terminal;
        private final int[] representative;
        private final byte[] parity;
        private final byte[] winning;
        private final int[] roots = new int[ALPHABET + 1];
        private final long[] keys;
        private final int[] codes = new int[ALPHABET];
        private final int alphabetSize;
        private final int prefixBits;
        private final int prefixPairs;
        private final int[] counts;
        private int nodeCount;
        private int rootCount;
        private long total;

        private GameIndex(String value) {
            text = value;
            letters = value.toCharArray();
            n = letters.length;
            char[] combined = new char[2 * n + 1];
            for (int i = 0; i < n; ++i) {
                combined[i] = letters[i];
                combined[2 * n - i] = letters[i];
            }
            combined[n] = '#';
            int[][] suffix = suffixArray(combined);
            suffixOrder = suffix[0];
            rank = suffix[1];
            int size = combined.length;
            int[] lcp = new int[size];
            int height = 0;
            for (int position = 0; position < size; ++position) {
                int place = rank[position];
                if (place == 0) {
                    height = 0;
                    continue;
                }
                int other = suffixOrder[place - 1];
                while (position + height < size && other + height < size
                        && combined[position + height] == combined[other + height]) {
                    ++height;
                }
                lcp[place] = height;
                if (height > 0) {
                    --height;
                }
            }
            logs = new int[size + 1];
            for (int i = 2; i <= size; ++i) {
                logs[i] = logs[i / 2] + 1;
            }
            table = new int[logs[size] + 1][];
            table[0] = lcp;
            for (int level = 1, span = 1; 2 * span <= size; ++level, span *= 2) {
                int[] previous = table[level - 1];
                int[] row = new int[size - 2 * span + 1];
                for (int i = 0; i < row.length; ++i) {
                    row[i] = Math.min(previous[i], previous[i + span]);
                }
                table[level] = row;
            }
            int capacity = NODE_FACTOR * n + ROOT_SLACK;
            depth = new int[capacity];
            parent = new int[capacity];
            firstChild = new int[capacity];
            nextSibling = new int[capacity];
            terminal = new int[capacity];
            representative = new int[capacity];
            parity = new byte[capacity];
            winning = new byte[capacity];
            keys = new long[n];
            boolean[] present = new boolean[ALPHABET];
            for (char letter : letters) {
                present[letter - 'a'] = true;
            }
            int alphabet = 0;
            for (int i = 0; i < ALPHABET; ++i) {
                if (present[i]) {
                    codes[i] = alphabet++;
                }
            }
            alphabetSize = alphabet;
            prefixBits = Integer.SIZE - Integer.numberOfLeadingZeros(alphabet * alphabet);
            prefixPairs = alphabet == 1 ? 1 : KEY_BITS / prefixBits;
            int[] even = new int[n - 1];
            for (int i = 1; i < n; ++i) {
                even[i - 1] = i;
            }
            build(even, 0);
            int[] frequencies = new int[ALPHABET];
            for (char letter : letters) {
                ++frequencies[letter - 'a'];
            }
            for (int letter = 0; letter < ALPHABET; ++letter) {
                if (frequencies[letter] == 0) {
                    continue;
                }
                int[] centers = new int[frequencies[letter]];
                int used = 0;
                for (int i = 0; i < n; ++i) {
                    if (letters[i] - 'a' == letter) {
                        centers[used++] = i;
                    }
                }
                build(centers, 1);
            }
            int[] traversal = new int[nodeCount];
            int[] stack = new int[nodeCount];
            int top = 0;
            int visited = 0;
            for (int i = 0; i < rootCount; ++i) {
                stack[top++] = roots[i];
            }
            while (top > 0) {
                int node = stack[--top];
                traversal[visited++] = node;
                for (int child = firstChild[node]; child >= 0; child = nextSibling[child]) {
                    stack[top++] = child;
                }
            }
            for (int i = visited - 1; i >= 0; --i) {
                int node = traversal[i];
                int radius = depth[node];
                int best = terminal[node];
                for (int child = firstChild[node]; child >= 0; child = nextSibling[child]) {
                    int immediate = winning[child] ^ ((depth[child] - radius - 1) & 1);
                    if (immediate == 0) {
                        winning[node] = 1;
                    }
                    int center = representative[child];
                    if (best < 0 || rank[center - radius] < rank[best - radius]) {
                        best = center;
                    }
                }
                representative[node] = best;
            }
            int[] difference = new int[n + 2];
            for (int node = 0; node < nodeCount; ++node) {
                if (parent[node] < 0) {
                    if (parity[node] == 1 && winning[node] == 1) {
                        int start = representative[node];
                        ++difference[start];
                        --difference[start + 2];
                    }
                    continue;
                }
                int low = depth[parent[node]] + 1;
                int high = depth[node];
                int center = representative[node];
                int wanted = (center - ((high + 1 - winning[node]) & 1)) & 1;
                int left = center - high;
                int right = center - low;
                if ((left & 1) != wanted) {
                    ++left;
                }
                if ((right & 1) != wanted) {
                    --right;
                }
                if (left <= right) {
                    ++difference[left];
                    --difference[right + 2];
                }
            }
            for (int i = 2; i < n; ++i) {
                difference[i] += difference[i - 2];
            }
            counts = Arrays.copyOf(difference, n);
            total = winning[roots[0]];
            for (int amount : counts) {
                total += amount;
            }
        }

        private int lce(int a, int b) {
            if (a == b) {
                return rank.length - a;
            }
            int left = Math.min(rank[a], rank[b]);
            int right = Math.max(rank[a], rank[b]);
            int level = logs[right - left];
            return Math.min(table[level][left + 1], table[level][right - (1 << level) + 1]);
        }

        private int radius(int center, int kind) {
            return Math.min(center, n - center - kind);
        }

        private int common(int a, int b, int kind) {
            int cap = Math.min(radius(a, kind), radius(b, kind));
            if (cap == 0) {
                return 0;
            }
            int edge = 2 * n + 1;
            return Math.min(cap, Math.min(lce(edge - a, edge - b), lce(a + kind, b + kind)));
        }

        private int compare(int a, int b, int kind) {
            int order = Long.compare(keys[a], keys[b]);
            if (order != 0) {
                return order;
            }
            int shared = common(a, b, kind);
            int ra = radius(a, kind);
            int rb = radius(b, kind);
            if (shared == Math.min(ra, rb)) {
                return Integer.compare(ra, rb);
            }
            int left = Character.compare(letters[a - shared - 1], letters[b - shared - 1]);
            return left != 0
                       ? left
                       : Character.compare(letters[a + shared + kind], letters[b + shared + kind]);
        }

        private void sortCenters(int[] centers, int kind) {
            int[] from = centers;
            int[] to = new int[centers.length];
            for (int width = 1; width < centers.length; width *= 2) {
                for (int begin = 0; begin < centers.length; begin += 2 * width) {
                    int middle = Math.min(begin + width, centers.length);
                    int end = Math.min(begin + 2 * width, centers.length);
                    int a = begin;
                    int b = middle;
                    for (int at = begin; at < end; ++at) {
                        if (a < middle && (b == end || compare(from[a], from[b], kind) <= 0)) {
                            to[at] = from[a++];
                        } else {
                            to[at] = from[b++];
                        }
                    }
                }
                int[] swap = from;
                from = to;
                to = swap;
            }
            if (from != centers) {
                System.arraycopy(from, 0, centers, 0, centers.length);
            }
        }

        private int newNode(int radius, int kind, int center) {
            int node = nodeCount++;
            depth[node] = radius;
            parity[node] = (byte) kind;
            firstChild[node] = -1;
            nextSibling[node] = -1;
            parent[node] = -1;
            terminal[node] = center;
            representative[node] = -1;
            return node;
        }

        private void attach(int boss, int child) {
            parent[child] = boss;
            nextSibling[child] = firstChild[boss];
            firstChild[boss] = child;
        }

        private void build(int[] centers, int kind) {
            int root = newNode(0, kind, -1);
            roots[rootCount++] = root;
            for (int center : centers) {
                int radius = radius(center, kind);
                long key = 0;
                for (int offset = 0; offset < prefixPairs; ++offset) {
                    key <<= prefixBits;
                    if (offset < radius) {
                        key += codes[letters[center - offset - 1] - 'a'] * alphabetSize
                               + codes[letters[center + offset + kind] - 'a'] + 1;
                    }
                }
                keys[center] = key;
            }
            sortCenters(centers, kind);
            int[] stack = new int[2 * centers.length + 1];
            int top = 1;
            stack[0] = root;
            int previousCenter = -1;
            for (int center : centers) {
                int shared = previousCenter < 0 ? 0 : common(previousCenter, center, kind);
                int last = -1;
                while (depth[stack[top - 1]] > shared) {
                    int popped = stack[--top];
                    if (last >= 0) {
                        attach(popped, last);
                    }
                    last = popped;
                }
                if (depth[stack[top - 1]] < shared) {
                    int node = newNode(shared, kind, -1);
                    attach(node, last);
                    stack[top++] = node;
                } else if (last >= 0) {
                    attach(stack[top - 1], last);
                }
                int radius = radius(center, kind);
                if (radius > depth[stack[top - 1]]) {
                    stack[top++] = newNode(radius, kind, center);
                } else {
                    int node = stack[top - 1];
                    int old = terminal[node];
                    if (old < 0 || rank[center - radius] < rank[old - radius]) {
                        terminal[node] = center;
                    }
                }
                previousCenter = center;
            }
            while (top > 1) {
                int child = stack[--top];
                attach(stack[top - 1], child);
            }
        }

        private String kth(long k) {
            if (k > total) {
                return "no solution";
            }
            if (winning[roots[0]] == 1) {
                if (k == 1) {
                    return "-";
                }
                --k;
            }
            int start = -1;
            for (int position : suffixOrder) {
                if (position >= n) {
                    continue;
                }
                if (k > counts[position]) {
                    k -= counts[position];
                } else {
                    start = position;
                    break;
                }
            }
            int[] lengths = new int[nodeCount];
            int used = 0;
            for (int node = 0; node < nodeCount; ++node) {
                if (parent[node] < 0) {
                    if (parity[node] == 1 && winning[node] == 1 && representative[node] == start) {
                        lengths[used++] = 1;
                    }
                    continue;
                }
                int radius = representative[node] - start;
                if (depth[parent[node]] < radius && radius <= depth[node]
                        && (winning[node] ^ ((depth[node] - radius) & 1)) == 1) {
                    lengths[used++] = 2 * radius + parity[node];
                }
            }
            Arrays.sort(lengths, 0, used);
            return text.substring(start, start + lengths[(int) k - 1]);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String text = input.readLine().trim();
        long k = Long.parseLong(input.readLine().trim());
        System.out.println(new GameIndex(text).kth(k));
    }
}
