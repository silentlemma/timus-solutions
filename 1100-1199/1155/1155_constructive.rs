use std::collections::HashMap;
use std::io::{self, Read};

// the cube: A B C D around the bottom face, E F G H above them
const EDGES: [&str; 12] = [
    "AB", "BC", "CD", "DA", "EF", "FG", "GH", "HE", "AE", "BF", "CG", "DH",
];
// the cube is bipartite; every operation changes one chamber of each side
const EVEN: &str = "ACFH";
const CELLS: &str = "ABCDEFGH";

fn even(c: char) -> bool {
    EVEN.contains(c)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut count: HashMap<char, u32> = CELLS
        .chars()
        .zip(input.split_ascii_whitespace().map(|t| t.parse().unwrap()))
        .collect();
    let side = |even_side: bool| -> u32 {
        CELLS
            .chars()
            .filter(|&c| even(c) == even_side)
            .map(|c| count[&c])
            .sum()
    };
    if side(true) != side(false) {
        println!("IMPOSSIBLE");
        return;
    }
    let mut near: HashMap<char, Vec<char>> = HashMap::new();
    for e in EDGES {
        let (a, b) = (e.as_bytes()[0] as char, e.as_bytes()[1] as char);
        near.entry(a).or_default().push(b);
        near.entry(b).or_default().push(a);
    }
    let mut out = String::new();
    let mut emit = |a: char, b: char, sign: char| {
        out.push(a);
        out.push(b);
        out.push(sign);
        out.push('\n');
    };
    // annihilate along every edge as long as both ends hold duons; afterwards
    // every edge has an empty end
    for e in EDGES {
        let (a, b) = (e.as_bytes()[0] as char, e.as_bytes()[1] as char);
        let k = count[&a].min(count[&b]);
        for _ in 0..k {
            emit(a, b, '-');
        }
        *count.get_mut(&a).unwrap() -= k;
        *count.get_mut(&b).unwrap() -= k;
    }
    // what is left can only sit at two opposite corners u and w, in equal
    // numbers; a pair made on the middle edge of a path u x y w removes both
    for u in EVEN.chars() {
        let left = count[&u];
        if left == 0 {
            continue;
        }
        let w = CELLS.chars().find(|&c| count[&c] > 0 && !even(c)).unwrap();
        let x = near[&u][0];
        let y = *near[&x].iter().find(|c| near[&w].contains(c)).unwrap();
        for _ in 0..left {
            emit(x, y, '+');
            emit(u, x, '-');
            emit(y, w, '-');
        }
        *count.get_mut(&w).unwrap() -= left;
        *count.get_mut(&u).unwrap() = 0;
    }
    print!("{}", out);
}
