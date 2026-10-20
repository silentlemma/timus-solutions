use std::collections::{BTreeSet, HashMap};
use std::fmt::Write as FmtWrite;
use std::io::{self, Read};

const VALUE_LIMIT: i32 = 1_000_000_000;
const INFINITY: i32 = 2 * VALUE_LIMIT + 1;

#[derive(Clone, Copy)]
struct Answer {
    score: i32,
    first: usize,
    second: usize,
}

fn add(
    rank: usize,
    active: &mut BTreeSet<usize>,
    best: &mut Answer,
    values: &[i32],
    potential: &[i32],
    order: &[usize],
) -> bool {
    if potential[rank] >= best.score {
        return false;
    }
    let below = active.range(..rank).next_back().copied();
    let above = active.range(rank..).next().copied();
    for other in [below, above].into_iter().flatten() {
        let score = (values[rank] + values[other]).abs();
        if score < best.score {
            *best = Answer {
                score,
                first: order[rank],
                second: order[other],
            };
        }
    }
    active.insert(rank);
    true
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let q: usize = tokens.next().unwrap().parse().unwrap();
    let days: Vec<i32> = (0..n)
        .map(|_| tokens.next().unwrap().parse().unwrap())
        .collect();
    let mut order: Vec<usize> = (0..n).collect();
    order.sort_unstable_by_key(|&day| (days[day].abs(), day));
    let mut ranks = vec![0; n];
    let values: Vec<i32> = order.iter().map(|&day| days[day]).collect();
    let mut numeric = Vec::with_capacity(n);
    for (rank, &day) in order.iter().enumerate() {
        ranks[day] = rank;
        numeric.push((values[rank], rank));
    }
    numeric.sort_unstable();
    let mut potential = vec![INFINITY; n];
    for rank in 0..n {
        let position = numeric.partition_point(|&(value, _)| value < -values[rank]);
        for &(value, other) in &numeric[position.saturating_sub(2)..n.min(position + 2)] {
            if other != rank {
                potential[rank] = potential[rank].min((values[rank] + value).abs());
            }
        }
    }
    let root = (q as f64).sqrt() as usize;
    let block_size = 1.max(2 * n / root.max(1));
    let mut buckets = vec![Vec::new(); (n + block_size - 1) / block_size];
    let mut last = HashMap::new();
    let mut global_pairs = Vec::with_capacity(n);
    let mut global_pair = None;
    let global_score = *potential.iter().min().unwrap();
    for (day, &value) in days.iter().enumerate() {
        let target = -(value as i64);
        for target in [target - global_score as i64, target + global_score as i64] {
            if let Some(&first) = last.get(&target) {
                if global_pair.map_or(true, |(previous, _)| first > previous) {
                    global_pair = Some((first, day));
                }
            }
        }
        global_pairs.push(global_pair);
        last.insert(value as i64, day);
    }
    let empty = Answer {
        score: INFINITY,
        first: 0,
        second: 0,
    };
    let mut answers = vec![empty; q];
    for id in 0..q {
        let left = tokens.next().unwrap().parse::<usize>().unwrap() - 1;
        let right: usize = tokens.next().unwrap().parse().unwrap();
        if let Some((first, second)) = global_pairs[right - 1].filter(|&(first, _)| first >= left) {
            answers[id] = Answer {
                score: global_score,
                first,
                second,
            };
        } else {
            buckets[left / block_size].push((right, left, id));
        }
    }
    for (block, queries) in buckets.iter_mut().enumerate() {
        queries.sort_unstable();
        let boundary = n.min((block + 1) * block_size);
        let mut end = boundary;
        let mut active = BTreeSet::new();
        let mut core_best = empty;
        let start = block * block_size;
        let mut suffix_best = vec![empty; boundary - start + 1];
        let mut fringe_best = empty;
        for day in (start..boundary).rev() {
            add(
                ranks[day],
                &mut active,
                &mut fringe_best,
                &values,
                &potential,
                &order,
            );
            suffix_best[day - start] = fringe_best;
        }
        active.clear();
        for &(right, left, id) in queries.iter() {
            while end < right && core_best.score != 0 {
                add(
                    ranks[end],
                    &mut active,
                    &mut core_best,
                    &values,
                    &potential,
                    &order,
                );
                end += 1;
            }
            let mut best = core_best;
            if right <= boundary {
                for &rank in &ranks[left..right] {
                    add(rank, &mut active, &mut best, &values, &potential, &order);
                }
                active.clear();
            } else {
                if suffix_best[left - start].score < best.score {
                    best = suffix_best[left - start];
                }
                // Internal pairs are known; inspect the nearest core ranks.
                for &rank in &ranks[left..boundary] {
                    if potential[rank] >= best.score {
                        continue;
                    }
                    let below = active.range(..rank).next_back().copied();
                    let above = active.range(rank..).next().copied();
                    for other in [below, above].into_iter().flatten() {
                        let score = (values[rank] + values[other]).abs();
                        if score < best.score {
                            best = Answer {
                                score,
                                first: order[rank],
                                second: order[other],
                            };
                        }
                    }
                }
            }
            answers[id] = best;
        }
    }
    let mut output = String::new();
    for best in answers {
        let first = best.first.min(best.second) + 1;
        let second = best.first.max(best.second) + 1;
        writeln!(output, "{} {}", first, second).unwrap();
    }
    print!("{}", output);
}
