use std::io::{self, Read, Write};

fn solve(cost: &[Vec<u64>], plants: &[usize]) -> u64 {
    let n = cost.len();
    let mut best = vec![u64::MAX; n];
    let mut used = vec![false; n];
    for &v in plants {
        best[v] = 0;
    }
    let mut answer = 0;
    for _ in 0..n {
        let vertex = (0..n)
            .filter(|&v| !used[v])
            .min_by_key(|&v| best[v])
            .unwrap();
        answer += best[vertex];
        used[vertex] = true;
        for v in 0..n {
            if !used[v] && cost[vertex][v] < best[v] {
                best[v] = cost[vertex][v];
            }
        }
    }
    answer
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut input = text.split_whitespace();
    let n: usize = match input.next() {
        Some(s) => s.parse().unwrap(),
        None => return,
    };
    let k: usize = input.next().unwrap().parse().unwrap();
    let plants: Vec<usize> = (0..k)
        .map(|_| input.next().unwrap().parse::<usize>().unwrap() - 1)
        .collect();
    let cost: Vec<Vec<u64>> = (0..n)
        .map(|_| {
            (0..n)
                .map(|_| input.next().unwrap().parse().unwrap())
                .collect()
        })
        .collect();
    let mut out = io::BufWriter::new(io::stdout().lock());
    writeln!(out, "{}", solve(&cost, &plants)).unwrap();
}
