import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static final int SECONDS_PER_MINUTE = 60;
    private static final int SECONDS_PER_HOUR = SECONDS_PER_MINUTE * SECONDS_PER_MINUTE;
    private static final int MAX_INTERVAL = 500;

    private static int parseTime(String text) {
        String[] parts = text.split(":");
        int hour = Integer.parseInt(parts[0]);
        int minute = Integer.parseInt(parts[1]);
        int second = Integer.parseInt(parts[2]);
        return hour * SECONDS_PER_HOUR + minute * SECONDS_PER_MINUTE + second;
    }

    private static void appendPair(StringBuilder output, int value) {
        if (value < 10) {
            output.append('0');
        }
        output.append(value);
    }

    private static void appendTime(StringBuilder output, int seconds) {
        appendPair(output, seconds / SECONDS_PER_HOUR);
        output.append(':');
        appendPair(output, seconds / SECONDS_PER_MINUTE % SECONDS_PER_MINUTE);
        output.append(':');
        appendPair(output, seconds % SECONDS_PER_MINUTE);
        output.append('\n');
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer intervals = new StringTokenizer(input.readLine());
        int takeTake = Integer.parseInt(intervals.nextToken());
        int takeLand = Integer.parseInt(intervals.nextToken());
        int landTake = Integer.parseInt(intervals.nextToken());
        int landLand = Integer.parseInt(intervals.nextToken());
        int n = Integer.parseInt(input.readLine());
        int[] departures = new int[n];
        int[] takeResult = new int[n];
        for (int i = 0; i < n; ++i) {
            departures[i] = parseTime(input.readLine());
        }
        int m = Integer.parseInt(input.readLine());
        int[] landings = new int[m];
        int[] landResult = new int[m];
        for (int i = 0; i < m; ++i) {
            landings[i] = parseTime(input.readLine());
        }
        int takeIndex = 0;
        int landIndex = 0;
        int lastTake = -MAX_INTERVAL;
        int lastLand = -MAX_INTERVAL;
        while (takeIndex < n || landIndex < m) {
            int ready = 0;
            if (takeIndex < n) {
                ready = Math.max(departures[takeIndex],
                        Math.max(lastTake + takeTake, lastLand + landTake));
            }
            if (landIndex < m && (takeIndex == n || landings[landIndex] <= ready)) {
                lastLand = Math.max(landings[landIndex],
                        Math.max(lastTake + takeLand, lastLand + landLand));
                landResult[landIndex++] = lastLand;
            } else {
                lastTake = ready;
                takeResult[takeIndex++] = lastTake;
            }
        }
        StringBuilder output = new StringBuilder();
        for (int time : takeResult) {
            appendTime(output, time);
        }
        for (int time : landResult) {
            appendTime(output, time);
        }
        System.out.print(output);
    }
}
