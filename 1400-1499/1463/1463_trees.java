import java.io.BufferedInputStream;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Main {
    private static int number(BufferedInputStream input) throws IOException {
        int c;
        do {
            c = input.read();
        } while (c >= 0 && c <= ' ');
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = input.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int count = number(input);
        int flights = number(input);
        char[] joy = new char[count + 1];
        char[] degree = new char[count + 1];
        char[] neighbor = new char[count + 1];
        char[] weight = new char[count + 1];
        char[] child = new char[count + 1];
        int[] arm = new int[count + 1];
        char[] leaves = new char[count];
        int best = 0;
        int center = 1;
        for (int v = 1; v <= count; v++) {
            joy[v] = (char)number(input);
            if (joy[v] > best) {
                best = joy[v];
                center = v;
            }
        }
        for (int i = 0; i < flights; i++) {
            int a = number(input);
            int b = number(input);
            int edgeWeight = number(input);
            degree[a]++;
            degree[b]++;
            neighbor[a] ^= b;
            neighbor[b] ^= a;
            weight[a] ^= edgeWeight;
            weight[b] ^= edgeWeight;
        }

        int end = 0;
        for (int v = 1; v <= count; v++) {
            if (degree[v] == 1) {
                leaves[end++] = (char)v;
            }
        }
        int left = 0;
        int right = 0;
        for (int head = 0; head < end; head++) {
            int v = leaves[head];
            if (degree[v] == 0) {
                continue;
            }
            // For a leaf, the XOR fields identify its one remaining edge.
            int parent = neighbor[v];
            degree[v] = 0;
            neighbor[parent] ^= v;
            weight[parent] ^= weight[v];
            if (--degree[parent] == 1) {
                leaves[end++] = (char)parent;
            }
            int branch = arm[v] + joy[v] + weight[v];
            int total = joy[parent] + arm[parent] + branch;
            if (total > best) {
                best = total;
                center = parent;
                left = v;
                right = child[parent];
            }
            if (branch > arm[parent]) {
                arm[parent] = branch;
                child[parent] = (char)v;
            }
        }

        int length = 0;
        for (int v = left; v != 0; v = child[v]) {
            leaves[length++] = (char)v;
        }
        int leftLength = length;
        leaves[length++] = (char)center;
        for (int v = right; v != 0; v = child[v]) {
            leaves[length++] = (char)v;
        }
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));
        output.write(Integer.toString(best));
        output.newLine();
        output.write(Integer.toString(length));
        output.newLine();
        for (int i = leftLength - 1; i >= 0; i--) {
            output.write(Integer.toString(leaves[i]));
            output.write(' ');
        }
        for (int i = leftLength; i < length; i++) {
            if (i > leftLength) {
                output.write(' ');
            }
            output.write(Integer.toString(leaves[i]));
        }
        output.newLine();
        output.flush();
    }
}
