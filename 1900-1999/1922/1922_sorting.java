import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    private static final BufferedInputStream INPUT = new BufferedInputStream(System.in);

    private static int nextInt() throws IOException {
        int value;
        do {
            value = INPUT.read();
        } while (value <= ' ' && value >= 0);
        int result = 0;
        while (value > ' ') {
            result = result * 10 + value - '0';
            value = INPUT.read();
        }
        return result;
    }

    static int[][] reliableTeams(int[] values) {
        int count = values.length;
        Integer[] order = new Integer[count];
        for (int index = 0; index < count; ++index) {
            order[index] = index;
        }
        Arrays.sort(order, (first, second) -> {
            int compared = Integer.compare(values[first], values[second]);
            return compared != 0 ? compared : Integer.compare(first, second);
        });
        ArrayList<int[]> teams = new ArrayList<>();
        int[] members = new int[count];
        for (int size = 1; size <= count; ++size) {
            members[size - 1] = order[size - 1] + 1;
            if (values[order[size - 1]] <= size
                    && (size == count || values[order[size]] > size + 1)) {
                teams.add(Arrays.copyOf(members, size));
            }
        }
        return teams.toArray(new int[teams.size()][]);
    }

    public static void main(String[] args) throws IOException {
        int count = nextInt();
        int[] values = new int[count];
        for (int index = 0; index < count; ++index) {
            values[index] = nextInt();
        }
        int[][] teams = reliableTeams(values);
        StringBuilder output = new StringBuilder();
        output.append(teams.length).append('\n');
        for (int[] team : teams) {
            output.append(team.length);
            for (int member : team) {
                output.append(' ').append(member);
            }
            output.append('\n');
        }
        System.out.print(output);
    }
}
