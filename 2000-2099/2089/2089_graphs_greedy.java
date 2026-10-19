import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;

public class Main {
  private static int[] winner;
  private static List<List<Integer>> incident;

  // a pair of v without a winner yet
  private static int open(int v) {
    for (int i : incident.get(v)) if (winner[i] == 0) return i;
    return -1;
  }

  public static void main(String[] args) throws IOException {
    StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
    in.nextToken();
    int n = (int) in.nval;
    in.nextToken();
    int k = (int) in.nval;
    int[] ex = new int[n];
    int[] ey = new int[n];
    incident = new ArrayList<>();
    for (int v = 0; v <= k; v++) incident.add(new ArrayList<>());
    for (int i = 0; i < n; i++) {
      in.nextToken();
      ex[i] = (int) in.nval;
      in.nextToken();
      ey[i] = (int) in.nval;
      incident.get(ex[i]).add(i);
      incident.get(ey[i]).add(i);
    }
    winner = new int[n];
    int[] degree = new int[k + 1];
    // every team may win at most one pair: a team with a single open pair takes
    // it, which never hurts, and the pair is closed for the other team
    ArrayDeque<Integer> leaves = new ArrayDeque<>();
    for (int v = 1; v <= k; v++) {
      degree[v] = incident.get(v).size();
      if (degree[v] == 1) leaves.push(v);
    }
    while (!leaves.isEmpty()) {
      int v = leaves.pop();
      if (degree[v] != 1) continue;
      int i = open(v);
      int u = ex[i] + ey[i] - v;
      winner[i] = v;
      degree[v] = 0;
      if (--degree[u] == 1) leaves.push(u);
    }
    // what is left must be disjoint cycles (every degree 2); each cycle is walked
    // and every pair is won by the team it leads to
    for (int v = 1; v <= k; v++) {
      if (degree[v] > 2) {
        System.out.println("No");
        return;
      }
    }
    for (int start = 1; start <= k; start++) {
      if (degree[start] != 2) continue;
      int v = start;
      do {
        int i = open(v);
        int u = ex[i] + ey[i] - v;
        winner[i] = u;
        degree[v]--;
        degree[u]--;
        v = u;
      } while (v != start);
    }
    StringBuilder out = new StringBuilder("Yes\n");
    for (int w : winner) out.append(w).append('\n');
    System.out.print(out);
  }
}
