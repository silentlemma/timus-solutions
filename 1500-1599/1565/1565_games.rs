use std::io::{self, Read};

const SHOOTERS: usize = 3;
const INDEX_SUM: usize = 0 + 1 + 2;
const EPS: f64 = 1e-12; // survival chances closer than this count as equal

type Chances = [f64; SHOOTERS];

struct Truel {
    acc: [f64; SHOOTERS],
    order: [usize; SHOOTERS],
}

impl Truel {
    /// The most accurate living opponent of all three; the earlier one on a tie.
    fn strongest(&self, shooter: usize) -> usize {
        let mut best = usize::MAX;
        for i in 0..SHOOTERS {
            if i != shooter && (best == usize::MAX || self.acc[i] > self.acc[best]) {
                best = i;
            }
        }
        best
    }

    /// Two left, first to shoot: first wins p / (p + q - p q).
    fn duel(&self, first: usize, second: usize) -> Chances {
        let (p, q) = (self.acc[first], self.acc[second]);
        let mut c = [0.0; SHOOTERS];
        c[first] = p / (p + q - p * q);
        c[second] = 1.0 - c[first];
        c
    }

    /// The duel left after a hit, with the next living shooter first.
    fn after_hit(&self, turn: usize, killed: usize) -> Chances {
        let mut first = self.order[(turn + 1) % SHOOTERS];
        if first == killed {
            first = self.order[(turn + 2) % SHOOTERS];
        }
        self.duel(first, INDEX_SUM - killed - first)
    }

    /// Chances when all three live and order[turn] shoots; A never misses,
    /// so the shooting stops at A's turn at the latest.
    fn three(&self, turn: usize) -> Chances {
        let shooter = self.order[turn];
        if shooter == 0 {
            return self.after_hit(turn, self.strongest(shooter));
        }
        let p = self.acc[shooter];
        let miss = self.three((turn + 1) % SHOOTERS);
        // the outcome of a shot at each target, None for the air
        let mut outcomes: Vec<(Option<usize>, Chances)> = vec![(None, miss)];
        for target in (0..SHOOTERS).filter(|&t| t != shooter) {
            let hit = self.after_hit(turn, target);
            let mut mixed = [0.0; SHOOTERS];
            for i in 0..SHOOTERS {
                mixed[i] = p * hit[i] + (1.0 - p) * miss[i];
            }
            outcomes.push((Some(target), mixed));
        }
        let best = outcomes
            .iter()
            .map(|o| o.1[shooter])
            .fold(f64::MIN, f64::max);
        // on a tie the strongest opponent is shot, then A, B, C, then the air
        let mut preference: Vec<Option<usize>> = vec![Some(self.strongest(shooter))];
        preference.extend((0..SHOOTERS).map(Some));
        preference.push(None);
        for choice in preference {
            if let Some(o) = outcomes.iter().find(|o| o.0 == choice) {
                if o.1[shooter] >= best - EPS {
                    return o.1;
                }
            }
        }
        miss
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let values: Vec<f64> = text
        .split_ascii_whitespace()
        .map(|w| w.parse().unwrap())
        .collect();
    let mut truel = Truel {
        acc: [values[0], values[1], values[2]],
        order: [0; SHOOTERS],
    };
    let mut total = [0.0; SHOOTERS];
    let mut orders = 0;
    for a in 0..SHOOTERS {
        for b in (0..SHOOTERS).filter(|&b| b != a) {
            truel.order = [a, b, INDEX_SUM - a - b];
            let c = truel.three(0);
            for i in 0..SHOOTERS {
                total[i] += c[i];
            }
            orders += 1;
        }
    }
    let share = 1.0 / orders as f64;
    println!(
        "{:.5} {:.5} {:.5}",
        total[0] * share,
        total[1] * share,
        total[2] * share
    );
}
