use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut values = input
        .split_ascii_whitespace()
        .map(|word| word.parse::<u32>().unwrap());
    let n = values.next().unwrap() as usize;
    let sentinel = n as u32;
    let mut boss = vec![sentinel; n];
    let mut child = vec![sentinel; n];
    let mut sibling = vec![sentinel; n];
    for vertex in 0..n {
        loop {
            let value = values.next().unwrap();
            if value == 0 {
                break;
            }
            let next = (value - 1) as usize;
            boss[next] = vertex as u32;
            sibling[next] = child[vertex];
            child[vertex] = next as u32;
        }
    }
    let source = (values.next().unwrap() - 1) as usize;
    let mut parent = vec![0_u32; n];
    let mut order = Vec::with_capacity(n);
    parent[source] = source as u32;
    order.push(source as u32);
    let mut cursor = 0;
    while cursor < order.len() {
        let vertex = order[cursor] as usize;
        cursor += 1;
        let other = boss[vertex];
        if other != sentinel && other != parent[vertex] {
            parent[other as usize] = vertex as u32;
            order.push(other);
        }
        let mut next = child[vertex];
        while next != sentinel {
            if next != parent[vertex] {
                parent[next as usize] = vertex as u32;
                order.push(next);
            }
            next = sibling[next as usize];
        }
    }
    let mut finish = vec![0_u32; n];
    let mut times = Vec::with_capacity(n);
    for &id in order.iter().rev() {
        let vertex = id as usize;
        times.clear();
        let other = boss[vertex];
        if other != sentinel && other != parent[vertex] {
            times.push(finish[other as usize]);
        }
        let mut next = child[vertex];
        while next != sentinel {
            if next != parent[vertex] {
                times.push(finish[next as usize]);
            }
            next = sibling[next as usize];
        }
        // Slow subtrees are called first; storage for the ordering is reused, not reallocated.
        times.sort_unstable_by(|left, right| right.cmp(left));
        finish[vertex] = times
            .iter()
            .enumerate()
            .map(|(i, &time)| time + i as u32 + 1)
            .max()
            .unwrap_or(0);
    }
    println!("{}", finish[source]);
}
