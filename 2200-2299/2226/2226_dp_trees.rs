use std::fmt::Write as FmtWrite;
use std::io::{self, Read, Write};

const MAX_LENGTH: usize = 1_000_000_000;
const INF: usize = MAX_LENGTH + 1;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut data = input
        .split_whitespace()
        .map(|s| s.parse::<usize>().unwrap());
    let n = data.next().unwrap();
    let mut graph = vec![Vec::new(); n + 1];
    let mut first = vec![0; n + 1];
    let mut second = vec![0; n + 1];
    let mut shortest = vec![INF; n + 1];
    let mut next_shortest = vec![INF; n + 1];
    for _ in 1..n {
        let u = data.next().unwrap();
        let v = data.next().unwrap();
        let length = data.next().unwrap();
        for (a, b) in [(u, v), (v, u)] {
            graph[a].push(b);
            if length < shortest[a] {
                next_shortest[a] = shortest[a];
                second[a] = first[a];
                shortest[a] = length;
                first[a] = b;
            } else if length < next_shortest[a] {
                next_shortest[a] = length;
                second[a] = b;
            }
        }
    }
    let mut parent = vec![0; n + 1];
    let mut order = Vec::with_capacity(n);
    order.push(1);
    for i in 0..n {
        let v = order[i];
        for &u in &graph[v] {
            if u != parent[v] {
                parent[u] = v;
                order.push(u);
            }
        }
    }

    // down[v] is the endpoint after arriving at v from its parent.
    let mut down = vec![0; n + 1];
    let mut up = vec![0; n + 1];
    for &v in order.iter().rev() {
        let u = if first[v] == parent[v] {
            second[v]
        } else {
            first[v]
        };
        down[v] = if u == 0 { v } else { down[u] };
    }
    // up[v] is the endpoint after leaving v for its parent.
    for &v in order.iter().skip(1) {
        let p = parent[v];
        let u = if first[p] == v { second[p] } else { first[p] };
        up[v] = if u == 0 {
            p
        } else if u == parent[p] {
            up[p]
        } else {
            down[u]
        };
    }
    let mut output = String::new();
    for v in 1..=n {
        if v != 1 {
            output.push(' ');
        }
        let answer = if first[v] == parent[v] {
            up[v]
        } else {
            down[v]
        };
        write!(output, "{}", answer).unwrap();
    }
    output.push('\n');
    io::BufWriter::new(io::stdout())
        .write_all(output.as_bytes())
        .unwrap();
}
