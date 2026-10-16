use std::fmt::Write as _;
use std::io::{self, Read};

const STEPS: usize = 100;

struct Bars {
    mass: Vec<f64>,
    purity: Vec<f64>,
    order: Vec<usize>,
}

impl Bars {
    // gold, in grams times a thousand, in the first t grams of the bars laid
    // out from the poorest to the richest
    fn gold_before(&self, mut t: f64) -> f64 {
        let mut gold = 0.0;
        for &i in &self.order {
            let part = self.mass[i].min(t);
            if part <= 0.0 {
                break;
            }
            gold += part * self.purity[i];
            t -= part;
        }
        gold
    }

    fn window(&self, s: f64, need: f64) -> f64 {
        self.gold_before(s + need) - self.gold_before(s)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace().map(|w| w.parse::<f64>().unwrap());
    let mut next = || words.next().unwrap();
    let (n, need, fineness) = (next() as usize, next(), next());
    let mut bars = Bars { mass: vec![0.0; n], purity: vec![0.0; n], order: (0..n).collect() };
    for i in 0..n {
        bars.mass[i] = next();
        bars.purity[i] = next();
    }
    let purity = bars.purity.clone();
    bars.order.sort_by(|&a, &b| purity[a].partial_cmp(&purity[b]).unwrap());
    let total: f64 = bars.mass.iter().sum();
    let target = need * fineness;
    // a window of the needed weight sliding from the poorest end to the
    // richest gains gold steadily, so it hits the target if anything does
    if total < need
        || bars.window(0.0, need) > target
        || bars.window(total - need, need) < target
    {
        println!("NO");
        return;
    }
    let (mut low, mut high) = (0.0, total - need);
    for _ in 0..STEPS {
        let mid = (low + high) / 2.0;
        if bars.window(mid, need) < target {
            low = mid;
        } else {
            high = mid;
        }
    }
    let start = (low + high) / 2.0;
    let mut take = vec![0.0; n];
    let mut left = 0.0;
    for &i in &bars.order {
        let right = left + bars.mass[i];
        take[i] = (right.min(start + need) - f64::max(left, start)).max(0.0);
        left = right;
    }
    let mut out = String::from("YES\n");
    for x in &take {
        writeln!(out, "{:.10}", x).unwrap();
    }
    print!("{}", out);
}
