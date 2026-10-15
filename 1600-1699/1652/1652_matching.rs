use std::collections::{BTreeMap, HashMap};
use std::io::{self, Read};

const FIELDS: usize = 3; // creditor, debtor, amount

#[derive(Clone, Copy)]
struct Debt {
    creditor: usize,
    debtor: usize,
    amount: i64,
}

struct Market {
    debts: Vec<Debt>,
    reach: HashMap<usize, usize>,
    own: HashMap<usize, Vec<usize>>,
    holder: Vec<Option<usize>>,
    seen: Vec<bool>,
    skip: Vec<usize>,
}

impl Market {
    fn unseen(&mut self, j: usize) -> usize {
        let mut root = j;
        while self.skip[root] != root {
            root = self.skip[root];
        }
        let mut j = j;
        while self.skip[j] != root {
            let next = self.skip[j];
            self.skip[j] = root;
            j = next;
        }
        root
    }

    fn try_debt(&mut self, j: usize, b: usize) -> bool {
        self.seen[j] = true;
        self.skip[j] = j + 1;
        let free = match self.holder[j] {
            None => true,
            Some(h) => self.augment(h),
        };
        if free {
            self.holder[j] = Some(b);
        }
        free
    }

    fn augment(&mut self, b: usize) -> bool {
        let own = self.own[&b].clone();
        for j in own {
            if !self.seen[j] && self.try_debt(j, b) {
                return true;
            }
        }
        let reach = self.reach[&b];
        let mut j = self.unseen(0);
        while j < reach {
            // a bank cannot hold its own debt
            if self.debts[j].debtor != b && self.try_debt(j, b) {
                return true;
            }
            j = self.unseen(j + 1);
        }
        false
    }

    fn reset(&mut self) {
        self.seen.iter_mut().for_each(|s| *s = false);
        for (j, s) in self.skip.iter_mut().enumerate() {
            *s = j;
        }
    }
}

/// a maximum matching of banks to debts of their own country: a bank keeps
/// a debt it already holds or buys one it can afford
fn most_responsible(banks: &[usize], mut debts: Vec<Debt>, money: &[i64]) -> usize {
    debts.sort_by_key(|d| d.amount);
    let nd = debts.len();
    let mut own: HashMap<usize, Vec<usize>> = banks.iter().map(|&b| (b, Vec::new())).collect();
    for (j, d) in debts.iter().enumerate() {
        if let Some(list) = own.get_mut(&d.creditor) {
            list.push(j);
        }
    }
    // the affordable prefix
    let reach = banks
        .iter()
        .map(|&b| (b, debts.partition_point(|d| d.amount <= money[b])))
        .collect();
    let (holder, seen, skip) = (vec![None; nd], vec![false; nd], (0..=nd).collect());
    let mut market = Market { debts, reach, own, holder, seen, skip };
    let mut order = banks.to_vec();
    // banks that hold a debt already go first, then the poorer ones
    order.sort_by_key(|b| (market.own[b].is_empty(), market.reach[b]));
    let mut count = 0;
    for b in order {
        // marks are cleared only after a success: when a search fails the
        // matching stays as it was, so the debts it saw still lead nowhere
        if market.augment(b) {
            count += 1;
            market.reset();
        }
    }
    count
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let nums: Vec<i64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let n = nums[0] as usize;
    let (mut country, mut money) = (vec![0i64; n], vec![0i64; n]);
    let mut banks: BTreeMap<i64, Vec<usize>> = BTreeMap::new();
    for b in 0..n {
        country[b] = nums[1 + 2 * b];
        money[b] = nums[2 + 2 * b];
        banks.entry(country[b]).or_default().push(b);
    }
    let m = nums[1 + 2 * n] as usize;
    let mut by_country: HashMap<i64, Vec<Debt>> = HashMap::new();
    for chunk in nums[2 + 2 * n..2 + 2 * n + FIELDS * m].chunks(FIELDS) {
        let (creditor, debtor) = (chunk[0] as usize - 1, chunk[1] as usize - 1);
        let d = Debt { creditor, debtor, amount: chunk[2] };
        by_country.entry(country[d.debtor]).or_default().push(d);
    }
    let total: usize = banks
        .iter()
        .map(|(c, group)| most_responsible(group, by_country.remove(c).unwrap_or_default(), &money))
        .sum();
    println!("{}", total);
}
