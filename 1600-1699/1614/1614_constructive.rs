use std::io::{self, Read, Write};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let n: usize = text.trim().parse().unwrap();
    let stops = 2 * n;
    let mut out = String::new();
    for k in 0..n {
        // k, k + 1, k - 1, k + 2, k - 2, ..., k + n around the circle of stops:
        // its neighbouring pairs are exactly those with sum 2k or 2k + 1
        let mut route = vec![k];
        for j in 1..=n {
            route.push((k + j) % stops);
            if j < n {
                route.push((k + stops - j) % stops);
            }
        }
        let line: Vec<String> = route.iter().map(|x| (x + 1).to_string()).collect();
        out.push_str(&line.join(" "));
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
