use std::io::{self, Read};

const INF: u32 = 1_000_000_000;

struct Labyrinth {
    n: usize,
    k: usize,
    size: usize,
    road: Vec<Vec<u32>>,
}

impl Labyrinth {
    /// Distances between the doors of the outer house when walking through an
    /// inner house from door i to door j costs inside[i][j].
    fn outer_distances(&self, inside: &[Vec<u32>]) -> Vec<Vec<u32>> {
        let (n, size) = (self.n, self.size);
        let mut weight = self.road.clone();
        for h in 1..=self.k {
            for i in 0..n {
                for j in 0..n {
                    let w = &mut weight[h * n + i][h * n + j];
                    *w = (*w).min(inside[i][j]);
                }
            }
        }
        let mut result = Vec::with_capacity(n);
        for s in 0..n {
            // Dijkstra on the dense graph, O(size^2)
            let mut dist = vec![INF; size];
            let mut done = vec![false; size];
            dist[s] = 0;
            for _ in 0..size {
                let u = (0..size).filter(|&v| !done[v] && dist[v] < INF).min_by_key(|&v| dist[v]);
                let u = match u {
                    Some(u) => u,
                    None => break,
                };
                done[u] = true;
                for v in 0..size {
                    if weight[u][v] < INF && dist[u] + weight[u][v] < dist[v] {
                        dist[v] = dist[u] + weight[u][v];
                    }
                }
            }
            dist.truncate(n);
            result.push(dist);
        }
        result
    }
}

fn door(s: &str, n: usize) -> usize {
    let (h, d) = s.split_once('.').unwrap();
    h.parse::<usize>().unwrap() * n + d.parse::<usize>().unwrap()
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let mut next = || words.next().unwrap();
    let n: usize = next().parse().unwrap();
    let k: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();
    let size = (k + 1) * n; // door d of house h is h * n + d
    let mut road = vec![vec![INF; size]; size];
    for _ in 0..m {
        let u = door(next(), n);
        next();
        let v = door(next(), n);
        road[u][v] = 1;
        road[v][u] = 1;
    }
    let source: usize = next().parse().unwrap();
    let sink: usize = next().parse().unwrap();
    let lab = Labyrinth { n, k, size, road };
    // Round t allows paths nested t houses deep; the distances only shrink,
    // and once a round changes nothing, no later round will.
    let mut inside = lab.outer_distances(&vec![vec![INF; n]; n]);
    loop {
        let nxt = lab.outer_distances(&inside);
        if nxt == inside {
            break;
        }
        inside = nxt;
    }
    if inside[source][sink] >= INF {
        println!("no solution");
    } else {
        println!("{}", inside[source][sink]);
    }
}
