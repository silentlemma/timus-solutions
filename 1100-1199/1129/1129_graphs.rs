use std::collections::{HashMap, VecDeque};
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let n = tok.next().unwrap();
    let rows: Vec<Vec<usize>> = (0..n)
        .map(|_| {
            let k = tok.next().unwrap();
            (0..k).map(|_| tok.next().unwrap() - 1).collect()
        })
        .collect();
    // pair the k-th mention of v in room u with the k-th mention of u in room
    // v; a door to the room itself is mentioned twice in its own row
    let mut ends: Vec<[(usize, usize); 2]> = Vec::new();
    let mut waiting: HashMap<(usize, usize), VecDeque<usize>> = HashMap::new();
    for u in 0..n {
        for (i, &v) in rows[u].iter().enumerate() {
            let queue = waiting.entry((u.min(v), u.max(v))).or_default();
            if let Some(e) = queue.pop_front() {
                ends[e][1] = (u, i);
            } else {
                queue.push_back(ends.len());
                ends.push([(u, i), (usize::MAX, 0)]);
            }
        }
    }
    // a dummy room joined to every room of odd degree makes all degrees even
    let dummy = n;
    let mut edges = ends.len();
    let mut adj: Vec<Vec<(usize, usize)>> = vec![Vec::new(); n + 1];
    for (e, pair) in ends.iter().enumerate() {
        let (u, v) = (pair[0].0, pair[1].0);
        adj[u].push((v, e));
        adj[v].push((u, e));
    }
    for u in 0..n {
        if adj[u].len() % 2 == 1 {
            adj[u].push((dummy, edges));
            adj[dummy].push((u, edges));
            edges += 1;
        }
    }
    // walk Euler circuits and orient each door along the walk
    let mut used = vec![false; edges];
    let mut tail = vec![0; edges];
    let mut ptr = vec![0; n + 1];
    for start in 0..=n {
        let mut stack = vec![start];
        while let Some(&u) = stack.last() {
            while ptr[u] < adj[u].len() && used[adj[u][ptr[u]].1] {
                ptr[u] += 1;
            }
            if ptr[u] == adj[u].len() {
                stack.pop();
                continue;
            }
            let (v, e) = adj[u][ptr[u]];
            used[e] = true;
            tail[e] = u;
            stack.push(v);
        }
    }
    let mut colours: Vec<Vec<&str>> = rows.iter().map(|r| vec![""; r.len()]).collect();
    for (e, &[(ua, ia), (ub, ib)]) in ends.iter().enumerate() {
        // green on the side the walk leaves from, orange where it enters
        let out_first = tail[e] == ua;
        colours[ua][ia] = if out_first { "G" } else { "Y" };
        colours[ub][ib] = if out_first { "Y" } else { "G" };
    }
    let lines: Vec<String> = colours.iter().map(|row| row.join(" ")).collect();
    println!("{}", lines.join("\n"));
}
