use std::io::{self, Read};

const MAXC: usize = 64; // binomials needed only up to 41

// ways to put identical items into runs in order, runs may stay empty
fn spread(binom: &[[u64; MAXC]], items: usize, runs: usize) -> u64 {
    if runs == 0 {
        return (items == 0) as u64;
    }
    binom[items + runs - 1][runs - 1]
}

fn main() {
    let mut binom = vec![[0u64; MAXC]; MAXC];
    for i in 0..MAXC {
        binom[i][0] = 1;
        for j in 1..=i {
            binom[i][j] = binom[i - 1][j - 1] + binom[i - 1][j];
        }
    }
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let k: usize = words.next().unwrap().parse().unwrap();
    let bit = |c: u8| (c == b'B') as usize;
    let loco = words.next().unwrap().as_bytes();
    // have[x][y]: carriages with couplings x, y (0 = A)
    let mut have = [[0usize; 2]; 2];
    for car in words.take(n) {
        let c = car.as_bytes();
        have[bit(c[0])][bit(c[1])] += 1;
    }
    // the train starts with the coupling that fits the locomotive's right
    // end and finishes with the one that fits its left end
    let (start, end) = (bit(loco[1]), bit(loco[0]));
    let mut total = 0u64;
    for sw in 0..=k {
        // AB and BA carriages must alternate, beginning with the one that
        // leaves the starting coupling
        if (sw + 1) / 2 > have[start][1 - start] || sw / 2 > have[1 - start][start] {
            continue;
        }
        if start ^ (sw % 2) != end {
            continue;
        }
        // the runs between switches hold the AA and BB carriages
        let mut runs = [0usize; 2];
        runs[start] = sw / 2 + 1;
        runs[1 - start] = (sw + 1) / 2;
        for aa in 0..=k - sw {
            let bb = k - sw - aa;
            if aa <= have[0][0] && bb <= have[1][1] {
                total += spread(&binom, aa, runs[0]) * spread(&binom, bb, runs[1]);
            }
        }
    }
    if total > 0 {
        println!("YES\n{}", total);
    } else {
        println!("NO");
    }
}
