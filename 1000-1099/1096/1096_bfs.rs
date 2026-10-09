use std::collections::{HashMap, VecDeque};
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let k = v[0] as usize;
    let route: Vec<i64> = (0..k).map(|j| v[1 + 2 * j]).collect();
    let back: Vec<i64> = (0..k).map(|j| v[2 + 2 * j]).collect();
    let [.., t, s1, s2] = v[..] else {
        return;
    };
    let mut by_route: HashMap<i64, Vec<usize>> = HashMap::new();
    for j in 0..k {
        by_route.entry(route[j]).or_default().push(j);
    }
    // a state is the plate in hand: the first one, or the plate of bus j; a
    // driver swaps when the plate in hand shows the route of his bus
    let mut came: Vec<Option<usize>> = vec![None; k];
    let mut queue = VecDeque::from([(s1, s2, None)]);
    while let Some((x, y, j)) = queue.pop_front() {
        for r in [x, y] {
            for i in by_route.remove(&r).unwrap_or_default() {
                came[i] = j;
                if route[i] == t || back[i] == t {
                    let mut path = vec![i + 1];
                    let mut b = came[i];
                    while let Some(p) = b {
                        path.push(p + 1);
                        b = came[p];
                    }
                    path.reverse();
                    let lines: Vec<String> = path.iter().map(|p| p.to_string()).collect();
                    println!("{}\n{}", path.len(), lines.join("\n"));
                    return;
                }
                queue.push_back((route[i], back[i], Some(i)));
            }
        }
    }
    println!("IMPOSSIBLE");
}
