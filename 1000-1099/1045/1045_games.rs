use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let (n, k) = (it.next().unwrap(), it.next().unwrap());
    let mut adj = vec![Vec::new(); n + 1];
    for _ in 1..n {
        let (a, b) = (it.next().unwrap(), it.next().unwrap());
        adj[a].push(b);
        adj[b].push(a);
    }
    // the destroyed airports are exactly the ones on the way back to k, so a
    // move always goes down the tree rooted at k; a breadth-first order lists
    // parents before children
    let mut parent = vec![usize::MAX; n + 1];
    let mut order = vec![k];
    let mut i = 0;
    while i < order.len() {
        let v = order[i];
        for j in 0..adj[v].len() {
            let w = adj[v][j];
            if w != parent[v] {
                parent[w] = v;
                order.push(w);
            }
        }
        i += 1;
    }
    // win[v]: the player to move at v wins, that is, some child is a loss
    let mut win = vec![false; n + 1];
    for &v in order[1..].iter().rev() {
        if !win[v] {
            win[parent[v]] = true;
        }
    }
    match adj[k].iter().filter(|&&w| !win[w]).min() {
        Some(best) => println!("First player wins flying to airport {}", best),
        None => println!("First player loses"),
    }
}
