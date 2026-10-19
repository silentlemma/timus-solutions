import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int DECIMAL_BASE = 10;

    static final class Movie {
        int start, finish, count;

        Movie(int start, int finish, int count) {
            this.start = start;
            this.finish = finish;
            this.count = count;
        }
    }

    static int nextInt(BufferedInputStream in) throws IOException {
        int symbol;
        do {
            symbol = in.read();
        } while (symbol <= ' ' && symbol != -1);
        int value = 0;
        while (symbol >= '0' && symbol <= '9') {
            value = value * DECIMAL_BASE + symbol - '0';
            symbol = in.read();
        }
        return value;
    }

    static boolean augment(int vertex, boolean[][] edges, int[] own, int[] other,
                           boolean[] active, boolean[] visited) {
        for (int target = 0; target < active.length; ++target) {
            if (!edges[vertex][target] || !active[target] || visited[target])
                continue;
            visited[target] = true;
            int partner = other[target];
            if (partner < 0 || augment(partner, edges, own, other, active, visited)) {
                own[vertex] = target;
                other[target] = vertex;
                return true;
            }
        }
        return false;
    }

    static String chooseMovies(Movie[] movies, int students) {
        int size = movies.length;
        boolean[][] following = new boolean[size][size], preceding = new boolean[size][size];
        for (int first = 0; first < size; ++first) {
            for (int second = 0; second < size; ++second) {
                if (movies[first].finish <= movies[second].start &&
                    movies[first].count <= movies[second].count) {
                    following[first][second] = true;
                    preceding[second][first] = true;
                }
            }
        }
        int[] left = new int[size], right = new int[size];
        Arrays.fill(left, -1);
        Arrays.fill(right, -1);
        boolean[] active = new boolean[size];
        int chosen = 0, matching = 0;
        StringBuilder answer = new StringBuilder();
        for (int candidate = 0; candidate < size; ++candidate) {
            int[] oldLeft = left.clone(), oldRight = right.clone();
            int oldMatching = matching;
            if (augment(candidate, following, left, right, active, new boolean[size]))
                ++matching;
            active[candidate] = true;
            if (augment(candidate, preceding, right, left, active, new boolean[size]))
                ++matching;
            if (chosen + 1 - matching <= students) {
                answer.append('1');
                ++chosen;
            } else {
                answer.append('0');
                active[candidate] = false;
                left = oldLeft;
                right = oldRight;
                matching = oldMatching;
            }
        }
        return answer.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream in = new BufferedInputStream(System.in);
        int size = nextInt(in), students = nextInt(in);
        Movie[] movies = new Movie[size];
        for (int index = 0; index < size; ++index)
            movies[index] = new Movie(nextInt(in), nextInt(in), nextInt(in));
        System.out.println(chooseMovies(movies, students));
    }
}
