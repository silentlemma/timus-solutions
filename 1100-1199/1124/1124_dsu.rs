use std::collections::HashSet;
use std::io::{self, Read};

fn find(parent: &mut [usize], mut x: usize) -> usize {
    while parent[x] != x {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    x
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let (m, n) = (tok.next().unwrap(), tok.next().unwrap());
    let mut parent: Vec<usize> = (0..m).collect();
    // a piece of colour c in box b is an edge b -> c; every box has n pieces
    // and should get n back, so each connected group of boxes is an Euler
    // circuit, walked one carried piece per move
    let mut moves = 0;
    let mut touched = vec![false; m];
    for bx in 0..m {
        for _ in 0..n {
            let colour = tok.next().unwrap() - 1;
            if colour != bx {
                moves += 1;
                touched[bx] = true;
                touched[colour] = true;
                let (a, b) = (find(&mut parent, bx), find(&mut parent, colour));
                parent[a] = b;
            }
        }
    }
    let groups: HashSet<usize> = (0..m)
        .filter(|&x| touched[x])
        .map(|x| find(&mut parent, x))
        .collect();
    // one empty move of the hand between groups
    println!(
        "{}",
        if moves == 0 {
            0
        } else {
            moves + groups.len() - 1
        }
    );
}
