use std::io::{self, Read};

const SIDE: i32 = 3;
const CUBES: usize = 27;
const WAYS: usize = 6;
// the six directions; cells are numbered x * 9 + y * 3 + z
const STEPS: [(i32, i32, i32); WAYS] =
    [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)];
const AXIS: [usize; WAYS] = [0, 0, 1, 1, 2, 2];
const NAMES: &[u8] = b"RLFBUD";
const RIGHT: usize = 0; // the index of R
const UP: usize = 4; // the index of U

fn cell_of(x: i32, y: i32, z: i32) -> Option<usize> {
    let inside = |v: i32| (0..SIDE).contains(&v);
    if inside(x) && inside(y) && inside(z) {
        Some(((x * SIDE + y) * SIDE + z) as usize)
    } else {
        None
    }
}

struct Search {
    snake: Vec<u8>,
    near: Vec<[Option<usize>; WAYS]>,
    used: [bool; CUBES],
    answer: Vec<u8>,
}

impl Search {
    /// the free cells must stay one piece for the rest of the snake
    fn connected(&self, left: usize) -> bool {
        let start = match (0..CUBES).find(|&c| !self.used[c]) {
            None => return true,
            Some(c) => c,
        };
        let mut seen = [false; CUBES];
        let mut stack = vec![start];
        seen[start] = true;
        let mut count = 0;
        while let Some(at) = stack.pop() {
            count += 1;
            for next in self.near[at].iter().flatten() {
                if !self.used[*next] && !seen[*next] {
                    seen[*next] = true;
                    stack.push(*next);
                }
            }
        }
        count == left
    }

    /// place cube k + 1 after cube k, which sits at cell at
    fn fold(&mut self, k: usize, at: usize, way: usize) -> bool {
        if k == CUBES - 1 {
            return true;
        }
        for d in 0..WAYS {
            // a straight cube keeps the direction, a turning one changes axis
            let blocked = if self.snake[k] == b'F' { d != way } else { AXIS[d] == AXIS[way] };
            if blocked {
                continue;
            }
            let next = match self.near[at][d] {
                Some(c) if !self.used[c] => c,
                _ => continue,
            };
            self.used[next] = true;
            self.answer.push(NAMES[d]);
            if self.connected(CUBES - 2 - k) && self.fold(k + 1, next, d) {
                return true;
            }
            self.answer.pop();
            self.used[next] = false;
        }
        false
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut near = vec![[None; WAYS]; CUBES];
    for x in 0..SIDE {
        for y in 0..SIDE {
            for z in 0..SIDE {
                let here = cell_of(x, y, z).unwrap();
                for (d, &(a, b, c)) in STEPS.iter().enumerate() {
                    near[here][d] = cell_of(x + a, y + b, z + c);
                }
            }
        }
    }
    let snake = text.trim().as_bytes().to_vec();
    let mut search = Search { snake, near, used: [false; CUBES], answer: Vec::new() };
    // the cube colours 14 cells one way and 13 the other, and the snake
    // alternates, so it starts on the larger colour: a corner or the centre
    // of a face; up to symmetry that leaves three first moves
    let (corner, face) = (cell_of(0, 0, 0).unwrap(), cell_of(1, 1, 0).unwrap());
    for &(start, d) in &[(corner, RIGHT), (face, UP), (face, RIGHT)] {
        let next = search.near[start][d].unwrap();
        search.used = [false; CUBES];
        search.used[start] = true;
        search.used[next] = true;
        search.answer = vec![NAMES[d]];
        if search.connected(CUBES - 2) && search.fold(1, next, d) {
            println!("{}", String::from_utf8(search.answer).unwrap());
            return;
        }
    }
    println!("IMPOSSIBLE");
}
