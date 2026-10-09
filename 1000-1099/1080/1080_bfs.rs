use std::collections::VecDeque;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    let mut adj = vec![Vec::new(); n + 1];
    for i in 1..=n {
        loop {
            let v = it.next().unwrap();
            if v == 0 {
                break;
            }
            adj[i].push(v);
            adj[v].push(i);
        }
    }
    // the map is connected, so the colour of the first country decides all
    let mut color = vec![-1i32; n + 1];
    color[1] = 0;
    let mut queue = VecDeque::from([1usize]);
    while let Some(u) = queue.pop_front() {
        for &v in &adj[u] {
            if color[v] < 0 {
                color[v] = 1 - color[u];
                queue.push_back(v);
            } else if color[v] == color[u] {
                println!("-1");
                return;
            }
        }
    }
    let out: String = color[1..].iter().map(|c| c.to_string()).collect();
    println!("{}", out);
}
