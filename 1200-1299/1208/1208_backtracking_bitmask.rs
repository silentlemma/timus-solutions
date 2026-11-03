use std::io::{self, Read};

const TEAM_SIZE: usize = 3;

fn search(mask: u32, selected: u32, clash: &[u32], answer: &mut u32) {
    if selected + mask.count_ones() <= *answer {
        return;
    }
    let (mut chosen, mut degree, mut remaining) = (0, 0, mask);
    while remaining != 0 {
        let i = remaining.trailing_zeros() as usize;
        let count = (mask & clash[i]).count_ones();
        if count > degree {
            chosen = i;
            degree = count;
        }
        remaining &= remaining - 1;
    }
    // An edgeless remainder can be taken whole. Try the most-conflicting
    // team first to tighten the upper bound for the exclusion branch.
    if degree <= 1 {
        *answer = (*answer).max(selected + mask.count_ones());
        return;
    }
    search(mask & !clash[chosen], selected + 1, clash, answer);
    search(mask & !(1 << chosen), selected, clash, answer);
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let k: usize = tokens.next().unwrap().parse().unwrap();
    let teams: Vec<Vec<&str>> = (0..k)
        .map(|_| tokens.by_ref().take(TEAM_SIZE).collect())
        .collect();
    let mut clash = vec![0u32; k];
    for i in 0..k {
        for j in 0..k {
            if teams[i].iter().any(|name| teams[j].contains(name)) {
                clash[i] |= 1 << j;
            }
        }
    }
    let mut answer = 0;
    search((1 << k) - 1, 0, &clash, &mut answer);
    println!("{}", answer);
}
