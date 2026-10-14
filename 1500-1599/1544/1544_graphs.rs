use std::collections::{BTreeSet, VecDeque};
use std::io::{self, Read};

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let mut it = s.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let m: usize = it.next().unwrap().parse().unwrap();
    let protocol: Vec<&str> = (0..n).map(|_| it.next().unwrap()).collect();
    let mut adj = vec![Vec::new(); n];
    for _ in 0..m {
        let a: usize = it.next().unwrap().parse().unwrap();
        let b: usize = it.next().unwrap().parse().unwrap();
        adj[a - 1].push(b - 1);
        adj[b - 1].push(a - 1);
    }
    // glue neighbours with the same protocol into regions
    let mut region = vec![usize::MAX; n];
    let mut regions = 0;
    for s in 0..n {
        if region[s] != usize::MAX {
            continue;
        }
        region[s] = regions;
        let mut stack = vec![s];
        while let Some(v) = stack.pop() {
            for &u in &adj[v] {
                if region[u] == usize::MAX && protocol[u] == protocol[v] {
                    region[u] = regions;
                    stack.push(u);
                }
            }
        }
        regions += 1;
    }
    let mut near = vec![BTreeSet::new(); regions];
    for v in 0..n {
        for &u in &adj[v] {
            if region[u] != region[v] {
                near[region[v]].insert(region[u]);
            }
        }
    }
    // switching a region merges it with all its neighbours, so switching the
    // same region again and again takes its eccentricity in steps, and no
    // plan does better than the radius of the region graph
    let (mut best, mut centre) = (regions, 0);
    for start in 0..regions {
        let mut dist = vec![usize::MAX; regions];
        dist[start] = 0;
        let mut queue = VecDeque::from(vec![start]);
        let mut far = 0;
        while let Some(r) = queue.pop_front() {
            far = far.max(dist[r]);
            for &x in &near[r] {
                if dist[x] == usize::MAX {
                    dist[x] = dist[r] + 1;
                    queue.push_back(x);
                }
            }
        }
        if far < best {
            best = far;
            centre = start;
        }
    }
    let computer = region.iter().position(|&r| r == centre).unwrap();
    let mut current = protocol[computer];
    let mut out = format!("{}\n", best);
    for _ in 0..best {
        current = if current == "J" { "E" } else { "J" };
        out += &format!("{} {}\n", computer + 1, current);
    }
    print!("{}", out);
}
