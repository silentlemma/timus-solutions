use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i32>().unwrap());
    let n = it.next().unwrap() as usize;
    let mut rating = vec![0i32; n + 1];
    for v in 1..=n {
        rating[v] = it.next().unwrap();
    }
    let mut parent = vec![0usize; n + 1];
    // children as linked lists: first[v], then next[c] for the next sibling
    let mut first = vec![0usize; n + 1];
    let mut next = vec![0usize; n + 1];
    while let (Some(child), Some(boss)) = (it.next(), it.next()) {
        if child == 0 {
            break;
        }
        let (child, boss) = (child as usize, boss as usize);
        parent[child] = boss;
        next[child] = first[boss];
        first[boss] = child;
    }
    // a breadth-first order from the roots puts every boss before the subordinates
    let mut order: Vec<usize> = (1..=n).filter(|&v| parent[v] == 0).collect();
    let mut i = 0;
    while i < order.len() {
        let mut c = first[order[i]];
        while c != 0 {
            order.push(c);
            c = next[c];
        }
        i += 1;
    }
    // take[v], skip[v]: the best sum in the subtree of v with v invited or not
    let mut take = vec![0i32; n + 1];
    let mut skip = vec![0i32; n + 1];
    let mut total = 0;
    for &v in order.iter().rev() {
        take[v] += rating[v];
        let best = take[v].max(skip[v]);
        if parent[v] == 0 {
            total += best;
        } else {
            take[parent[v]] += skip[v];
            skip[parent[v]] += best;
        }
    }
    println!("{}", total);
}
