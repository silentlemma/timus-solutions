import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    static final int WIDTH = 6, FULL = 100, NONE = -1, CODE = 3;

    // percents of total that round each value down or up and add up to 100:
    // round all down, then raise the ones with the largest remainders
    static int[] shares(int[] values, int total) {
        int n = values.length;
        int[] out = new int[n];
        if (total == 0) {
            java.util.Arrays.fill(out, NONE);
            return out;
        }
        Integer[] order = new Integer[n];
        int[] rest = new int[n];
        int sum = 0;
        for (int k = 0; k < n; k++) {
            out[k] = FULL * values[k] / total;
            rest[k] = FULL * values[k] % total;
            order[k] = k;
            sum += out[k];
        }
        java.util.Arrays.sort(order, (a, b) -> rest[b] - rest[a]);
        for (int k = 0; k < FULL - sum; k++) {
            out[order[k]]++;
        }
        return out;
    }

    static String cell(String s) { return String.format("%" + WIDTH + "s", s); }

    static String percent(int p) { return cell(p == NONE ? "-" : p + "%"); }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        List<String> lines = new ArrayList<>();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            lines.add(line);
        }
        String survey = lines.get(0);
        int at = 1;
        // each question: its line, then the lines of its answers
        List<List<String>> questions = new ArrayList<>();
        Map<String, Integer> place = new HashMap<>();
        for (; !lines.get(at).equals("#"); at++) {
            String line = lines.get(at);
            if (line.startsWith(" ")) {
                questions.get(questions.size() - 1).add(line);
            } else {
                place.put(line.substring(0, CODE), questions.size());
                questions.add(new ArrayList<>());
                questions.get(questions.size() - 1).add(line);
            }
        }
        List<String> results = new ArrayList<>();
        for (at++; !lines.get(at).equals("#"); at++) {
            results.add(lines.get(at));
        }
        StringBuilder out = new StringBuilder();
        for (at++; at < lines.size() && !lines.get(at).equals("#"); at++) {
            String spec = lines.get(at);
            int p1 = place.get(spec.substring(0, CODE)),
                p2 = place.get(spec.substring(CODE + 1, 2 * CODE + 1));
            List<String> first = questions.get(p1), second = questions.get(p2);
            String c1 = first.get(0).substring(0, CODE), c2 = second.get(0).substring(0, CODE);
            int rows = first.size() - 1, cols = second.size() - 1;
            StringBuilder a1 = new StringBuilder(), a2 = new StringBuilder();
            for (int i = 1; i <= rows; i++) {
                a1.append(first.get(i).charAt(1));
            }
            for (int j = 1; j <= cols; j++) {
                a2.append(second.get(j).charAt(1));
            }
            // the table with its totals as one more column and one more row
            int[][] table = new int[rows + 1][cols + 1];
            for (String line : results) {
                int r = a1.indexOf(String.valueOf(line.charAt(p1)));
                int c = a2.indexOf(String.valueOf(line.charAt(p2)));
                for (int i : new int[] {r, rows}) {
                    for (int j : new int[] {c, cols}) {
                        table[i][j]++;
                    }
                }
            }
            int[][] byRow = new int[rows + 1][cols + 1], byCol = new int[rows + 1][cols + 1];
            for (int i = 0; i <= rows; i++) {
                int[] got = shares(java.util.Arrays.copyOf(table[i], cols), table[i][cols]);
                System.arraycopy(got, 0, byRow[i], 0, cols);
                byRow[i][cols] = table[i][cols] > 0 ? FULL : NONE;
            }
            for (int j = 0; j <= cols; j++) {
                int[] part = new int[rows];
                for (int i = 0; i < rows; i++) {
                    part[i] = table[i][j];
                }
                int[] got = shares(part, table[rows][j]);
                for (int i = 0; i < rows; i++) {
                    byCol[i][j] = got[i];
                }
                byCol[rows][j] = table[rows][j] > 0 ? FULL : NONE;
            }
            if (out.length() > 0) {
                out.append('\n');
            }
            out.append(survey).append(" - ").append(spec.substring(2 * CODE + 2)).append('\n');
            for (List<String> q : java.util.Arrays.asList(first, second)) {
                for (String line : q) {
                    out.append(line).append('\n');
                }
            }
            out.append('\n').append(cell(""));
            for (int j = 0; j < cols; j++) {
                out.append(cell(c2 + ":" + a2.charAt(j)));
            }
            out.append(cell("TOTAL")).append('\n');
            for (int i = 0; i <= rows; i++) {
                out.append(cell(i < rows ? c1 + ":" + a1.charAt(i) : "TOTAL"));
                for (int v : table[i]) {
                    out.append(cell(String.valueOf(v)));
                }
                for (int[] ps : new int[][] {byRow[i], byCol[i]}) {
                    out.append('\n').append(cell(""));
                    for (int p : ps) {
                        out.append(percent(p));
                    }
                }
                out.append('\n');
            }
        }
        System.out.print(out);
    }
}
