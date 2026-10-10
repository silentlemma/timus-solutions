use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    let mut knows = vec![vec![false; n]; n];
    for row in knows.iter_mut() {
        loop {
            let j = it.next().unwrap();
            if j == 0 {
                break;
            }
            row[j - 1] = true;
        }
    }
    // two people who do not both know each other must be in different
    // teams, so these pairs must form a bipartite graph; each component
    // gives two sides, and one side of each goes to the first team
    let mut side = vec![usize::MAX; n];
    let mut parts: Vec<[Vec<usize>; 2]> = Vec::new();
    for s in 0..n {
        if side[s] != usize::MAX {
            continue;
        }
        side[s] = 0;
        let mut groups = [Vec::new(), Vec::new()];
        let mut queue = vec![s];
        let mut h = 0;
        while h < queue.len() {
            let v = queue[h];
            h += 1;
            groups[side[v]].push(v);
            for u in 0..n {
                if u != v && !(knows[v][u] && knows[u][v]) {
                    if side[u] == usize::MAX {
                        side[u] = 1 - side[v];
                        queue.push(u);
                    } else if side[u] == side[v] {
                        println!("No solution");
                        return;
                    }
                }
            }
        }
        parts.push(groups);
    }
    // reach[k][size]: which side of part k-1 gives the first team that size
    let mut reach = vec![vec![None; n + 1]; parts.len() + 1];
    reach[0][0] = Some(0);
    for (k, groups) in parts.iter().enumerate() {
        for size in 0..=n {
            if reach[k][size].is_none() {
                continue;
            }
            for (pick, group) in groups.iter().enumerate() {
                let next = size + group.len();
                if reach[k + 1][next].is_none() {
                    reach[k + 1][next] = Some(pick);
                }
            }
        }
    }
    let mut size = (0..=n)
        .filter(|&s| reach[parts.len()][s].is_some())
        .min_by_key(|&s| (2 * s as i64 - n as i64).abs())
        .unwrap();
    let mut team: [Vec<usize>; 2] = [Vec::new(), Vec::new()];
    for k in (0..parts.len()).rev() {
        let pick = reach[k + 1][size].unwrap();
        team[0].extend(parts[k][pick].iter().copied());
        team[1].extend(parts[k][1 - pick].iter().copied());
        size -= parts[k][pick].len();
    }
    for t in &team {
        let ids: String = t.iter().map(|v| format!(" {}", v + 1)).collect();
        println!("{}{}", t.len(), ids);
    }
}
