import java.util.HashMap;
import java.util.Map;

public class Main {

    static final int BUFFER_SIZE = 1024, BYTE_MASK = 255;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position >= available) {
            available = System.in.read(buffer);
            position = 0;
            if (available <= 0)
                return -1;
        }
        return buffer[position++] & BYTE_MASK;
    }
    static long nextLong() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }

    static String next() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        StringBuilder value = new StringBuilder();
        while (c > ' ') {
            value.append((char)c);
            c = read();
        }
        return value.toString();
    }

    static final int TEAM_SIZE = 3;
    static int[] clash;
    static int answer;

    static void search(int mask, int selected) {
        if (selected + Integer.bitCount(mask) <= answer)
            return;
        int chosen = 0, degree = 0;
        for (int remaining = mask; remaining != 0; remaining &= remaining - 1) {
            int i = Integer.numberOfTrailingZeros(remaining);
            int count = Integer.bitCount(mask & clash[i]);
            if (count > degree) {
                chosen = i;
                degree = count;
            }
        }
        // Take an edgeless remainder whole; otherwise try the team with
        // most conflicts first to tighten the bound for its skip branch.
        if (degree <= 1) {
            answer = Math.max(answer, selected + Integer.bitCount(mask));
            return;
        }
        search(mask & ~clash[chosen], selected + 1);
        search(mask & ~(1 << chosen), selected);
    }

    public static void main(String[] args) throws Exception {
        int k = (int)nextLong();
        int[][] teams = new int[k][TEAM_SIZE];
        int[] owners = new int[k * TEAM_SIZE];
        Map<String, Integer> people = new HashMap<>();
        for (int i = 0; i < k; i++)
            for (int j = 0; j < TEAM_SIZE; j++) {
                String name = next();
                Integer person = people.get(name);
                if (person == null) {
                    person = people.size();
                    people.put(name, person);
                }
                teams[i][j] = person;
                owners[person] |= 1 << i;
            }
        clash = new int[k];
        for (int i = 0; i < k; i++)
            for (int person : teams[i])
                clash[i] |= owners[person];
        search((1 << k) - 1, 0);
        System.out.println(answer);
    }
}
