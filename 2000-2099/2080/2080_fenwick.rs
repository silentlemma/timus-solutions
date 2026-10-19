use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input.split_ascii_whitespace().map(|t| t.parse().unwrap()).collect();
    let (n, k) = (v[0], v[1]);
    let mut uses = vec![0; k + 1];
    uses[1..].copy_from_slice(&v[2..2 + k]);
    // the stack is kept in order of next use: after a card is used, the cards above
    // it are those used before its next use, the distinct cards in between
    let mut nxt = vec![0; k + 1];
    let mut seen = vec![k + 1; n + 1];
    for i in (1..=k).rev() {
        nxt[i] = seen[uses[i]];
        seen[uses[i]] = i;
    }
    // Fenwick tree over moments: a moment j counts once the query time i reaches
    // the previous use of its card, so the counted moments are first uses after i
    let mut tree = vec![0i32; k + 1];
    let add = |tree: &mut Vec<i32>, mut j: usize| {
        while j <= k {
            tree[j] += 1;
            j += j & j.wrapping_neg();
        }
    };
    let prefix = |tree: &Vec<i32>, mut j: usize| {
        let mut s = 0;
        while j > 0 {
            s += tree[j];
            j -= j & j.wrapping_neg();
        }
        s
    };
    for card in 1..=n {
        if seen[card] <= k {
            add(&mut tree, seen[card]);
        }
    }
    let mut order: Vec<usize> = (1..=n).collect();
    order.sort_by_key(|&card| seen[card]);
    let mut out = order.iter().map(|c| c.to_string()).collect::<Vec<_>>().join(" ");
    out.push('\n');
    for i in 1..=k {
        if nxt[i] <= k {
            add(&mut tree, nxt[i]);
        }
        out.push_str(&(prefix(&tree, nxt[i] - 1) - prefix(&tree, i)).to_string());
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
