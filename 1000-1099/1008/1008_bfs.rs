use std::fmt::Write as _;
use std::io::{self, Read};

const MAX_COORD: usize = 10;
const SIDE: usize = MAX_COORD + 2;
const LETTERS: [char; 4] = ['R', 'T', 'L', 'B'];
const DX: [isize; 4] = [1, 0, -1, 0];
const DY: [isize; 4] = [0, 1, 0, -1];

fn step(x: usize, y: usize, d: usize) -> (usize, usize) {
    (x.wrapping_add_signed(DX[d]), y.wrapping_add_signed(DY[d]))
}

// Breadth-first search from the lowest of the leftmost pixels; each line names
// the neighbours seen for the first time.
fn describe(black: &mut [[bool; SIDE]; SIDE], count: usize, out: &mut String) {
    let start = (1..=MAX_COORD)
        .flat_map(|x| (1..=MAX_COORD).map(move |y| (x, y)))
        .find(|&(x, y)| black[x][y])
        .unwrap();
    let mut queue = vec![start];
    black[start.0][start.1] = false;
    writeln!(out, "{} {}", start.0, start.1).unwrap();
    for head in 0..count {
        let (x, y) = queue[head];
        for (d, &letter) in LETTERS.iter().enumerate() {
            let (nx, ny) = step(x, y, d);
            if black[nx][ny] {
                black[nx][ny] = false;
                queue.push((nx, ny));
                out.push(letter);
            }
        }
        out.push(if head + 1 < count { ',' } else { '.' });
        out.push('\n');
    }
}

// Replay the same search: the lines tell which pixels it adds.
fn list(start: (usize, usize), lines: &[&str], out: &mut String) {
    let mut queue = vec![start];
    for (head, line) in lines.iter().enumerate() {
        let (x, y) = queue[head];
        for c in line.chars() {
            if let Some(d) = LETTERS.iter().position(|&l| l == c) {
                queue.push(step(x, y, d));
            }
        }
    }
    queue.sort_unstable();
    writeln!(out, "{}", queue.len()).unwrap();
    for (x, y) in queue {
        writeln!(out, "{} {}", x, y).unwrap();
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let tokens: Vec<&str> = input.split_ascii_whitespace().collect();
    let num = |i: usize| -> usize { tokens[i].parse().unwrap() };
    let mut out = String::new();
    // only the description ends with a full stop
    if tokens[tokens.len() - 1].ends_with('.') {
        list((num(0), num(1)), &tokens[2..], &mut out);
    } else {
        let mut black = [[false; SIDE]; SIDE];
        let count = num(0);
        for i in 0..count {
            black[num(1 + 2 * i)][num(2 + 2 * i)] = true;
        }
        describe(&mut black, count, &mut out);
    }
    print!("{}", out);
}
