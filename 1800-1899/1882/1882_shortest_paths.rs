use std::io::{self, Read, Write};

const KEYS: &[&str] = &["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"];
const SLOWEST: usize = 4;

fn main() {
    let mut presses = [0usize; (b'z' + 1) as usize];
    for key in KEYS.iter() {
        for (k, ch) in key.bytes().enumerate() {
            presses[ch as usize] = k + 1;
        }
    }
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let words: Vec<&[u8]> = (0..n).map(|_| it.next().unwrap().as_bytes()).collect();
    // state offset[x] + d: name x is current and its first d letters are
    // typed; node_of[state] is the trie node of the typed letters
    let mut offset = vec![0usize; n + 1];
    for x in 0..n {
        offset[x + 1] = offset[x] + words[x].len() + 1;
    }
    let states = offset[n];
    let mut node_of = vec![0usize; states];
    let mut owner = vec![0usize; states];
    let (mut low, mut high) = (vec![0usize], vec![n - 1]); // names below a node form a range
    let mut children: Vec<Vec<(usize, usize)>> = vec![Vec::new()];
    let mut path = vec![0usize];
    for x in 0..n {
        let w = words[x];
        let mut same = 0;
        if x > 0 {
            let p = words[x - 1];
            while same < w.len() && same < p.len() && w[same] == p[same] {
                same += 1;
            }
        }
        path.truncate(same + 1);
        for d in same + 1..=w.len() {
            let v = low.len();
            low.push(x);
            high.push(x);
            children.push(Vec::new());
            let top = *path.last().unwrap();
            children[top].push((offset[x] + d, presses[w[d - 1] as usize]));
            path.push(v);
        }
        for d in 0..=w.len() {
            node_of[offset[x] + d] = path[d];
            owner[offset[x] + d] = x;
            high[path[d]] = x;
        }
    }
    let hubs = low.len();
    let mut dist = vec![usize::MAX; states + hubs];
    // every move costs at most SLOWEST, so SLOWEST + 1 buckets in a circle
    let mut buckets: Vec<Vec<usize>> = vec![Vec::new(); SLOWEST + 1];
    dist[0] = 0;
    buckets[0].push(0);
    let mut pending = 1usize;
    let mut moves: Vec<(usize, usize)> = Vec::with_capacity(SLOWEST);
    let mut now = 0usize;
    while pending > 0 {
        let b = now % (SLOWEST + 1);
        while let Some(s) = buckets[b].pop() {
            pending -= 1;
            if dist[s] != now {
                continue;
            }
            moves.clear();
            if s >= states {
                moves.extend_from_slice(&children[s - states]);
            } else {
                let x = owner[s];
                let d = s - offset[x];
                let v = node_of[s];
                let nxt = if x < high[v] { x + 1 } else { low[v] };
                let prv = if x > low[v] { x - 1 } else { high[v] };
                moves.push((offset[nxt] + d, 1));
                moves.push((offset[prv] + d, 1));
                moves.push((states + v, 0));
                if d > 0 {
                    moves.push((s - 1, 1));
                }
            }
            for &(t, cost) in &moves {
                if now + cost < dist[t] {
                    dist[t] = now + cost;
                    buckets[(now + cost) % (SLOWEST + 1)].push(t);
                    pending += 1;
                }
            }
        }
        now += 1;
    }
    let best: Vec<String> = (0..n)
        .map(|x| dist[offset[x]..offset[x + 1]].iter().min().unwrap().to_string())
        .collect();
    let out = best.join(" ") + "\n";
    io::stdout().write_all(out.as_bytes()).unwrap();
}
