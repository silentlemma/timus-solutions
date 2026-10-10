use std::collections::{HashMap, HashSet};
use std::io::{self, Read};

// face positions in the input: front, right, left, back, top, bottom; a
// quarter turn about the vertical axis (front goes right) and one about the
// left-right axis (top goes front), as new position from old position
const FACES: usize = 6;
const FRONT: usize = 0;
const RIGHT: usize = 1;
const LEFT: usize = 2;
const BACK: usize = 3;
const SIDES: usize = 4;
const SPIN: [usize; FACES] = [2, 0, 3, 1, 4, 5];
const TIP: [usize; FACES] = [4, 1, 2, 5, 3, 0];

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input.split_ascii_whitespace();
    let n: usize = tok.next().unwrap().parse().unwrap();
    // all 24 rotations as position -> original face
    let start: [usize; FACES] = std::array::from_fn(|p| p);
    let mut seen = HashSet::new();
    seen.insert(start);
    let mut stack = vec![start];
    let mut rotations = Vec::new();
    while let Some(cur) = stack.pop() {
        rotations.push(cur);
        for turn in [SPIN, TIP] {
            let mut next = [0; FACES];
            for p in 0..FACES {
                next[p] = cur[turn[p]];
            }
            if seen.insert(next) {
                stack.push(next);
            }
        }
    }
    // each cube can show a given ring of side colours at most once, since its
    // faces all differ; the tallest tower is the most common ring
    let mut rings: HashMap<[u8; SIDES], usize> = HashMap::new();
    let mut best = 0;
    for _ in 0..n {
        let cube = tok.next().unwrap().as_bytes();
        for rot in &rotations {
            let ring = [
                cube[rot[FRONT]],
                cube[rot[RIGHT]],
                cube[rot[BACK]],
                cube[rot[LEFT]],
            ];
            let count = rings.entry(ring).or_insert(0);
            *count += 1;
            best = best.max(*count);
        }
    }
    println!("{}", best);
}
