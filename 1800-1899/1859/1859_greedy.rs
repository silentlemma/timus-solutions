use std::io::{self, Read};

const SEATS: usize = 4; // compartment seats in a block
const SIDES: usize = 2; // side seats in a block

fn find(parent: &mut Vec<usize>, mut x: usize) -> usize {
    while parent[x] != x {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    x
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let wish = it.next().unwrap().as_bytes();
    let m: usize = it.next().unwrap().parse().unwrap();
    let people = (SEATS + SIDES) * n;
    let mut parent: Vec<usize> = (0..people).collect();
    for _ in 0..m {
        let a: usize = it.next().unwrap().parse().unwrap();
        let b: usize = it.next().unwrap().parse().unwrap();
        let (ra, rb) = (find(&mut parent, a - 1), find(&mut parent, b - 1));
        parent[ra] = rb;
    }
    let mut members: Vec<Vec<usize>> = vec![Vec::new(); people];
    for p in 0..people {
        let r = find(&mut parent, p);
        members[r].push(p + 1);
    }
    // a group of friends wants a compartment seats and b side seats; a block
    // holds one group with b = 2, or two groups with b = 1, and groups with
    // b = 0 fill the compartment seats left: kind[b][a]
    let mut kind: Vec<Vec<Vec<Vec<usize>>>> = vec![vec![Vec::new(); SEATS + 1]; SIDES + 1];
    for g in members.into_iter().filter(|g| !g.is_empty()) {
        let a = g.iter().filter(|&&p| wish[p - 1] == b'1').count();
        kind[g.len() - a][a].push(g);
    }
    let wholes = kind.pop().unwrap();
    let mut halves = kind.pop().unwrap();
    let fillers = kind.pop().unwrap();
    let count = |x: &Vec<Vec<usize>>| x.len() as i64;
    let (s0, s1, s2) = (count(&halves[0]), count(&halves[1]), count(&halves[2]));
    let (s3, s4) = (count(&halves[SEATS - 1]), count(&halves[SEATS]));
    let (t0, t1, t2) = (count(&wholes[0]), count(&wholes[1]), count(&wholes[2]));
    let (f2, f3, f4) = (count(&fillers[2]), count(&fillers[SEATS - 1]), count(&fillers[SEATS]));
    // can the fillers fill blocks with c4, c3, c2 free compartment seats (and
    // some with 1)? fours need a 4, threes take a 3 first and then a 4, twos
    // take what is left of the 2s, 3s and 4s
    let fits = |c4: i64, c3: i64, c2: i64| {
        if f4 > c4 || f3 > c3 + c4 - f4 {
            return false;
        }
        let late = (f3 - c3).max(0); // threes in blocks with 4 free seats
        f2 <= c2 + (c3 - f3 + late) + 2 * (c4 - f4 - late)
    };
    // two halves with a1 and a2 leave 4 - a1 - a2 free seats; merging the
    // free seats of two blocks never hurts, so threes pair with ones when
    // they can, and two (0, 2) pairs would rather be (2, 2) and (0, 0)
    let x31 = s3.min(s1);
    let x30 = s3 - x31;
    let ones = s1 - x31;
    let zeros = s0 - s4 - x30;
    let mut plan: Vec<(usize, usize, i64)> = Vec::new();
    'search: for x20 in 0..=1i64 {
        for x21 in 0..=(s2 - x20).min(ones) {
            // with x11 pairs (1, 1) the zeros left pair up as base + 2 x11
            let base = zeros - x20 - ones + x21;
            if (s2 - x21 - x20) % 2 != 0 || base % 2 != 0 {
                continue;
            }
            // x11 must leave both kinds of pairs possible and give the fours
            // and the threes their blocks; the room for twos rises until the
            // free threes run short of threes and falls after that
            let low = 0.max(-base / 2).max(f4 - t0 - base / 2);
            let high = ((ones - x21) / 2).min(t0 + t1 + ones - x21 + base / 2 - f3 - f4);
            let peak = ((t1 + ones - x21 - f3).div_euclid(2)).max(low).min(high);
            for x11 in peak - 1..=peak + 1 {
                let (x10, x00) = (ones - x21 - 2 * x11, base / 2 + x11);
                if low <= x11 && x11 <= high && fits(t0 + x00, t1 + x10, t2 + x20 + x11) {
                    plan = vec![
                        (SEATS, 0, s4),
                        (SEATS - 1, 1, x31),
                        (SEATS - 1, 0, x30),
                        (2, 2, (s2 - x21 - x20) / 2),
                        (2, 1, x21),
                        (2, 0, x20),
                        (1, 1, x11),
                        (1, 0, x10),
                        (0, 0, x00),
                    ];
                    break 'search;
                }
            }
        }
    }
    // members and free compartment seats of every block
    let mut blocks: Vec<(Vec<usize>, usize)> = Vec::new();
    for (a, single) in wholes.into_iter().enumerate() {
        blocks.extend(single.into_iter().map(|g| (g, SEATS - a)));
    }
    for (a, b, k) in plan {
        for _ in 0..k {
            let mut g = halves[a].pop().unwrap();
            g.extend(halves[b].pop().unwrap());
            blocks.push((g, SEATS - a - b));
        }
    }
    // the fillers, largest first, as the check above assumes
    let mut free: Vec<Vec<usize>> = vec![Vec::new(); SEATS + 1];
    for (i, block) in blocks.iter().enumerate() {
        free[block.1].push(i);
    }
    for size in (1..=SEATS).rev() {
        for g in &fillers[size] {
            let at = (size..=SEATS).find(|&c| !free[c].is_empty()).unwrap();
            let i = free[at].pop().unwrap();
            blocks[i].0.extend(g.iter().copied());
            free[at - size].push(i);
        }
    }
    let lines: Vec<String> = blocks
        .iter()
        .map(|(g, _)| g.iter().map(|p| p.to_string()).collect::<Vec<_>>().join(" "))
        .collect();
    println!("{}", lines.join("\n"));
}
