use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut children = vec![Vec::new(); n + 1];
    let mut value = vec![0i32; n + 1];
    let mut depth = vec![0usize; n + 1];
    for v in 2..=n {
        let kind = words.next().unwrap();
        let parent: usize = words.next().unwrap().parse().unwrap();
        children[parent].push(v);
        if kind == "L" {
            value[v] = words
                .next()
                .unwrap()
                .trim_start_matches('+')
                .parse()
                .unwrap();
        }
    }
    // breadth-first order from the root, then values from the leaves up:
    // the first player moves at even depths and takes the largest result
    let mut order = vec![1];
    let mut i = 0;
    while i < order.len() {
        let v = order[i];
        for &c in &children[v] {
            depth[c] = depth[v] + 1;
            order.push(c);
        }
        i += 1;
    }
    for &v in order.iter().rev() {
        if children[v].is_empty() {
            continue;
        }
        let results = children[v].iter().map(|&c| value[c]);
        value[v] = if depth[v] % 2 == 0 {
            results.max().unwrap()
        } else {
            results.min().unwrap()
        };
    }
    println!(
        "{}",
        match value[1] {
            1 => "+1",
            -1 => "-1",
            _ => "0",
        }
    );
}
