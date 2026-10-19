import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;

public class Main {
    private static int nextInt(StreamTokenizer input) throws IOException {
        input.nextToken();
        return (int) input.nval;
    }

    private static final class Schedule {
        final int busy;
        final int[][] starts;

        Schedule(int busy, int[][] starts) {
            this.busy = busy;
            this.starts = starts;
        }
    }

    private static Schedule solve(int window, int capacity, int[] deadlines) {
        int n = deadlines.length;
        int width = n + 1;
        int stateCount = width * width;
        int target = stateCount - 1;
        int infinity = deadlines[n - 1] + 1;
        int[] releases = new int[n];
        for (int i = 0; i < n; ++i) {
            releases[i] = Math.max(0, deadlines[i] - window);
        }
        int[][] layers = new int[2 * n + 1][];
        int[][] parents = new int[2 * n + 1][];
        layers[0] = new int[stateCount];
        Arrays.fill(layers[0], infinity);
        layers[0][0] = -1;
        int[] active = new int[stateCount];
        int activeCount = 1;
        for (int busy = 1; busy <= 2 * n; ++busy) {
            int[] following = new int[stateCount];
            int[] previous = new int[stateCount];
            Arrays.fill(following, infinity);
            Arrays.fill(previous, -1);
            int[] nextActive = new int[stateCount];
            int nextCount = 0;
            for (int at = 0; at < activeCount; ++at) {
                int state = active[at];
                int firstDone = state / width;
                int secondDone = state % width;
                int earliest = layers[busy - 1][state] + 1;
                for (int newFirst = 0; newFirst <= Math.min(capacity, n - firstDone);
                        ++newFirst) {
                    int newSecond = Math.min(capacity - newFirst, firstDone - secondDone);
                    if (newFirst + newSecond == 0) {
                        continue;
                    }
                    int ni = firstDone + newFirst;
                    int nj = secondDone + newSecond;
                    int minute = newFirst > 0 ? Math.max(earliest, releases[ni - 1]) : earliest;
                    if (newSecond > 0 && minute >= deadlines[secondDone]) {
                        continue;
                    }
                    if (nj < n) {
                        int remainingSides = nj < ni ? 1 : 2;
                        if (minute + 1 + remainingSides > deadlines[nj]) {
                            continue;
                        }
                    }
                    int destination = ni * width + nj;
                    if (minute < following[destination]) {
                        if (following[destination] == infinity) {
                            nextActive[nextCount++] = destination;
                        }
                        following[destination] = minute;
                        previous[destination] = state;
                    }
                }
            }
            layers[busy] = following;
            parents[busy] = previous;
            if (following[target] != infinity) {
                int[][] starts = new int[n][2];
                int state = target;
                for (int used = busy; used > 0; --used) {
                    int oldState = parents[used][state];
                    int ni = state / width;
                    int nj = state % width;
                    int oi = oldState / width;
                    int oj = oldState % width;
                    int minute = layers[used][state];
                    for (int job = oi; job < ni; ++job) {
                        starts[job][0] = minute;
                    }
                    for (int job = oj; job < nj; ++job) {
                        starts[job][1] = minute;
                    }
                    state = oldState;
                }
                return new Schedule(busy, starts);
            }
            if (nextCount == 0) {
                return new Schedule(-1, new int[0][2]);
            }
            active = nextActive;
            activeCount = nextCount;
        }
        return new Schedule(-1, new int[0][2]);
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer input = new StreamTokenizer(
                new BufferedReader(new InputStreamReader(System.in)));
        int window = nextInt(input);
        int capacity = nextInt(input);
        int n = nextInt(input);
        int[] deadlines = new int[n];
        for (int i = 0; i < n; ++i) {
            deadlines[i] = nextInt(input);
        }
        Schedule answer = solve(window, capacity, deadlines);
        StringBuilder output = new StringBuilder().append(answer.busy).append('\n');
        for (int[] starts : answer.starts) {
            output.append(starts[0]).append(' ').append(starts[1]).append('\n');
        }
        System.out.print(output);
    }
}
