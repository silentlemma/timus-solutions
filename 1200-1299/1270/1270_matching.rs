use std::collections::HashSet;
use std::io::{self, Read};

const FACES: usize = 6;
const COORDS: usize = 3; // the cell's place does not matter

// faces in the input order: front, up, right, down, left, back; a turn p
// gives face f the colour of face p[f]; SPIN turns the cube about the
// vertical axis, TIP about the left-right one
const SPIN: [usize; FACES] = [2, 1, 5, 3, 0, 4];
const TIP: [usize; FACES] = [1, 5, 2, 0, 4, 3];

// all 24 rotations of a cube, from two quarter turns
fn rotations() -> Vec<[usize; FACES]> {
    let start: [usize; FACES] = std::array::from_fn(|f| f);
    let mut found: HashSet<[usize; FACES]> = [start].into_iter().collect();
    let mut queue = vec![start];
    let mut k = 0;
    while k < queue.len() {
        for g in [SPIN, TIP] {
            let p = queue[k];
            let q: [usize; FACES] = std::array::from_fn(|f| p[g[f]]);
            if found.insert(q) {
                queue.push(q);
            }
        }
        k += 1;
    }
    queue
}

fn augment(j: usize, fits: &[Vec<usize>], owner: &mut [Option<usize>], seen: &mut [bool]) -> bool {
    for &i in &fits[j] {
        if !seen[i] {
            seen[i] = true;
            let free = match owner[i] {
                None => true,
                Some(k) => augment(k, fits, owner, seen),
            };
            if free {
                owner[i] = Some(j);
                return true;
            }
        }
    }
    false
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    let cubes: Vec<Vec<usize>> = (0..n).map(|_| it.by_ref().take(FACES).collect()).collect();
    let m = it.next().unwrap();
    let turns = rotations();
    // fits[j]: the cubes that can stand in cell j, turned somehow
    let fits: Vec<Vec<usize>> = (0..m)
        .map(|_| {
            let need: Vec<usize> = it.by_ref().take(COORDS + FACES).skip(COORDS).collect();
            (0..n)
                .filter(|&i| {
                    turns
                        .iter()
                        .any(|p| (0..FACES).all(|f| need[f] == 0 || need[f] == cubes[i][p[f]]))
                })
                .collect()
        })
        .collect();
    // Kuhn's augmenting paths from every cell
    let mut owner = vec![None; n];
    for j in 0..m {
        if !augment(j, &fits, &mut owner, &mut vec![false; n]) {
            println!("0");
            return;
        }
    }
    let mut cube_of = vec![0; m];
    for (i, o) in owner.iter().enumerate() {
        if let Some(j) = o {
            cube_of[*j] = i + 1;
        }
    }
    let lines: Vec<String> = cube_of.iter().map(|c| c.to_string()).collect();
    println!("{}", lines.join("\n"));
}
