import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), k = in.nextInt(), m = in.nextInt();
        // rooms in turn: every room gets someone, and the split is as even as
        // possible, which leaves the most pairs from different rooms
        int[] room = new int[n];
        for (int i = 0; i < n; i++)
            room[i] = i % k;
        // neighbours in this order always have different rooms
        List<int[]> days = new ArrayList<>();
        for (int i = 0; i + 1 < n; i += 2)
            days.add(new int[] {i, i + 1});
        if (n % 2 == 1)
            days.add(new int[] {room[n - 1] == room[0] ? 1 : 0, n - 1});
        boolean[][] used = new boolean[n][n];
        for (int[] d : days)
            used[d[0]][d[1]] = true;
        for (int i = 0; i < n && days.size() < m; i++)
            for (int j = i + 1; j < n && days.size() < m; j++)
                if (room[i] != room[j] && !used[i][j])
                    days.add(new int[] {i, j});
        StringBuilder sb = new StringBuilder();
        for (int r : room)
            sb.append(r + 1).append('\n');
        for (int d = 0; d < m; d++)
            sb.append(days.get(d)[0] + 1).append(' ').append(days.get(d)[1] + 1).append('\n');
        System.out.print(sb);
    }
}
