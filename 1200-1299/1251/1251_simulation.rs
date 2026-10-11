use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io::{self, Read};

const FORGET: i64 = 1001; // a grave untouched for 1000 days can go on the next day
const NOTICE: i64 = 101; // and only when no neighbour was visited in the last 100

type Pending = BinaryHeap<Reverse<(i64, usize)>>;

// sets the day grave g may be freed and queues it
fn schedule(g: usize, touched: &[i64], near: &[i64], release: &mut [i64], pending: &mut Pending) {
    release[g] = (touched[g] + FORGET).max(near[g] + NOTICE);
    pending.push(Reverse((release[g], g)));
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let m: usize = words.next().unwrap().parse().unwrap();
    let cells = n * m;
    // the client in each grave (0 if free), the last burial or visit of that
    // client, the last visit next door and the day the grave may be freed
    let mut owner = vec![0usize; cells];
    let (mut touched, mut near_visit, mut release) =
        (vec![0i64; cells], vec![-NOTICE; cells], vec![0i64; cells]);
    let mut grave_of: Vec<Option<usize>> = Vec::new();
    let mut free: BinaryHeap<Reverse<usize>> = (0..cells).map(Reverse).collect();
    let mut pending: Pending = BinaryHeap::new();
    let mut cremated = 0;
    while let Some(word) = words.next() {
        let day: i64 = word.parse().unwrap();
        let kind = words.next().unwrap();
        // graves free at the start of the day, before its events
        while let Some(&Reverse((when, g))) = pending.peek() {
            if when > day {
                break;
            }
            pending.pop();
            if owner[g] != 0 && release[g] == when {
                grave_of[owner[g] - 1] = None;
                owner[g] = 0;
                free.push(Reverse(g));
            }
        }
        if kind == "d" {
            grave_of.push(None);
            match free.pop() {
                None => cremated += 1,
                Some(Reverse(g)) => {
                    owner[g] = grave_of.len();
                    *grave_of.last_mut().unwrap() = Some(g);
                    touched[g] = day;
                    schedule(g, &touched, &near_visit, &mut release, &mut pending);
                }
            }
            continue;
        }
        let client: usize = words.next().unwrap().parse().unwrap();
        let g = match grave_of[client - 1] {
            Some(g) => g,
            None => continue,
        };
        touched[g] = day;
        schedule(g, &touched, &near_visit, &mut release, &mut pending);
        let (r, c) = (g / m, g % m);
        for nr in r.saturating_sub(1)..=(r + 1).min(n - 1) {
            for nc in c.saturating_sub(1)..=(c + 1).min(m - 1) {
                if (nr, nc) != (r, c) {
                    let k = nr * m + nc;
                    near_visit[k] = day;
                    if owner[k] != 0 {
                        schedule(k, &touched, &near_visit, &mut release, &mut pending);
                    }
                }
            }
        }
    }
    println!("{}", cremated);
}
