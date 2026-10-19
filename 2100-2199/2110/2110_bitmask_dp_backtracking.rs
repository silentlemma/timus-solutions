use std::io::{self, Read};

const SMALL_REMOVALS: usize = 7;

fn visit(
    values: &[u32],
    suffix: &[u32],
    index: usize,
    needed: usize,
    current: u32,
    best: &mut u32,
) {
    if needed == 0 {
        *best = (*best).max(current);
        return;
    }
    let upper = current | suffix[index];
    if upper <= *best {
        return;
    }
    // One witness per uncovered bit suffices; extra elements fill unused places.
    if needed == values.len() - index || needed >= (suffix[index] & !current).count_ones() as usize
    {
        *best = upper;
        return;
    }
    visit(
        values,
        suffix,
        index + 1,
        needed - 1,
        current | values[index],
        best,
    );
    visit(values, suffix, index + 1, needed, current, best);
}

fn search(values: &[u32], kept: usize) -> u32 {
    let mut suffix = vec![0; values.len() + 1];
    for index in (0..values.len()).rev() {
        suffix[index] = suffix[index + 1] | values[index];
    }
    let mut best = values[..kept].iter().fold(0, |acc, value| acc | value);
    visit(values, &suffix, 0, kept, 0, &mut best);
    best
}

fn solve_dp(values: &[u32], kept: usize, full: u32) -> u32 {
    let mut count = vec![kept + 1; full as usize + 1];
    count[0] = 0;
    let mut upper = 0;
    let mut best = 0;
    for &value in values {
        // OR never decreases a mask, so descending updates use each element once.
        for mask in (0..=upper).rev() {
            if count[mask] < kept {
                let merged = mask | value as usize;
                count[merged] = count[merged].min(count[mask] + 1);
                best = best.max(merged);
            }
        }
        upper |= value as usize;
        if best == full as usize {
            break;
        }
    }
    best as u32
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let removed: usize = tokens.next().unwrap().parse().unwrap();
    let mut values: Vec<u32> = tokens.take(n).map(|token| token.parse().unwrap()).collect();
    let full = values.iter().fold(0, |acc, value| acc | value);
    let kept = n - removed;
    let answer = if kept >= full.count_ones() as usize {
        full
    } else {
        values.sort_unstable_by(|left, right| right.cmp(left));
        if removed <= SMALL_REMOVALS {
            search(&values, kept)
        } else {
            values.dedup();
            solve_dp(&values, kept, full)
        }
    };
    println!("{}", answer);
}
