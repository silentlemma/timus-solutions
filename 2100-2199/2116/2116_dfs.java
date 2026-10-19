import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int a = input.nextInt();
        int b = input.nextInt();
        if (b == 0) {
            System.out.println((long) n * n);
            return;
        }

        // For these moves, components stabilize at a side of twice b.
        int side = Math.min(n, 2 * b);
        boolean[] seen = new boolean[side * side];
        int[] stack = new int[side * side];
        int answer = 0;
        for (int start = 0; start < seen.length; start++) {
            if (seen[start]) {
                continue;
            }
            answer++;
            seen[start] = true;
            int size = 0;
            stack[size++] = start;
            while (size > 0) {
                int cell = stack[--size];
                int x = cell / side;
                int y = cell % side;
                for (int orientation = 0; orientation < 2; orientation++) {
                    int dx = orientation == 0 ? a : b;
                    int dy = orientation == 0 ? b : a;
                    for (int sx = -1; sx <= 1; sx += 2) {
                        for (int sy = -1; sy <= 1; sy += 2) {
                            int nx = x + sx * dx;
                            int ny = y + sy * dy;
                            if (nx < 0 || nx >= side || ny < 0 || ny >= side) {
                                continue;
                            }
                            int next = nx * side + ny;
                            if (!seen[next]) {
                                seen[next] = true;
                                stack[size++] = next;
                            }
                        }
                    }
                }
            }
        }
        System.out.println(answer);
    }
}
