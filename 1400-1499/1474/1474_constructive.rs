use std::io::{self, Read, Write};

const EMPTY: u8 = 0;
const WHITE: u8 = 1;
const BLACK: u8 = 2;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: i64 = input.trim().parse().unwrap();
    let mut hummocks: Vec<u8> = (0..=2 * n)
        .map(|i| if i < n { WHITE } else { BLACK })
        .collect();
    hummocks[n as usize] = EMPTY;
    let mut hole = n;
    let mut moves: Vec<i64> = Vec::new();
    // runs of 1, 2, ..., n, n, n, ..., 1 moves, the colours taking turns,
    // and in a run a frog jumps into the hole when it can and slides otherwise
    let runs: Vec<i64> = (1..=n)
        .chain(std::iter::once(n))
        .chain((1..=n).rev())
        .collect();
    let mut colour = BLACK;
    for run in runs {
        // where the frogs come from
        let (step, other) = if colour == BLACK {
            (1, WHITE)
        } else {
            (-1, BLACK)
        };
        for _ in 0..run {
            let (far, near) = (hole + 2 * step, hole + step);
            let jump = (0..=2 * n).contains(&far)
                && hummocks[far as usize] == colour
                && hummocks[near as usize] == other;
            let frog = if jump { far } else { near };
            hummocks[hole as usize] = colour;
            hummocks[frog as usize] = EMPTY;
            hole = frog;
            moves.push(frog);
        }
        colour = other;
    }
    let text: Vec<String> = moves.iter().map(|m| m.to_string()).collect();
    let out = format!("{}\n{}\n", moves.len(), text.join(" "));
    io::stdout().write_all(out.as_bytes()).unwrap();
}
