use std::io::{self, Read};

const NEVER: i32 = 1 << 30;

#[derive(Clone, Copy, PartialEq)]
enum Spell {
    Bolt,
    Heal,
    Teleport(usize),
}

struct Battle {
    n: usize,
    hp_hero: i32,
    hp_monster: i32,
    speed: usize,
    heal: i32,
    bolt: Vec<i32>,
    // need[m][h][p] is the fewest hit points the hero needs at the start of
    // a turn with m mana against a pack of h hit points on square p; more
    // hit points never hurt, so this number decides every state
    need: Vec<Vec<Vec<i32>>>,
}

impl Battle {
    // where the monsters stop after moving from square p
    fn land(&self, p: usize) -> usize {
        if p - 1 < self.speed {
            1
        } else {
            p - self.speed
        }
    }

    // the damage of a pack with h hit points that ends its move on p
    fn strike(&self, h: i32, p: usize) -> i32 {
        if p == 1 {
            (h + self.hp_monster - 1) / self.hp_monster
        } else {
            0
        }
    }

    // the hit points a spell needs with m mana against h hit points on p
    fn cost(&self, m: usize, mut h: i32, mut p: usize, spell: Spell) -> i32 {
        let mut cure = 0;
        match spell {
            Spell::Bolt => {
                if h <= self.bolt[p] {
                    return 1;
                }
                h -= self.bolt[p];
            }
            Spell::Heal => cure = self.heal,
            Spell::Teleport(to) => p = to,
        }
        let q = self.land(p);
        let rest = self.need[m - 1][h as usize][q];
        if rest == NEVER {
            return NEVER;
        }
        let req = self.strike(h, q) + rest;
        if cure == 0 {
            req
        } else if req > self.hp_hero {
            NEVER
        } else {
            (req - cure).max(1)
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i32> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let mut it = v.iter().copied();
    let mut next = || it.next().unwrap();
    let (n, hp_hero, mana, hp_monster) = (next() as usize, next(), next() as usize, next());
    let (count, speed, heal) = (next(), next() as usize, next());
    let mut bolt = vec![0];
    bolt.extend((0..n).map(|_| next()));
    let top = (count * hp_monster) as usize;
    let mut b = Battle {
        n,
        hp_hero,
        hp_monster,
        speed,
        heal,
        bolt,
        need: vec![vec![vec![NEVER; n + 1]; top + 1]; mana + 1],
    };
    let mut spells = vec![Spell::Bolt, Spell::Heal];
    spells.extend((1..=b.n).map(Spell::Teleport));
    for m in 1..=mana {
        for h in 1..=top {
            for p in 1..=n {
                let best = spells
                    .iter()
                    .map(|&s| b.cost(m, h as i32, p, s))
                    .min()
                    .unwrap();
                b.need[m][h][p] = best;
            }
        }
    }
    let (mut hp, mut h, mut p) = (hp_hero, top as i32, n);
    if b.need[mana][top][n] > hp {
        println!("DEFEATED");
        return;
    }
    let mut out = String::from("VICTORIOUS\n");
    // replay: any spell whose need the hero meets keeps the win in reach
    let mut m = mana;
    while h > 0 {
        let s = *spells.iter().find(|&&s| b.cost(m, h, p, s) <= hp).unwrap();
        match s {
            Spell::Bolt => {
                out.push_str("L\n");
                h -= b.bolt[p];
            }
            Spell::Heal => {
                out.push_str("H\n");
                hp = hp_hero.min(hp + b.heal);
            }
            Spell::Teleport(to) => {
                out.push_str(&format!("T {}\n", to));
                p = to;
            }
        }
        if h > 0 {
            p = b.land(p);
            hp -= b.strike(h, p);
        }
        m -= 1;
    }
    print!("{}", out);
}
