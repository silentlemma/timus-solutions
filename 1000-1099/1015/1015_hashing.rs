use std::collections::HashMap;
use std::fmt::Write as _;
use std::io::{self, Read};

const FACES: usize = 6;
const BASE: usize = 7;
// quarter turns around the vertical and the left-right axes: the new face at
// position i is the old face at position TURNS[t][i]
const TURNS: [[usize; FACES]; 2] = [[3, 5, 2, 1, 4, 0], [0, 1, 5, 2, 3, 4]];

fn rotations() -> Vec<[usize; FACES]> {
    let identity: [usize; FACES] = std::array::from_fn(|i| i);
    let mut all = vec![identity];
    let mut k = 0;
    while k < all.len() {
        for turn in &TURNS {
            let r: [usize; FACES] = std::array::from_fn(|i| all[k][turn[i]]);
            if !all.contains(&r) {
                all.push(r);
            }
        }
        k += 1;
    }
    all
}

fn main() {
    let rots = rotations();
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    // the key of a die is the smallest code among its 24 rotations
    let mut group: HashMap<usize, usize> = HashMap::new();
    let mut members: Vec<Vec<usize>> = Vec::new();
    for d in 1..=n {
        let face: Vec<usize> = (0..FACES).map(|_| it.next().unwrap()).collect();
        let key = rots
            .iter()
            .map(|r| r.iter().fold(0, |code, &i| code * BASE + face[i]))
            .min()
            .unwrap();
        match group.get(&key) {
            Some(&g) => members[g].push(d),
            None => {
                group.insert(key, members.len());
                members.push(vec![d]);
            }
        }
    }
    let mut out = String::new();
    writeln!(out, "{}", members.len()).unwrap();
    for m in &members {
        let line: Vec<String> = m.iter().map(|d| d.to_string()).collect();
        writeln!(out, "{}", line.join(" ")).unwrap();
    }
    print!("{}", out);
}
