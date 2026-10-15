use std::io::{self, Read};

const MAX_CLIQUE: usize = 4; // four points pairwise 1 apart fit in space, five do not

fn find(parent: &mut [usize], mut v: usize) -> usize {
    while parent[v] != v {
        parent[v] = parent[parent[v]];
        v = parent[v];
    }
    v
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut nums = text.split_ascii_whitespace().map(|w| w.parse::<usize>().unwrap());
    let (n, m) = (nums.next().unwrap(), nums.next().unwrap());
    let mut parent: Vec<usize> = (0..n).collect();
    let mut degree = vec![0; n];
    let mut ends = Vec::with_capacity(m);
    for _ in 0..m {
        let u = nums.next().unwrap() - 1;
        let v = nums.next().unwrap() - 1;
        degree[u] += 1;
        degree[v] += 1;
        ends.push(u);
        let (ru, rv) = (find(&mut parent, u), find(&mut parent, v));
        parent[ru] = rv;
    }
    let (mut size, mut edges, mut widest) = (vec![0; n], vec![0; n], vec![0; n]);
    for v in 0..n {
        let root = find(&mut parent, v);
        size[root] += 1;
        widest[root] = widest[root].max(degree[v]);
    }
    for &u in &ends {
        let root = find(&mut parent, u);
        edges[root] += 1;
    }
    // every component must be a path or a clique of at most four vertices
    for root in 0..n {
        let k: usize = size[root];
        if k == 0 {
            continue;
        }
        let path = edges[root] == k - 1 && widest[root] <= 2;
        let clique = edges[root] == k * (k - 1) / 2 && k <= MAX_CLIQUE;
        if !path && !clique {
            println!("Unlucky Petr");
            return;
        }
    }
    println!("Luck is possible");
}
