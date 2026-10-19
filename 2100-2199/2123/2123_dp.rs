use std::io::{self, Read};

type State = u64;

fn lower_bound(states: &[State], value: i64, mask: u64) -> usize {
    let mut left = 0;
    let mut right = states.len();
    while left < right {
        let middle = left + (right - left) / 2;
        if ((states[middle] & mask) as i64) < value {
            left = middle + 1;
        } else {
            right = middle;
        }
    }
    left
}

fn upper_bound(states: &[State], value: i64, mask: u64) -> usize {
    let mut left = 0;
    let mut right = states.len();
    while left < right {
        let middle = left + (right - left) / 2;
        if ((states[middle] & mask) as i64) <= value {
            left = middle + 1;
        } else {
            right = middle;
        }
    }
    left
}

fn merge(
    states: &[State],
    weight: i64,
    remaining: i64,
    mass_bits: u32,
    output: &mut Vec<State>,
    write: bool,
    answer: &mut i64,
) -> usize {
    let mask = (1_u64 << mass_bits) - 1;
    let mut stay = 0;
    let stay_end = upper_bound(states, remaining, mask);
    let mut reflected = upper_bound(states, weight, mask);
    let reflected_end = lower_bound(states, weight - remaining, mask);
    let mut shifted = upper_bound(states, weight, mask);
    let shifted_end = upper_bound(states, weight + remaining, mask);
    let mut size = 0;

    // Each transition produces an ordered stream; reflection reverses its order.
    while stay < stay_end || reflected > reflected_end || shifted < shifted_end {
        let stay_mass = if stay < stay_end {
            (states[stay] & mask) as i64
        } else {
            i64::MAX
        };
        let reflected_mass = if reflected > reflected_end {
            weight - (states[reflected - 1] & mask) as i64
        } else {
            i64::MAX
        };
        let shifted_mass = if shifted < shifted_end {
            (states[shifted] & mask) as i64 - weight
        } else {
            i64::MAX
        };
        let mass = stay_mass.min(reflected_mass).min(shifted_mass);
        let mut ways = 0;
        if stay_mass == mass {
            ways += (states[stay] >> mass_bits) as i64;
            stay += 1;
        }
        if reflected_mass == mass {
            reflected -= 1;
            ways += (states[reflected] >> mass_bits) as i64;
        }
        if shifted_mass == mass {
            ways += (states[shifted] >> mass_bits) as i64;
            shifted += 1;
        }
        if mass == 0 {
            if write {
                *answer += ways;
            }
        } else {
            size += 1;
            if write {
                output.push(((ways as u64) << (mass_bits - 1)) | mass as u64);
            }
        }
    }
    size
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let mut target: i64 = tokens.next().unwrap().parse().unwrap();
    let weights: Vec<i64> = (0..n)
        .map(|_| tokens.next().unwrap().parse().unwrap())
        .collect();
    let mut remaining: i64 = weights.iter().sum();
    if target > 2 * remaining {
        println!("0");
        return;
    }
    target = (target - remaining).abs();
    if target == 0 {
        println!("1");
        return;
    }

    // Each processed type halves the mass bound and at most doubles a multiplicity.
    let mut mass_bits = u64::BITS - 2;
    let mut states = vec![(1_u64 << mass_bits) | target as u64];
    let mut answer = 0;
    for &weight in weights.iter().rev() {
        if states.is_empty() {
            break;
        }
        remaining -= weight;
        // Count distinct masses first to allocate exactly one compact frontier.
        let mut next = Vec::new();
        let size = merge(
            &states,
            weight,
            remaining,
            mass_bits,
            &mut next,
            false,
            &mut answer,
        );
        next.reserve_exact(size);
        merge(
            &states,
            weight,
            remaining,
            mass_bits,
            &mut next,
            true,
            &mut answer,
        );
        states = next;
        mass_bits -= 1;
    }
    println!("{}", answer);
}
