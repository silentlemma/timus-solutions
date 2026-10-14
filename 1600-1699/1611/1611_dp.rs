use std::io::{self, Read};

const STEP: usize = 10; // every tenth person is fined
const INF: usize = 1 << 30;

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let mut it = s.split_ascii_whitespace();
    let n: usize = match it.next() {
        Some(w) => w.parse().unwrap(),
        None => return,
    };
    let k: usize = it.next().unwrap().parse().unwrap();
    let good = it.next().unwrap_or("").as_bytes();
    // cost[i][j] holds the least fines once i conductors and j friends stand
    // in line, and the next person then stands at place i + j + 1
    let mut cost = vec![vec![INF; k + 1]; n + 1];
    cost[0][0] = 0;
    for i in 0..=n {
        for j in 0..=k {
            let here = cost[i][j];
            if here == INF {
                continue;
            }
            let fined = (i + j + 1) % STEP == 0;
            if j < k {
                cost[i][j + 1] = cost[i][j + 1].min(here + fined as usize); // a friend steps in
            }
            if i < n {
                let add = (fined && good[i] == b'1') as usize;
                cost[i + 1][j] = cost[i + 1][j].min(here + add);
            }
        }
    }
    let mut j = (0..=k).min_by_key(|&t| (cost[n][t], t)).unwrap();
    let best = cost[n][j];
    // walk back: a friend was added wherever the cost came from the left
    let mut places = Vec::new();
    let mut i = n;
    while i > 0 || j > 0 {
        let fined = (i + j) % STEP == 0;
        if i > 0 && cost[i - 1][j] + (fined && good[i - 1] == b'1') as usize == cost[i][j] {
            i -= 1;
        } else {
            places.push(i + j);
            j -= 1;
        }
    }
    places.reverse();
    let mut line = vec![places.len().to_string()];
    line.extend(places.iter().map(|p| p.to_string()));
    println!("{}\n{}", best, line.join(" "));
}
