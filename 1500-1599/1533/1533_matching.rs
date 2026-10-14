use std::io::{self, Read};

/// Tries to match the heavier copy of i, rerouting earlier matches.
fn augment(
    i: usize,
    heavier: &[Vec<bool>],
    match_of: &mut [Option<usize>],
    seen: &mut [bool],
) -> bool {
    for j in 0..heavier.len() {
        if heavier[i][j] && !seen[j] {
            seen[j] = true;
            if match_of[j].map_or(true, |owner| augment(owner, heavier, match_of, seen)) {
                match_of[j] = Some(i);
                return true;
            }
        }
    }
    false
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let mut it = s.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    // heavier[i][j]: hobbit i is known to outweigh j
    let mut heavier: Vec<Vec<bool>> = (0..n)
        .map(|_| (0..n).map(|_| it.next().unwrap() == "1").collect())
        .collect();
    // the weighings are consistent, so the closure is a strict order
    for k in 0..n {
        for i in 0..n {
            if heavier[i][k] {
                for j in 0..n {
                    heavier[i][j] = heavier[i][j] || heavier[k][j];
                }
            }
        }
    }
    // by Dilworth, the largest set of incomparable hobbits is n minus a
    // maximum matching between "heavier" copies and "lighter" copies
    let mut match_of: Vec<Option<usize>> = vec![None; n];
    let matched: Vec<bool> = (0..n)
        .map(|i| augment(i, &heavier, &mut match_of, &mut vec![false; n]))
        .collect();
    // Konig: walk alternating paths from the unmatched heavier copies; the
    // hobbits reached on the heavier side but not on the lighter side form
    // the answer, as everything else is a vertex cover
    let mut left: Vec<bool> = matched.iter().map(|&m| !m).collect();
    let mut right = vec![false; n];
    let mut stack: Vec<usize> = (0..n).filter(|&i| left[i]).collect();
    while let Some(i) = stack.pop() {
        for j in 0..n {
            if heavier[i][j] && !right[j] {
                right[j] = true;
                if let Some(owner) = match_of[j] {
                    if !left[owner] {
                        left[owner] = true;
                        stack.push(owner);
                    }
                }
            }
        }
    }
    let chosen: Vec<String> = (0..n)
        .filter(|&i| left[i] && !right[i])
        .map(|i| (i + 1).to_string())
        .collect();
    println!("{}", chosen.len());
    println!("{}", chosen.join(" "));
}
