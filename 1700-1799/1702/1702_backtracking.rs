use std::collections::HashMap;
use std::io::{self, Read};

const FLOWS: usize = 12;
const MINUTES: usize = 10;
const NIBBLE: u32 = 4; // a need is at most 10 minutes, four bits in the memo key

// the flows each flow crosses or merges with, read off the crossing: 1-3
// come from the south, 4-6 from the east, 7-9 from the north and 10-12 from
// the west, each turning right, going straight on and turning left
const CROSSES: [&[usize]; FLOWS] = [
    &[9, 11],
    &[4, 5, 6, 9, 11, 12],
    &[5, 6, 7, 8, 11, 12],
    &[2, 12],
    &[2, 3, 7, 8, 9, 12],
    &[2, 3, 8, 9, 10, 11],
    &[3, 5],
    &[3, 5, 6, 10, 11, 12],
    &[1, 2, 5, 6, 11, 12],
    &[6, 8],
    &[1, 2, 3, 6, 8, 9],
    &[2, 3, 4, 5, 8, 9],
];

struct Search {
    sets: Vec<Vec<usize>>,
    widest: usize,
    memo: HashMap<u64, bool>,
}

impl Search {
    // whether left green phases can serve every flow its need
    fn fits(&mut self, need: [usize; FLOWS], left: usize) -> bool {
        let mut top = 0;
        let mut key = left as u64;
        for i in 0..FLOWS {
            key = key << NIBBLE | need[i] as u64;
            if need[i] > need[top] {
                top = i;
            }
        }
        let total: usize = need.iter().sum();
        if need[top] > left || total > self.widest * left {
            return false;
        }
        if total == 0 {
            return true;
        }
        if let Some(&known) = self.memo.get(&key) {
            return known;
        }
        // some minute must open the flow that still needs the most
        let mut ok = false;
        for s in 0..self.sets.len() {
            if ok || !self.sets[s].contains(&top) {
                continue;
            }
            let mut rest = need;
            for &i in &self.sets[s] {
                rest[i] = rest[i].saturating_sub(1);
            }
            ok = self.fits(rest, left - 1);
        }
        self.memo.insert(key, ok);
        ok
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let v: Vec<usize> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let (cars, speed) = (&v[..FLOWS], &v[FLOWS..2 * FLOWS]);
    let mut conflict = [0usize; FLOWS];
    for (flow, others) in CROSSES.iter().enumerate() {
        for &other in others.iter() {
            conflict[flow] |= 1 << (other - 1);
        }
    }
    // a minute lets through a set of flows that cross nowhere; it never hurts
    // to open more, so only the maximal such sets matter
    let mut search = Search { sets: Vec::new(), widest: 0, memo: HashMap::new() };
    for mask in 1usize..1 << FLOWS {
        let inside = |i: usize| mask >> i & 1 == 1;
        let free = (0..FLOWS).all(|i| !(inside(i) && conflict[i] & mask != 0));
        let maximal = (0..FLOWS).all(|i| inside(i) || conflict[i] & mask != 0);
        if free && maximal {
            let set: Vec<usize> = (0..FLOWS).filter(|&i| inside(i)).collect();
            search.widest = search.widest.max(set.len());
            search.sets.push(set);
        }
    }
    let (mut lo, mut hi) = (0, *cars.iter().max().unwrap());
    while lo < hi {
        let mid = (lo + hi) / 2;
        let mut need = [0usize; FLOWS];
        for i in 0..FLOWS {
            if cars[i] > mid {
                need[i] = (cars[i] - mid + speed[i] - 1) / speed[i];
            }
        }
        if need.iter().all(|&x| x <= MINUTES) && search.fits(need, MINUTES) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    println!("{}", lo);
}
