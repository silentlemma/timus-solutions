use std::io::{self, Read};

const INF: i64 = 1 << 30;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<i64>().unwrap());
    let (n, m) = (it.next().unwrap() as usize, it.next().unwrap() as usize);
    let mut w = vec![vec![INF; n]; n];
    let mut edges = Vec::with_capacity(m);
    for _ in 0..m {
        let a = it.next().unwrap() as usize - 1;
        let b = it.next().unwrap() as usize - 1;
        let c = it.next().unwrap();
        w[a][b] = c;
        w[b][a] = c;
        edges.push((a, b, c));
    }
    // Prim on the matrix; heaviest[u][v] is the heaviest tree edge between u and v
    let mut heaviest = vec![vec![0i64; n]; n];
    let mut in_tree = vec![vec![false; n]; n];
    let mut dist = w[0].clone();
    let mut parent = vec![0usize; n];
    let mut done = vec![false; n];
    done[0] = true;
    let mut order = vec![0usize];
    let mut total = 0i64;
    for _ in 1..n {
        let v = (0..n)
            .filter(|&u| !done[u])
            .min_by_key(|&u| dist[u])
            .unwrap();
        let (p, c) = (parent[v], dist[v]);
        total += c;
        in_tree[p][v] = true;
        in_tree[v][p] = true;
        for &u in &order {
            let h = heaviest[p][u].max(c);
            heaviest[u][v] = h;
            heaviest[v][u] = h;
        }
        done[v] = true;
        order.push(v);
        for u in 0..n {
            if !done[u] && w[v][u] < dist[u] {
                dist[u] = w[v][u];
                parent[u] = v;
            }
        }
    }
    // the next tree swaps one outside edge for the heaviest edge on its tree path
    let swap = edges
        .iter()
        .filter(|&&(a, b, _)| !in_tree[a][b])
        .map(|&(a, b, c)| c - heaviest[a][b])
        .min();
    println!("Cost: {}", total);
    println!("Cost: {}", swap.map_or(-1, |s| total + s));
}
