use std::io::{self, Read};

fn reach(links: &[Vec<usize>]) -> Vec<bool> {
    let mut seen = vec![false; links.len()];
    seen[0] = true;
    let mut stack = vec![0];
    while let Some(v) = stack.pop() {
        for &u in &links[v] {
            if !seen[u] {
                seen[u] = true;
                stack.push(u);
            }
        }
    }
    seen
}

/// Bellman-Ford from every node at once: is some cycle negative?
fn negative_cycle(nodes: usize, edges: &[(usize, usize, i64)], sign: i64) -> bool {
    let mut dist = vec![0i64; nodes];
    for _ in 0..nodes {
        let mut changed = false;
        for &(from, to, weight) in edges {
            if dist[from] + sign * weight < dist[to] {
                dist[to] = dist[from] + sign * weight;
                changed = true;
            }
        }
        if !changed {
            return false;
        }
    }
    true
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let s = it.next().unwrap() as usize + 1;
    // rule[j][i][k]: cockroaches next month in a flat with j, i below, k above
    let mut rule = vec![vec![vec![0i64; s]; s]; s];
    for j in 0..s {
        for i in 0..s {
            for k in 0..s {
                rule[j][i][k] = it.next().unwrap();
            }
        }
    }
    // a finite floor plan read upwards is a closed walk through the pair (0, 0)
    // of the graph on pairs of neighbours; a step (a, b) -> (b, c) changes the
    // total by rule[b][a][c] - b, so the totals of a walk give the change
    let (mut out_of, mut into) = (vec![Vec::new(); s * s], vec![Vec::new(); s * s]);
    let mut all = Vec::new();
    for a in 0..s {
        for b in 0..s {
            for c in 0..s {
                all.push((a * s + b, b * s + c, rule[b][a][c] - b as i64));
                out_of[a * s + b].push(b * s + c);
                into[b * s + c].push(a * s + b);
            }
        }
    }
    let (forward, backward) = (reach(&out_of), reach(&into));
    let keep = |v: usize| forward[v] && backward[v];
    let edges: Vec<(usize, usize, i64)> = all
        .into_iter()
        .filter(|&(from, to, _)| keep(from) && keep(to))
        .collect();
    let fall = negative_cycle(s * s, &edges, 1);
    let rise = negative_cycle(s * s, &edges, -1);
    let answer = match (fall, rise) {
        (true, true) => "<>",
        (true, false) => "<",
        (false, true) => ">",
        (false, false) => "=",
    };
    println!("{}", answer);
}
