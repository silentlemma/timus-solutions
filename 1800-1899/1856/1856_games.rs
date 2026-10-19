use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|v| v.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    let mut spell = [vec![0usize; n], vec![0usize; n]];
    for i in 0..n {
        spell[0][i] = it.next().unwrap() - 1;
        spell[1][i] = it.next().unwrap() - 1;
    }
    // the army gathers exactly when every pair of garrisons can be forced
    // together, one pair after another; a pair (u, v), u < v, is the number
    // u * n + v, and a day is her spell m, then his spell k
    let size = n * n;
    let mut open_moves = vec![0u8; 2 * size]; // his replies keeping the pair apart
    let mut target: Vec<u32> = Vec::new(); // the pair after both spells
    let mut source: Vec<u32> = Vec::new(); // pair * 2 + her spell
    for u in 0..n {
        for v in u + 1..n {
            let p = u * n + v;
            for mine in 0..spell.len() {
                let (x, y) = (spell[mine][u], spell[mine][v]);
                if x == y {
                    continue;
                }
                for k in spell.iter() {
                    let (s, t) = (k[x].min(k[y]), k[x].max(k[y]));
                    if s == t {
                        continue;
                    }
                    target.push((s * n + t) as u32);
                    source.push((2 * p + mine) as u32);
                    open_moves[2 * p + mine] += 1;
                }
            }
        }
    }
    // the replies that lead into every pair, grouped by that pair
    let mut start = vec![0u32; size + 1];
    for &q in &target {
        start[q as usize + 1] += 1;
    }
    for q in 0..size {
        start[q + 1] += start[q];
    }
    let mut place = start[..size].to_vec();
    let mut from = vec![0u32; target.len()];
    for (&q, &s) in target.iter().zip(&source) {
        from[place[q as usize] as usize] = s;
        place[q as usize] += 1;
    }
    // a pair is won when some spell of hers leaves him no reply that keeps
    // the pair apart outside the won pairs
    let mut won = vec![false; size];
    let mut queue: Vec<usize> = Vec::new();
    for u in 0..n {
        for v in u + 1..n {
            let p = u * n + v;
            if open_moves[2 * p] == 0 || open_moves[2 * p + 1] == 0 {
                won[p] = true;
                queue.push(p);
            }
        }
    }
    let mut h = 0;
    while h < queue.len() {
        let q = queue[h];
        h += 1;
        for e in start[q] as usize..start[q + 1] as usize {
            let mv = from[e] as usize;
            let p = mv >> 1;
            if won[p] {
                continue;
            }
            open_moves[mv] -= 1;
            if open_moves[mv] == 0 {
                won[p] = true;
                queue.push(p);
            }
        }
    }
    println!("{}", if queue.len() == n * (n - 1) / 2 { "War" } else { "Peace" });
}
