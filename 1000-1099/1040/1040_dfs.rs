use std::io::{self, Read};

struct Search {
    adj: Vec<Vec<(usize, usize)>>,
    number: Vec<usize>,
    visited: Vec<bool>,
    counter: usize,
}

impl Search {
    // numbers the flights in the order the search meets them; the first flight
    // met at a new airport right after its entry flight k gets k + 1
    fn dfs(&mut self, v: usize) {
        self.visited[v] = true;
        for i in 0..self.adj[v].len() {
            let (w, e) = self.adj[v][i];
            if self.number[e] == 0 {
                self.counter += 1;
                self.number[e] = self.counter;
                if !self.visited[w] {
                    self.dfs(w);
                }
            }
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let (n, m) = (it.next().unwrap(), it.next().unwrap());
    let mut s = Search {
        adj: vec![Vec::new(); n + 1],
        number: vec![0; m],
        visited: vec![false; n + 1],
        counter: 0,
    };
    for e in 0..m {
        let (a, b) = (it.next().unwrap(), it.next().unwrap());
        s.adj[a].push((b, e));
        s.adj[b].push((a, e));
    }
    s.dfs(1);
    let numbers: Vec<String> = s.number.iter().map(|k| k.to_string()).collect();
    println!("YES\n{}", numbers.join(" "));
}
