use std::io::{self, Read};

const ALPHABET: usize = 26;

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut it = text.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let word = it.next().unwrap().as_bytes();
    let size = word.len();
    // placing the remaining letter whose next occurrence is farthest moves at
    // least k places when k letters remain, so a universal word needs
    // n + (n - 1) + ... + 1 letters
    if size < n * (n + 1) / 2 {
        println!("NO");
        return;
    }
    let fail = (size + 1) as i16;
    // after[c][p]: the place just after the first c at or after place p
    let mut after = vec![vec![fail; size + 2]; ALPHABET];
    for (c, row) in after.iter_mut().enumerate() {
        for p in (0..size).rev() {
            row[p] = if (word[p] - b'a') as usize == c { (p + 1) as i16 } else { row[p + 1] };
        }
    }
    // reach[mask]: how far the greedy embedding gets for the worst order of
    // the letters in mask; submasks come first in increasing order, and one
    // failing mask makes the whole set fail, so the table stops there
    let mut reach: Vec<i16> = vec![0];
    for mask in 1usize..1 << n {
        let mut best = 0;
        let mut rest = mask;
        while rest != 0 {
            let letter = rest.trailing_zeros() as usize;
            rest &= rest - 1;
            best = best.max(after[letter][reach[mask ^ (1 << letter)] as usize]);
        }
        if best == fail {
            println!("NO");
            return;
        }
        reach.push(best);
    }
    println!("YES");
}
