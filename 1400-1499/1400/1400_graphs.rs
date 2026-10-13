use std::io::{self, Read};

/// Key presses from the start to every character, by breadth-first search.
fn distances(n: usize, m: usize, start: usize) -> Vec<i64> {
    let mut dist = vec![-1i64; n];
    dist[start] = 0;
    let mut queue = vec![start];
    let mut h = 0;
    while h < queue.len() {
        let v = queue[h];
        h += 1;
        // left and right run on through the rows; up and down stop at the edges
        let up = if v >= m { v - m } else { v };
        let down = if v + m < n { v + m } else { v };
        for u in [(v + n - 1) % n, (v + 1) % n, up, down] {
            if dist[u] < 0 {
                dist[u] = dist[v] + 1;
                queue.push(u);
            }
        }
    }
    dist
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, m) = (v[0], v[1]);
    let best = (0..n)
        .map(|s| distances(n, m, s))
        .min_by_key(|d| d.iter().sum::<i64>())
        .unwrap();
    let total: i64 = best.iter().sum();
    let mut out = format!("Mean = {:.2}\n", total as f64 / n as f64);
    for row in best.chunks(m) {
        let parts: Vec<String> = row.iter().map(|x| x.to_string()).collect();
        out.push_str(&parts.join(" "));
        out.push('\n');
    }
    print!("{}", out);
}
