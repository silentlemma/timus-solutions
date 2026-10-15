use std::collections::{BTreeMap, HashMap};
use std::fmt::Write as _;
use std::io::{self, Read};

/// a max tree over cities: the best total, how many leaves reach it, and
/// one of them
struct Tree {
    size: usize,
    best: Vec<i64>,
    count: Vec<usize>,
    at: Vec<usize>,
}

impl Tree {
    fn new(cities: usize) -> Tree {
        let size = cities.next_power_of_two();
        let (best, count, at) = (vec![0; 2 * size], vec![1; 2 * size], vec![0; 2 * size]);
        let mut tree = Tree { size, best, count, at };
        for c in 0..size {
            tree.at[size + c] = c;
        }
        for i in (1..size).rev() {
            tree.count[i] = tree.count[2 * i] + tree.count[2 * i + 1];
            tree.at[i] = tree.at[2 * i];
        }
        tree
    }

    fn add(&mut self, city: usize, amount: i64) {
        let mut i = city + self.size;
        self.best[i] += amount;
        i /= 2;
        while i > 0 {
            let (a, b) = (2 * i, 2 * i + 1);
            if self.best[a] != self.best[b] {
                let w = if self.best[a] > self.best[b] { a } else { b };
                self.best[i] = self.best[w];
                self.count[i] = self.count[w];
                self.at[i] = self.at[w];
            } else {
                self.best[i] = self.best[a];
                self.count[i] = self.count[a] + self.count[b];
                self.at[i] = self.at[a];
            }
            i /= 2;
        }
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let people: Vec<(&str, &str, i64)> = (0..n)
        .map(|_| {
            let (who, city) = (words.next().unwrap(), words.next().unwrap());
            (who, city, words.next().unwrap().parse().unwrap())
        })
        .collect();
    let m: usize = words.next().unwrap().parse().unwrap();
    let k: usize = words.next().unwrap().parse().unwrap();
    let moves: Vec<(usize, &str, &str)> = (0..k)
        .map(|_| {
            let day = words.next().unwrap().parse().unwrap();
            (day, words.next().unwrap(), words.next().unwrap())
        })
        .collect();
    let mut city_id: HashMap<&str, usize> = HashMap::new();
    let mut city_name: Vec<&str> = Vec::new();
    for &c in people.iter().map(|p| &p.1).chain(moves.iter().map(|mv| &mv.2)) {
        if !city_id.contains_key(c) {
            city_id.insert(c, city_name.len());
            city_name.push(c);
        }
    }
    let mut tree = Tree::new(city_name.len());
    let mut home: HashMap<&str, (usize, i64)> = HashMap::new();
    for &(who, city, money) in &people {
        home.insert(who, (city_id[city], money));
        tree.add(city_id[city], money);
    }
    let mut days = vec![0usize; city_name.len()];
    let mut today = 1;
    for i in 0..=k {
        // the moves of a day count from the next morning
        let until = if i < k { moves[i].0 + 1 } else { m + 1 };
        if until > today && tree.count[1] == 1 {
            days[tree.at[1]] += until - today; // a strict leader only
        }
        today = today.max(until);
        if i == k {
            break;
        }
        let (_, who, to) = moves[i];
        let (from, money) = home[who];
        tree.add(from, -money);
        tree.add(city_id[to], money);
        home.insert(who, (city_id[to], money));
    }
    let answer: BTreeMap<&str, usize> =
        (0..city_name.len()).filter(|&c| days[c] > 0).map(|c| (city_name[c], days[c])).collect();
    let mut out = String::new();
    for (c, d) in answer {
        writeln!(out, "{} {}", c, d).unwrap();
    }
    print!("{}", out);
}
