use std::io::{self, Read};

const SCALE: i64 = 1000;
const SAFE: i64 = 256 * SCALE;
const DEODORANT: usize = 1;
const PERFUME: usize = 2;
const BOTH: usize = DEODORANT | PERFUME;
const INF: usize = usize::MAX;
const NONE: usize = usize::MAX;
const DOWN_NUM: i64 = 3;
const DOWN_DEN: i64 = 4;
const UP_NUM: i64 = 11;
const UP_DEN: i64 = 10;

#[derive(Clone, Copy)]
struct Move {
    kind: usize,
    deodorized: usize,
    perfumed: usize,
    set: usize,
}

// keep the sets not inside another one: carrying more costs nothing,
// since fruit already outside can be brought back and carried again
fn add_maximal(moves: &mut Vec<Move>, mut sets: Vec<usize>, kind: usize, i: usize, j: usize) {
    sets.sort_by_key(|m| std::cmp::Reverse(m.count_ones()));
    let mut kept: Vec<usize> = Vec::new();
    for a in sets {
        if !kept.iter().any(|&b| a & b == a) {
            kept.push(a);
            moves.push(Move { kind, deodorized: i, perfumed: j, set: a });
        }
    }
}

fn names(set: usize, n: usize) -> String {
    let list: Vec<String> =
        (0..n).filter(|k| set >> k & 1 == 1).map(|k| (k + 1).to_string()).collect();
    format!("{} {}", list.len(), list.join(" "))
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let n = v[0] as usize;
    // aromas times 1000 keep 3/4, 11/10 and both together whole
    let w: Vec<i64> = v[1..=n].iter().map(|x| x * SCALE).collect();
    let full = (1usize << n) - 1;
    let mut total = vec![0i64; full + 1];
    for m in 1..=full {
        total[m] = total[m & (m - 1)] + w[m.trailing_zeros() as usize];
    }
    let collect = |need: usize, change: i64| -> Vec<usize> {
        (1..=full).filter(|&m| m & need == need && (total[m] + change) % SAFE == 0).collect()
    };
    let mut moves = Vec::new();
    add_maximal(&mut moves, collect(0, 0), 0, NONE, NONE);
    // what each spray adds to the total of a set holding the fruit
    let weaker: Vec<i64> = w.iter().map(|x| x * DOWN_NUM / DOWN_DEN - x).collect();
    let stronger: Vec<i64> = w.iter().map(|x| x * UP_NUM / UP_DEN - x).collect();
    for i in 0..n {
        add_maximal(&mut moves, collect(1 << i, weaker[i]), DEODORANT, i, NONE);
        add_maximal(&mut moves, collect(1 << i, stronger[i]), PERFUME, NONE, i);
        for j in 0..n {
            let change = if i != j {
                weaker[i] + stronger[j]
            } else {
                w[i] * DOWN_NUM * UP_NUM / (DOWN_DEN * UP_DEN) - w[i]
            };
            add_maximal(&mut moves, collect(1 << i | 1 << j, change), BOTH, i, j);
        }
    }
    // carrying more is never worse, so of the moves with the same sprays only
    // the largest sets are kept, and none inside a set needing fewer sprays
    moves.sort_by_key(|mv| std::cmp::Reverse(mv.set.count_ones()));
    let mut kept: Vec<Move> = Vec::new();
    for kind in 0..=BOTH {
        let start = kept.len();
        for mv in moves.iter().filter(|mv| mv.kind == kind) {
            let inside = kept.iter().enumerate().any(|(k, other)| {
                (k >= start || other.kind & kind == other.kind) && mv.set & other.set == mv.set
            });
            if !inside {
                kept.push(*mv);
            }
        }
    }
    let moves = kept;
    // best[used][mask]: fewest exits that get the fruit of mask out
    let mut best = vec![vec![INF; full + 1]; BOTH + 1];
    let mut choice = vec![vec![0usize; full + 1]; BOTH + 1];
    for row in best.iter_mut() {
        row[0] = 0;
    }
    for mask in 1..=full {
        for used in 0..=BOTH {
            for (k, mv) in moves.iter().enumerate() {
                if mv.kind & used != 0 || mv.set & mask == 0 {
                    continue;
                }
                let next = best[used | mv.kind][mask & !mv.set];
                if next != INF && next + 1 < best[used][mask] {
                    best[used][mask] = next + 1;
                    choice[used][mask] = k;
                }
            }
        }
    }
    if best[0][full] == INF {
        println!("IMPOSSIBLE");
        return;
    }
    let mut lines = Vec::new();
    let (mut mask, mut used) = (full, 0);
    while mask != 0 {
        let mv = &moves[choice[used][mask]];
        let back = mv.set & !mask & full;
        if back != 0 {
            lines.push(format!("return {}", names(back, n)));
        }
        if mv.deodorized != NONE {
            lines.push(format!("dearomatize {}", mv.deodorized + 1));
        }
        if mv.perfumed != NONE {
            lines.push(format!("aromatize {}", mv.perfumed + 1));
        }
        lines.push(format!("take {}", names(mv.set, n)));
        used |= mv.kind;
        mask &= !mv.set;
    }
    println!("{}\n{}", lines.len(), lines.join("\n"));
}
