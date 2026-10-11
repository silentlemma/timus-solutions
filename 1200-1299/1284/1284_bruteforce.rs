use std::collections::BTreeSet;
use std::io::{self, Read};

const TOP: i32 = 101; // card values are 1..100
const SUITS: usize = 11;

// calls visit with every ordering of a, rearranging it in place
fn permutations(a: &mut Vec<usize>, k: usize, visit: &mut dyn FnMut(&[usize])) {
    if k == a.len() {
        visit(a);
        return;
    }
    for i in k..a.len() {
        a.swap(k, i);
        permutations(a, k + 1, visit);
        a.swap(k, i);
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i32>().unwrap());
    let n = it.next().unwrap() as usize;
    let cards: Vec<(i32, usize)> = (0..n)
        .map(|_| (it.next().unwrap(), it.next().unwrap() as usize))
        .collect();
    let blue: Vec<usize> = cards
        .iter()
        .map(|c| c.1)
        .filter(|s| s % 2 == 1)
        .collect::<BTreeSet<_>>()
        .into_iter()
        .collect();
    let yellow: Vec<usize> = cards
        .iter()
        .map(|c| c.1)
        .filter(|s| s % 2 == 0)
        .collect::<BTreeSet<_>>()
        .into_iter()
        .collect();
    // who starts: the larger colour group, or either when they are equal
    let mut starts = Vec::new();
    if blue.len() >= yellow.len() {
        starts.push((blue.clone(), yellow.clone()));
    }
    if yellow.len() >= blue.len() {
        starts.push((yellow.clone(), blue.clone()));
    }
    let mut best = 0;
    for (mut a, b) in starts {
        permutations(&mut a, 0, &mut |a: &[usize]| {
            let mut b = b.clone();
            permutations(&mut b, 0, &mut |b: &[usize]| {
                let mut place = [0i32; SUITS];
                for (i, &s) in a.iter().enumerate() {
                    place[s] = 2 * i as i32;
                }
                for (i, &s) in b.iter().enumerate() {
                    place[s] = 2 * i as i32 + 1;
                }
                for sign in [1, -1] {
                    // cards that stay form an increasing run of target ranks
                    let mut tails: Vec<i32> = Vec::new();
                    for &(value, suit) in &cards {
                        let rank = place[suit] * TOP + sign * value;
                        let k = tails.partition_point(|&t| t < rank);
                        if k == tails.len() {
                            tails.push(rank);
                        } else {
                            tails[k] = rank;
                        }
                    }
                    best = best.max(tails.len());
                }
            });
        });
    }
    println!("{}", n - best);
}
