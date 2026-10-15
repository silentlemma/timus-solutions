import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int DIM = 3;
    static final int OPPOSITE = 3;
    // each face and the vertex opposite it
    static final int[][] FACES = {{0, 1, 2, 3}, {0, 1, 3, 2}, {0, 2, 3, 1}, {1, 2, 3, 0}};
    static StreamTokenizer in;

    static long next() throws IOException {
        in.nextToken();
        return (long) in.nval;
    }

    public static void main(String[] args) throws IOException {
        in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        long[][] v = new long[FACES.length][DIM];
        for (long[] p : v) {
            for (int t = 0; t < DIM; t++) {
                p[t] = next();
            }
        }
        int n = (int) next();
        long[][] normals = new long[FACES.length][];
        for (int f = 0; f < FACES.length; f++) {
            int[] face = FACES[f];
            long[] u = new long[DIM];
            long[] w = new long[DIM];
            long[] d = new long[DIM];
            for (int t = 0; t < DIM; t++) {
                u[t] = v[face[1]][t] - v[face[0]][t];
                w[t] = v[face[2]][t] - v[face[0]][t];
                d[t] = v[face[OPPOSITE]][t] - v[face[0]][t];
            }
            long[] c = {
                u[1] * w[2] - u[2] * w[1], u[2] * w[0] - u[0] * w[2], u[0] * w[1] - u[1] * w[0]
            };
            // point the cross product, twice the face area long, away from the body
            if (c[0] * d[0] + c[1] * d[1] + c[2] * d[2] > 0) {
                c = new long[] {-c[0], -c[1], -c[2]};
            }
            normals[f] = c;
        }
        // a lit face gives area * intensity * cosine = (cross . star) / 2, and the
        // doubled total is a plain integer sum; the body is convex, so no shadows
        long total = 0;
        for (int i = 0; i < n; i++) {
            long[] s = {next(), next(), next()};
            for (long[] c : normals) {
                total += Math.max(0, c[0] * s[0] + c[1] * s[1] + c[2] * s[2]);
            }
        }
        System.out.println(total + ".00000");
    }
}
