use std::io::{self, Read};

fn bfs(neighbors: &[Vec<usize>], source: usize) -> (Vec<i32>, Vec<usize>) {
    let mut distance = vec![-1; neighbors.len()];
    distance[source] = 0;
    let mut order = Vec::with_capacity(neighbors.len());
    order.push(source);
    let mut at = 0;
    while at < order.len() {
        let vertex = order[at];
        for &next in &neighbors[vertex] {
            if distance[next] < 0 {
                distance[next] = distance[vertex] + 1;
                order.push(next);
            }
        }
        at += 1;
    }
    (distance, order)
}

fn solve(size: usize, edges: &[(usize, usize)], start: usize, finish: usize, origin: usize) -> i32 {
    let mut neighbors = vec![Vec::new(); size];
    for &(a, b) in edges {
        neighbors[a].push(b);
        neighbors[b].push(a);
    }
    let (depth, order) = bfs(&neighbors, start);
    let clearance = bfs(&neighbors, origin).0;
    let mut best = vec![-1; size];
    best[start] = clearance[start];
    for vertex in order {
        for &next in &neighbors[vertex] {
            if depth[next] == depth[vertex] + 1 {
                best[next] = best[next].max(best[vertex].min(clearance[next]));
            }
        }
    }
    best[finish]
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let size: usize = match tokens.next() {
        Some(word) => word.parse().unwrap(),
        None => return,
    };
    let count: usize = tokens.next().unwrap().parse().unwrap();
    let edges: Vec<(usize, usize)> = (0..count)
        .map(|_| {
            let a: usize = tokens.next().unwrap().parse().unwrap();
            let b: usize = tokens.next().unwrap().parse().unwrap();
            (a - 1, b - 1)
        })
        .collect();
    let start: usize = tokens.next().unwrap().parse().unwrap();
    let finish: usize = tokens.next().unwrap().parse().unwrap();
    let origin: usize = tokens.next().unwrap().parse().unwrap();
    println!("{}", solve(size, &edges, start - 1, finish - 1, origin - 1));
}
