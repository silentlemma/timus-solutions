use std::io::{self, BufRead, BufWriter, Write};

const JUICE_COUNT: usize = 3;
const TYPES: usize = (1 << JUICE_COUNT) - 1;
const PINEAPPLE: usize = 1 << (JUICE_COUNT - 1);
const STATES: usize = 1 << TYPES;
const UNREACHED: u8 = u8::MAX;

fn best_order(present: usize) -> (u8, Vec<usize>) {
    // One byte suffices for a cost (at most 21) and for a predecessor.
    let mut cost = [[UNREACHED; TYPES]; STATES];
    let mut previous = [[UNREACHED; TYPES]; STATES];
    for kind in 0..TYPES {
        if present & (1 << kind) != 0 {
            cost[1 << kind][kind] = (kind + 1).count_ones() as u8;
        }
    }
    for used in 1..=present {
        let available = present & !used;
        for last in 0..TYPES {
            let current = cost[used][last];
            if current == UNREACHED {
                continue;
            }
            let mut remaining = available;
            while remaining != 0 {
                let next = remaining.trailing_zeros() as usize;
                let bit = 1 << next;
                remaining ^= bit;
                let total = current + ((next + 1) & !(last + 1)).count_ones() as u8;
                if total < cost[used | bit][next] {
                    cost[used | bit][next] = total;
                    previous[used | bit][next] = last as u8;
                }
            }
        }
    }
    let mut last = (0..TYPES).min_by_key(|&kind| cost[present][kind]).unwrap();
    let minimum = cost[present][last];
    let mut order = Vec::with_capacity(TYPES);
    let mut used = present;
    while used != 0 {
        order.push(last);
        let predecessor = previous[used][last];
        used ^= 1 << last;
        last = usize::from(predecessor);
    }
    (minimum, order)
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock();
    let mut line = String::new();
    input.read_line(&mut line).unwrap();
    let glasses: usize = line.trim().parse().unwrap();

    // Link the glasses of each type through a single index array.
    let mut first = [0u32; TYPES];
    let mut next = vec![0u32; glasses + 1];
    let mut present = 0;
    for glass in 1..=glasses {
        line.clear();
        input.read_line(&mut line).unwrap();
        let mut mask = 0;
        for juice in line.trim().bytes() {
            mask |= match juice {
                b'A' => 1,
                b'B' => 2,
                b'P' => PINEAPPLE,
                _ => unreachable!(),
            };
        }
        let kind = mask - 1;
        present |= 1 << kind;
        next[glass] = first[kind];
        first[kind] = glass as u32;
    }

    let (minimum, order) = best_order(present);
    let mut output = BufWriter::new(io::stdout().lock());
    writeln!(output, "{}", minimum).unwrap();
    let mut separator = "";
    for &kind in order.iter().rev() {
        let mut glass = first[kind];
        while glass != 0 {
            write!(output, "{}{}", separator, glass).unwrap();
            separator = " ";
            glass = next[glass as usize];
        }
    }
    writeln!(output).unwrap();
}
