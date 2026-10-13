use std::collections::{HashMap, HashSet};
use std::io::{self, Read};

const FIELDS: usize = 3; // a given cell: its column, its row and its number

/// Pi and sigma of one number.
type Slot = (Vec<usize>, Vec<usize>);

fn permutations(k: usize) -> Vec<Vec<usize>> {
    if k == 0 {
        return vec![Vec::new()];
    }
    let mut all = Vec::new();
    for p in permutations(k - 1) {
        for pos in 0..=p.len() {
            let mut q = p.clone();
            q.insert(pos, k - 1);
            all.push(q);
        }
    }
    all
}

struct Search {
    n: usize,
    slots: Vec<Slot>,
    chosen: Vec<usize>,
    found: Vec<Vec<usize>>,
    used: Vec<Vec<HashSet<(usize, usize)>>>,
}

impl Search {
    /// The square survives block swaps exactly when each number v sits in row pi_v(J) of
    /// every block in column J and column sigma_v(I) of every block in row I, and each pair
    /// (I, J) meets all positions (pi_v(J), sigma_v(I)) once; such sets are searched.
    fn grow(&mut self, start: usize) {
        let n = self.n;
        if self.chosen.len() == n * n {
            self.found.push(self.chosen.clone());
            return;
        }
        for k in start..self.slots.len() {
            let (x, y) = self.slots[k].clone();
            let keys: Vec<(usize, usize, (usize, usize))> = (0..n)
                .flat_map(|i| (0..n).map(move |j| (i, j)))
                .map(|(i, j)| (i, j, (x[j], y[i])))
                .collect();
            if keys
                .iter()
                .any(|&(i, j, key)| self.used[i][j].contains(&key))
            {
                continue;
            }
            for &(i, j, key) in &keys {
                self.used[i][j].insert(key);
            }
            self.chosen.push(k);
            self.grow(k + 1);
            self.chosen.pop();
            for &(i, j, key) in &keys {
                self.used[i][j].remove(&key);
            }
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let n = v[0];
    let mut given = vec![(0usize, 0usize, 0usize)]; // the corner holds 0
    for g in v[2..].chunks(FIELDS) {
        given.push((g[0], g[1], g[2]));
    }
    let perms = permutations(n);
    let mut slots = Vec::new();
    for x in &perms {
        for y in &perms {
            slots.push((x.clone(), y.clone()));
        }
    }
    let mut search = Search {
        n,
        slots,
        chosen: Vec::new(),
        found: Vec::new(),
        used: vec![vec![HashSet::new(); n]; n],
    };
    search.grow(0);
    for structure in &search.found {
        // each given cell pins its number to the one slot that lands there
        let mut slot_of: HashMap<usize, usize> = HashMap::new();
        let mut number_of: HashMap<usize, usize> = HashMap::new();
        let mut fine = true;
        for &(a, b, value) in &given {
            let (j, c, i, r) = (a / n, a % n, b / n, b % n);
            let s = *structure
                .iter()
                .find(|&&t| search.slots[t].0[j] == r && search.slots[t].1[i] == c)
                .unwrap();
            if *slot_of.entry(value).or_insert(s) != s
                || *number_of.entry(s).or_insert(value) != value
            {
                fine = false;
                break;
            }
        }
        if fine {
            println!("YES");
            return;
        }
    }
    println!("NO");
}
