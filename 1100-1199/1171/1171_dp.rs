use std::io::{self, Read};

const SIDE: usize = 4;
const ROOMS: usize = SIDE * SIDE;
const NONE: i64 = i64::MIN / 2;
// moves inside a level: name, row step, column step
const MOVES: [(u8, i32, i32); 4] = [(b'N', -1, 0), (b'E', 0, 1), (b'S', 1, 0), (b'W', 0, -1)];

fn step(u: usize, d: usize) -> Option<usize> {
    let r = (u / SIDE) as i32 + MOVES[d].1;
    let c = (u % SIDE) as i32 + MOVES[d].2;
    let inside = (0..SIDE as i32).contains(&r) && (0..SIDE as i32).contains(&c);
    inside.then(|| r as usize * SIDE + c as usize)
}

// best[s][e][k]: most food on a path of k rooms from s to e in one level
type Table = Vec<Vec<Vec<i32>>>;

fn walk(food: &[i32], row: &mut Vec<Vec<i32>>, u: usize, mask: u32, k: usize, total: i32) {
    if total > row[u][k] {
        row[u][k] = total;
    }
    for d in 0..MOVES.len() {
        if let Some(v) = step(u, d) {
            if mask >> v & 1 == 0 {
                walk(food, row, v, mask | 1 << v, k + 1, total + food[v]);
            }
        }
    }
}

// appends a path of `left` rooms from u to e with exactly `rest` food
fn find_moves(
    food: &[i32],
    u: usize,
    e: usize,
    mask: u32,
    left: usize,
    rest: i32,
    path: &mut Vec<u8>,
) -> bool {
    if left == 1 {
        return u == e && rest == food[u];
    }
    for d in 0..MOVES.len() {
        if let Some(v) = step(u, d) {
            if mask >> v & 1 == 0 {
                path.push(MOVES[d].0);
                if find_moves(food, v, e, mask | 1 << v, left - 1, rest - food[u], path) {
                    return true;
                }
                path.pop();
            }
        }
    }
    false
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i32>().unwrap());
    let n = it.next().unwrap() as usize;
    let mut foods = Vec::new();
    let mut doors = Vec::new();
    for _ in 0..n {
        foods.push((0..ROOMS).map(|_| it.next().unwrap()).collect::<Vec<_>>());
        doors.push((0..ROOMS).map(|_| it.next().unwrap()).collect::<Vec<_>>());
    }
    let r = it.next().unwrap() as usize;
    let start = (r - 1) * SIDE + it.next().unwrap() as usize - 1;
    let tables: Vec<Table> = foods
        .iter()
        .map(|food| {
            (0..ROOMS)
                .map(|s| {
                    let mut row = vec![vec![-1; ROOMS + 1]; ROOMS];
                    walk(food, &mut row, s, 1 << s, 1, food[s]);
                    row
                })
                .collect()
        })
        .collect();
    // the path maximising den * food - num * rooms, as per-level choices
    // (start, end, rooms), with its food and room count
    let best_path = |num: i64, den: i64| {
        let mut after = vec![0i64; ROOMS];
        let mut choice = vec![vec![(0, 0, 0); ROOMS]; n];
        for lv in (0..n).rev() {
            let mut here = vec![NONE; ROOMS];
            for s in 0..ROOMS {
                for e in 0..ROOMS {
                    if (lv < n - 1 && doors[lv][e] == 0) || after[e] == NONE {
                        continue;
                    }
                    for k in 1..=ROOMS {
                        let w = tables[lv][s][e][k];
                        let v = den * w as i64 - num * k as i64 + after[e];
                        if w >= 0 && v > here[s] {
                            here[s] = v;
                            choice[lv][s] = (s, e, k);
                        }
                    }
                }
            }
            after = here;
        }
        let (mut plan, mut total, mut count, mut s) = (Vec::new(), 0i64, 0i64, start);
        for lv in 0..n {
            let (_, e, k) = choice[lv][s];
            plan.push((s, e, k));
            total += tables[lv][s][e][k] as i64;
            count += k as i64;
            s = e;
        }
        (plan, total, count)
    };
    // Dinkelbach: move to the better ratio until no path beats the current
    let (mut num, mut den, mut chosen) = (0i64, 1i64, Vec::new());
    loop {
        let (plan, total, count) = best_path(num, den);
        if total * den <= num * count {
            break;
        }
        num = total;
        den = count;
        chosen = plan;
    }
    let mut moves = Vec::new();
    for (lv, &(s, e, k)) in chosen.iter().enumerate() {
        if lv > 0 {
            moves.push(b'D');
        }
        find_moves(&foods[lv], s, e, 1 << s, k, tables[lv][s][e][k], &mut moves);
    }
    println!("{:.4}\n{}", num as f64 / den as f64, moves.len());
    if !moves.is_empty() {
        println!("{}", String::from_utf8(moves).unwrap());
    }
}
