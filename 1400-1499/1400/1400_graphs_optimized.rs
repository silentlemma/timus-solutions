use std::io::{self, Read};

/// Key presses from the start to every character, by breadth-first search.
fn distances(n: usize, m: usize, start: usize, dist: &mut [i64], queue: &mut Vec<usize>) -> i64 {
    dist.fill(-1);
    dist[start] = 0;
    queue.clear();
    queue.push(start);
    let (mut head, mut total) = (0, 0);
    while head < queue.len() {
        let v = queue[head];
        head += 1;
        // left and right run on through the rows; up and down stop at the edges
        let up = if v >= m { v - m } else { v };
        let down = if v + m < n { v + m } else { v };
        let left = if v == 0 { n - 1 } else { v - 1 };
        let right = if v + 1 == n { 0 } else { v + 1 };
        for u in [left, right, up, down] {
            if dist[u] < 0 {
                dist[u] = dist[v] + 1;
                total += dist[u];
                queue.push(u);
            }
        }
    }
    total
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let (n, m) = (tokens.next().unwrap(), tokens.next().unwrap());
    let mut work = vec![-1; n];
    let mut queue = Vec::with_capacity(n);
    let mut best = vec![0; n];
    let mut total = i64::MAX;
    // Reflection v -> n - 1 - v preserves every horizontal and vertical edge.
    for start in 0..(n + 1) / 2 {
        let sum = distances(n, m, start, &mut work, &mut queue);
        if sum < total {
            total = sum;
            best.copy_from_slice(&work);
        }
    }
    let mut out = format!("Mean = {:.2}\n", total as f64 / n as f64);
    for row in best.chunks(m) {
        for (index, value) in row.iter().enumerate() {
            if index != 0 {
                out.push(' ');
            }
            out.push_str(&value.to_string());
        }
        out.push('\n');
    }
    print!("{}", out);
}
