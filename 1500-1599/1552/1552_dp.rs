use std::io::{self, Read};

const CELLS: usize = 4; // the program needs at most four cells
const VALUES: usize = 27; // a cell holds 0 or a letter, kept as 0 or 1 to 26
const OTHERS: usize = VALUES * VALUES * VALUES; // states of the cells away from the pointer
const STATES: usize = CELLS * OTHERS;
const LETTER_BASE: i32 = b'a' as i32 - 1;
const UNREACHABLE: i32 = 1 << 30;

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let s = s.trim().as_bytes();
    // a state, after a letter is printed, is the pointer's cell (holding that
    // letter) and the values of the other three cells, left to right; the
    // used cells form a block of four that holds the start cell somewhere
    let mut cost = vec![UNREACHABLE; STATES];
    for start in 0..CELLS {
        cost[start * OTHERS] = 0;
    }
    let mut came_from: Vec<Vec<u32>> = Vec::new();
    let mut previous = 0usize; // the value under the pointer: 0 before the first letter
    for &c in s {
        let letter = (c as i32 - LETTER_BASE) as usize;
        let mut next = vec![UNREACHABLE; STATES];
        let mut back = vec![0u32; STATES];
        for (state, &here) in cost.iter().enumerate() {
            if here == UNREACHABLE {
                continue;
            }
            let (p, rest) = (state / OTHERS, state % OTHERS);
            let mut digits = [
                rest / (VALUES * VALUES),
                rest / VALUES % VALUES,
                rest % VALUES,
            ]
            .into_iter();
            let w: Vec<usize> = (0..CELLS)
                .map(|cell| {
                    if cell == p {
                        previous
                    } else {
                        digits.next().unwrap()
                    }
                })
                .collect();
            for q in 0..CELLS {
                let change = if w[q] != 0 {
                    letter as i32 - w[q] as i32
                } else {
                    letter as i32 + LETTER_BASE
                };
                let total = here + (p as i32 - q as i32).abs() + change.abs() + 1;
                let code = (0..CELLS)
                    .filter(|&cell| cell != q)
                    .fold(0, |code, cell| code * VALUES + w[cell])
                    + q * OTHERS;
                if total < next[code] {
                    next[code] = total;
                    back[code] = state as u32;
                }
            }
        }
        came_from.push(back);
        cost = next;
        previous = letter;
    }
    // walk back to recover the cells used, then write the program
    let mut state = (0..STATES).min_by_key(|&st| cost[st]).unwrap();
    let mut used = vec![0usize; s.len() + 1];
    for i in (1..=s.len()).rev() {
        used[i] = state / OTHERS;
        state = came_from[i - 1][state] as usize;
    }
    used[0] = state / OTHERS;
    let mut held = [0i32; CELLS];
    let mut out = String::new();
    for i in 0..s.len() {
        let (p, q, letter) = (used[i], used[i + 1], s[i] as i32 - LETTER_BASE);
        out +=
            &(if q > p { ">" } else { "<" }).repeat((q as i32 - p as i32).unsigned_abs() as usize);
        let change = if held[q] != 0 {
            letter - held[q]
        } else {
            letter + LETTER_BASE
        };
        out += &(if change > 0 { "+" } else { "-" }).repeat(change.unsigned_abs() as usize);
        out.push('.');
        held[q] = letter;
    }
    println!("{}", out);
}
