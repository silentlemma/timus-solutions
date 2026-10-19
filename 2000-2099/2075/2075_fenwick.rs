use std::collections::HashMap;
use std::io::{self, Read, Write};

const ENDLESS: i64 = 1 << 62;

// layers in order of names (the densest at the bottom), with a Fenwick tree of heights
struct Glass {
    tree: Vec<i64>,
    height: Vec<i64>,
    top: usize,
    total: i64,
    straw: i64,
    clock: i64,
    sips: Vec<(i64, i64, usize)>, // neighbours of one liqueur merged
}

impl Glass {
    fn add(&mut self, i: usize, delta: i64) {
        self.height[i] += delta;
        self.total += delta;
        let mut j = i + 1;
        while j < self.tree.len() {
            self.tree[j] += delta;
            j += j & j.wrapping_neg();
        }
    }

    // the layer that contains level h, and how much of it lies above h
    fn layer_at(&self, mut h: i64) -> (usize, i64) {
        let m = self.height.len();
        let (mut pos, mut step) = (0, self.top);
        while step > 0 {
            if pos + step <= m && self.tree[pos + step] <= h {
                pos += step;
                h -= self.tree[pos];
            }
            step >>= 1;
        }
        (pos, self.height[pos] - h)
    }

    fn drink(&mut self, mut amount: i64) {
        while amount > 0 && self.total > self.straw {
            let (layer, above) = self.layer_at(self.straw);
            let take = above.min(amount);
            self.add(layer, -take);
            amount -= take;
            let clock = self.clock;
            match self.sips.last_mut() {
                Some(last) if last.2 == layer && last.1 == clock => last.1 = clock + take,
                _ => self.sips.push((clock, clock + take, layer)),
            }
            self.clock += take;
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.lines();
    let n: usize = lines.next().unwrap().trim().parse().unwrap();
    let events: Vec<Vec<&str>> =
        (0..n).map(|_| lines.next().unwrap().split_whitespace().collect()).collect();
    let mut names: Vec<&str> =
        events.iter().map(|e| e[1]).filter(|&w| w != "Oleg" && w != "fire").collect();
    names.sort_unstable();
    names.dedup();
    let index: HashMap<&str, usize> = names.iter().enumerate().map(|(i, &s)| (s, i)).collect();
    let m = names.len();
    let mut top = 1;
    while top * 2 <= m {
        top *= 2;
    }
    let mut glass = Glass {
        tree: vec![0; m + 1],
        height: vec![0; m],
        top,
        total: 0,
        straw: 0,
        clock: 0,
        sips: Vec::new(),
    };
    let mut drinking = false;
    for e in &events {
        let t: i64 = e[0].parse().unwrap();
        if drinking {
            glass.drink(t - glass.clock);
            // running dry before this moment stops him; running dry exactly now does not
            // matter: a pour lets him go on, and Oleg or fire set the state anyway
            drinking = glass.clock == t;
        }
        glass.clock = t;
        match e[1] {
            "Oleg" => {
                glass.straw = e[2].parse().unwrap();
                drinking = true;
            }
            "fire" => drinking = false,
            name => glass.add(index[name], e[2].parse().unwrap()),
        }
    }
    if drinking {
        glass.drink(ENDLESS);
    }
    let mut out = String::new();
    for &(from, to, layer) in &glass.sips {
        out.push_str(&format!("{}-{} {}\n", from, to, names[layer]));
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
