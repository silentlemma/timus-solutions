use std::collections::VecDeque;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace().map(|w| w.parse::<usize>().unwrap());
    let n = words.next().unwrap();
    let grid: Vec<Vec<usize>> =
        (0..n).map(|_| (0..n).map(|_| words.next().unwrap()).collect()).collect();
    // renumbering contests and rooms together, room j must be free of every
    // later contest, so a contest that uses room b must come no later than
    // contest b: an order of the graph with an edge a -> b for each such use
    let mut waiting = vec![0; n];
    for a in 0..n {
        for b in 0..n {
            if a != b && grid[a][b] == 1 {
                waiting[b] += 1;
            }
        }
    }
    let mut ready: VecDeque<usize> = (0..n).filter(|&v| waiting[v] == 0).collect();
    let mut order = Vec::new();
    while let Some(a) = ready.pop_front() {
        order.push(a);
        for b in 0..n {
            if a != b && grid[a][b] == 1 {
                waiting[b] -= 1;
                if waiting[b] == 0 {
                    ready.push_back(b);
                }
            }
        }
    }
    if order.len() < n {
        println!("-1");
        return;
    }
    // each swap puts the next contest of the order in its place, so at most
    // n - 1 swaps are needed
    let mut where_: Vec<usize> = (0..n).collect();
    let mut here: Vec<usize> = (0..n).collect();
    let mut swaps = Vec::new();
    for i in 0..n {
        let j = where_[order[i]];
        if j == i {
            continue;
        }
        swaps.push((i + 1, j + 1));
        here.swap(i, j);
        where_[here[i]] = i;
        where_[here[j]] = j;
    }
    let mut out = format!("{}\n", swaps.len());
    for (i, j) in swaps {
        out.push_str(&format!("{} {}\n", i, j));
    }
    print!("{}", out);
}
