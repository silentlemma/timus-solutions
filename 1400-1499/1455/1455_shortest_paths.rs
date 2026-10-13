use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap};
use std::io::{self, Read};

/// The previous tail, the new piece of text, and whether the tail starts a search.
struct Link {
    from: String,
    piece: String,
    first: bool,
}

struct Search {
    dist: HashMap<String, usize>,
    back: HashMap<String, Link>,
    heap: BinaryHeap<Reverse<(usize, String)>>,
}

impl Search {
    fn relax(&mut self, tail: &str, cost: usize, link: Link) {
        if self.dist.get(tail).map_or(false, |&d| d <= cost) {
            return;
        }
        self.dist.insert(tail.to_string(), cost);
        self.back.insert(tail.to_string(), link);
        self.heap.push(Reverse((cost, tail.to_string())));
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let words: Vec<&str> = it.take(n).collect();
    // a state is the tail by which one parse runs ahead of the other; the
    // cost is the length of the text so far, and Dijkstra finds the shortest text
    let mut search = Search {
        dist: HashMap::new(),
        back: HashMap::new(),
        heap: BinaryHeap::new(),
    };
    for u in &words {
        for v in &words {
            if u != v && v.starts_with(u) {
                let link = Link {
                    from: String::new(),
                    piece: v.to_string(),
                    first: true,
                };
                search.relax(&v[u.len()..], v.len(), link);
            }
        }
    }
    while let Some(Reverse((cost, tail))) = search.heap.pop() {
        if cost > search.dist[&tail] {
            continue;
        }
        for w in &words {
            if *w == tail {
                // both parses end together: rebuild the text from its pieces
                let mut pieces = Vec::new();
                let mut t = tail.clone();
                loop {
                    let link = &search.back[&t];
                    pieces.push(link.piece.clone());
                    if link.first {
                        break;
                    }
                    t = link.from.clone();
                }
                pieces.reverse();
                println!("YES");
                println!("{}", pieces.concat());
                return;
            }
            if w.starts_with(tail.as_str()) {
                let rest = &w[tail.len()..];
                let link = Link {
                    from: tail.clone(),
                    piece: rest.to_string(),
                    first: false,
                };
                search.relax(rest, cost + rest.len(), link);
            } else if tail.starts_with(w) {
                let link = Link {
                    from: tail.clone(),
                    piece: String::new(),
                    first: false,
                };
                search.relax(&tail[w.len()..], cost, link);
            }
        }
    }
    println!("NO");
}
