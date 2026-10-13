use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let k = it.next().unwrap() as usize;
    let mut joy = vec![0i64; n + 1];
    for v in joy.iter_mut().skip(1) {
        *v = it.next().unwrap();
    }
    let mut adj: Vec<Vec<(usize, i64)>> = vec![Vec::new(); n + 1];
    for _ in 0..k {
        let a = it.next().unwrap() as usize;
        let b = it.next().unwrap() as usize;
        let c = it.next().unwrap();
        adj[a].push((b, c));
        adj[b].push((a, c));
    }
    // down[v]: the best route that starts at v and goes away from its parent,
    // nxt[v] the next city on it; the routes are in a forest, so each tree once
    let mut down = joy.clone();
    let mut nxt = vec![0usize; n + 1];
    let mut parent = vec![usize::MAX; n + 1];
    let (mut best, mut center, mut end_a, mut end_b) = (-1i64, 0usize, 0usize, 0usize);
    for root in 1..=n {
        if parent[root] != usize::MAX {
            continue;
        }
        parent[root] = 0;
        let mut order = Vec::new();
        let mut stack = vec![root];
        while let Some(v) = stack.pop() {
            order.push(v);
            for &(w, _) in &adj[v] {
                if parent[w] == usize::MAX {
                    parent[w] = v;
                    stack.push(w);
                }
            }
        }
        for &v in order.iter().rev() {
            // the best two routes through children: (value, child)
            let (mut first, mut second) = ((0i64, 0usize), (0i64, 0usize));
            for &(w, c) in &adj[v] {
                if w != parent[v] {
                    let option = (c + down[w], w);
                    if option > first {
                        second = first;
                        first = option;
                    } else if option > second {
                        second = option;
                    }
                }
            }
            down[v] = joy[v] + first.0;
            nxt[v] = first.1;
            if joy[v] + first.0 + second.0 > best {
                best = joy[v] + first.0 + second.0;
                center = v;
                end_a = first.1;
                end_b = second.1;
            }
        }
    }
    let mut route = Vec::new();
    let mut a = end_a;
    while a != 0 {
        route.push(a);
        a = nxt[a];
    }
    route.reverse();
    route.push(center);
    let mut b = end_b;
    while b != 0 {
        route.push(b);
        b = nxt[b];
    }
    let text: Vec<String> = route.iter().map(|v| v.to_string()).collect();
    println!("{}\n{}\n{}", best, route.len(), text.join(" "));
}
