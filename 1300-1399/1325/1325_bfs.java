import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static final byte WALL = '0';

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder all = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine())
            all.append(line).append(' ');
        StringTokenizer words = new StringTokenizer(all.toString());
        int n = Integer.parseInt(words.nextToken()), m = Integer.parseInt(words.nextToken());
        int sr = Integer.parseInt(words.nextToken()), sc = Integer.parseInt(words.nextToken());
        int tr = Integer.parseInt(words.nextToken()), tc = Integer.parseInt(words.nextToken());
        int width = m + 2;
        // the plan with a frame of walls, as one flat array
        byte[] grid = new byte[width * (n + 2)];
        Arrays.fill(grid, WALL);
        for (int r = 1; r <= n; r++) {
            String row = words.nextToken();
            for (int c = 1; c <= m && c <= row.length(); c++)
                grid[r * width + c] = (byte)row.charAt(c - 1);
        }
        int[] steps = new int[grid.length];
        int[] seeded = new int[grid.length]; // the layer that last took the cell as a seed
        Arrays.fill(steps, -1);
        Arrays.fill(seeded, -1);
        int[] moves = {-width - 1, -width, -width + 1, -1, 1, width - 1, width, width + 1};
        int start = sr * width + sc, target = tr * width + tc;
        // layer c holds the cells first reached after c changes of shoes, all of
        // the same kind; seeds come in sorted by the number of steps
        byte kind = grid[start];
        int changes = 0;
        int[] seedLevel = new int[grid.length + 1];
        int[] seedCell = new int[seedLevel.length];
        int[] laterLevel = new int[seedLevel.length], laterCell = new int[seedLevel.length];
        int[] current = new int[grid.length], following = new int[grid.length];
        int seedCount = 1;
        seedCell[0] = start;
        while (seedCount > 0 && steps[target] < 0) {
            int laterCount = 0, currentCount = 0, i = 0, level = seedLevel[0];
            while ((i < seedCount || currentCount > 0) && steps[target] < 0) {
                if (currentCount == 0 && seedLevel[i] > level)
                    level = seedLevel[i];
                for (; i < seedCount && seedLevel[i] == level; i++) {
                    int cell = seedCell[i];
                    if (steps[cell] < 0) {
                        steps[cell] = level;
                        current[currentCount++] = cell;
                    }
                }
                int followingCount = 0;
                for (int k = 0; k < currentCount; k++) {
                    for (int move : moves) {
                        int near = current[k] + move;
                        if (steps[near] >= 0 || grid[near] == WALL)
                            continue;
                        if (grid[near] == kind) {
                            steps[near] = level + 1;
                            following[followingCount++] = near;
                        } else if (seeded[near] != changes) {
                            seeded[near] = changes;
                            laterLevel[laterCount] = level + 1;
                            laterCell[laterCount++] = near;
                        }
                    }
                }
                int[] swap = current;
                current = following;
                following = swap;
                currentCount = followingCount;
                level++;
            }
            if (steps[target] < 0) {
                if (laterCount > 0)
                    kind = grid[laterCell[0]];
                changes++;
                int[] swap = seedLevel;
                seedLevel = laterLevel;
                laterLevel = swap;
                swap = seedCell;
                seedCell = laterCell;
                laterCell = swap;
                seedCount = laterCount;
            }
        }
        if (steps[target] < 0)
            System.out.println("0 0");
        else
            System.out.println((steps[target] + 1) + " " + changes);
    }
}
