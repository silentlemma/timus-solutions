import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    // front, back, down, up, left, right: face 2a + side lies on axis a
    static final String FACES = "FBDULR";
    static final int SIDES = FACES.length();
    static final int AXES = SIDES / 2;
    // the axis other than a and b is AXIS_SUM - a - b
    static final int AXIS_SUM = AXES * (AXES - 1) / 2;
    static final char INSIDE = '.';
    // quarter turns about the vertical and the front-back axis: the face at
    // each letter's place comes from the place of the next letter, cyclically
    static final String[] QUARTER_TURNS = {"FLBR", "DLUR"};

    // every turn: p puts the old face p[k] at place k, and the two quarter
    // turns generate all 24
    static List<int[]> rotations() {
        int[] start = new int[SIDES];
        for (int k = 0; k < SIDES; k++) {
            start[k] = k;
        }
        List<int[]> turns = new ArrayList<>();
        for (String cycle : QUARTER_TURNS) {
            int[] p = start.clone();
            for (int i = 0; i < cycle.length(); i++) {
                char next = cycle.charAt((i + 1) % cycle.length());
                p[FACES.indexOf(cycle.charAt(i))] = FACES.indexOf(next);
            }
            turns.add(p);
        }
        Set<String> seen = new HashSet<>();
        seen.add(Arrays.toString(start));
        List<int[]> all = new ArrayList<>();
        all.add(start);
        ArrayDeque<int[]> todo = new ArrayDeque<>(all);
        while (!todo.isEmpty()) {
            int[] p = todo.pop();
            for (int[] q : turns) {
                int[] r = new int[SIDES];
                for (int k = 0; k < SIDES; k++) {
                    r[k] = p[q[k]];
                }
                if (seen.add(Arrays.toString(r))) {
                    all.add(r);
                    todo.push(r);
                }
            }
        }
        return all;
    }

    // the extents and colours of a turned piece, written as one string
    static String turned(int[] p, int[] dims, String colors) {
        StringBuilder s = new StringBuilder();
        for (int a = 0; a < AXES; a++) {
            s.append(dims[p[2 * a] / 2]).append(',');
        }
        for (int k = 0; k < SIDES; k++) {
            s.append(colors.charAt(p[k]));
        }
        return s.toString();
    }

    static List<int[]> turns;

    static String canonical(int[] dims, String colors) {
        String best = turned(turns.get(0), dims, colors);
        for (int[] p : turns) {
            String s = turned(p, dims, colors);
            if (s.compareTo(best) < 0) {
                best = s;
            }
        }
        return best;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            text.append(line).append(' ');
        }
        StringTokenizer st = new StringTokenizer(text.toString());
        for (int a = 0; a < AXES; a++) {
            st.nextToken();
        }
        String box = st.nextToken();
        int n = Integer.parseInt(st.nextToken());
        int[][] dims = new int[n][AXES];
        String[] colors = new String[n];
        for (int i = 0; i < n; i++) {
            for (int a = 0; a < AXES; a++) {
                dims[i][a] = Integer.parseInt(st.nextToken());
            }
            colors[i] = st.nextToken();
        }
        turns = rotations();
        // the pieces on the edge along an axis carry the two box colours of
        // the faces before it on the other axes; their remaining extents are
        // the sections, the first one also coloured like the start face
        int[][] cuts = new int[AXES][];
        for (int axis = 0; axis < AXES; axis++) {
            int a = axis == 0 ? 1 : 0;
            int b = AXIS_SUM - axis - a;
            List<Integer> first = new ArrayList<>();
            List<Integer> middle = new ArrayList<>();
            List<Integer> last = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                int fa = colors[i].indexOf(box.charAt(2 * a));
                int fb = colors[i].indexOf(box.charAt(2 * b));
                if (fa < 0 || fb < 0) {
                    continue;
                }
                int extent = dims[i][AXIS_SUM - fa / 2 - fb / 2];
                if (colors[i].indexOf(box.charAt(2 * axis)) >= 0) {
                    first.add(extent);
                } else if (colors[i].indexOf(box.charAt(2 * axis + 1)) >= 0) {
                    last.add(extent);
                } else {
                    middle.add(extent);
                }
            }
            first.addAll(middle);
            first.addAll(last);
            cuts[axis] = first.stream().mapToInt(Integer::intValue).toArray();
        }
        // middle sections may come in any order: the pieces are the same
        Map<String, ArrayDeque<Integer>> groups = new HashMap<>();
        for (int i = 0; i < n; i++) {
            groups.computeIfAbsent(canonical(dims[i], colors[i]), k -> new ArrayDeque<>()).push(i);
        }
        String[] answer = new String[n];
        int[] place = new int[AXES];
        int[] corner = new int[AXES];
        for (place[0] = 0; place[0] < cuts[0].length; place[0]++) {
            corner[1] = 0;
            for (place[1] = 0; place[1] < cuts[1].length; place[1]++) {
                corner[2] = 0;
                for (place[2] = 0; place[2] < cuts[2].length; place[2]++) {
                    int[] want = new int[AXES];
                    StringBuilder paint = new StringBuilder();
                    for (int axis = 0; axis < AXES; axis++) {
                        want[axis] = cuts[axis][place[axis]];
                        boolean start = place[axis] == 0;
                        boolean end = place[axis] == cuts[axis].length - 1;
                        paint.append(start ? box.charAt(2 * axis) : INSIDE);
                        paint.append(end ? box.charAt(2 * axis + 1) : INSIDE);
                    }
                    String wanted = paint.toString();
                    int k = groups.get(canonical(want, wanted)).pop();
                    String target = turned(turns.get(0), want, wanted);
                    for (int[] p : turns) {
                        if (turned(p, dims[k], colors[k]).equals(target)) {
                            answer[k] = FACES.charAt(p[0]) + " " + FACES.charAt(p[2]) + " "
                                    + corner[0] + " " + corner[1] + " " + corner[2];
                            break;
                        }
                    }
                    corner[2] += want[2];
                }
                corner[1] += cuts[1][place[1]];
            }
            corner[0] += cuts[0][place[0]];
        }
        System.out.println(String.join("\n", answer));
    }
}
