use std::fmt::Write as _;
use std::io::{self, Read};

const WIN: i32 = 3;
const SIGNS: [&str; 4] = ["<", "<=", ">=", ">"];

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i32> = input.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let n = v[0] as usize;
    let mut left: Vec<i32> = v[1..=n].to_vec();
    let mut got = vec![vec![0usize; n]; n];
    let mut active: Vec<usize> = (0..n).collect();
    let mut ok = true;
    // the weakest team plays all its games now: it keeps its own points
    // and hands the rest out, three a game, to the strongest teams first
    while ok && active.len() > 1 {
        active.sort_by_key(|&t| (left[t], t));
        let weak = active[0];
        let mut give = WIN * (active.len() as i32 - 1) - left[weak];
        if give < 0 {
            break;
        }
        for &t in active[1..].iter().rev() {
            let share = give.min(WIN);
            give -= share;
            left[t] -= share;
            got[t][weak] = share as usize;
            got[weak][t] = (WIN - share) as usize;
            if left[t] < 0 {
                ok = false;
            }
        }
        left[weak] = 0;
        if give != 0 {
            ok = false;
        }
        active.remove(0);
    }
    if !ok || left.iter().any(|&x| x != 0) {
        println!("INCORRECT");
        return;
    }
    let mut out = String::from("CORRECT\n");
    for i in 0..n {
        for j in i + 1..n {
            writeln!(out, "{} {} {}", i + 1, SIGNS[got[i][j]], j + 1).unwrap();
        }
    }
    print!("{}", out);
}
