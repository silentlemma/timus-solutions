use std::io::{self, Read};

const PERFECT: usize = 0;
const GREAT: usize = 1;
const GOOD: usize = 2;
const BOO: usize = 3;
const MISS: usize = 4;
const MARKS: usize = 5;
const NAMES: [&str; MARKS] = ["Perfect", "Great", "Good", "Boo", "Miss"];
const SCORE: [i64; MARKS] = [10, 5, 0, 0, 0]; // p
const COMBO: [i64; MARKS] = [55, 33, 0, 0, 0]; // q
const DANCE: [i64; MARKS] = [2, 1, 0, -4, -5]; // dance points
const BASE_SCORE: i64 = 1_000_000;
const PERCENT: i64 = 100;
// level bonuses: share of the most dance points needed, in percent
const SHARES: [(i64, i64); 3] = [(80, 100_000), (64, 10_000), (50, 1_000)];
const ALL_PERFECT: i64 = 10_000_000;
const ALL_GREAT: i64 = 1_000_000;
const LOW: i64 = 100;
const SLOWEST: i64 = 1000; // ms per beat on Easy, halved on each harder level
const TENTHS: i64 = 10;
const PERFECT_TENTHS: i64 = 4; // under 40 % of the period
const GREAT_TENTHS: i64 = 7; // under 70 %
const LEVELS: [&str; 3] = ["Easy", "Medium", "Hard"];
const SEPARATOR: &str = "--------------------";
const HEADER: usize = 3; // tokens before the log: duration, level, beats

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let tokens: Vec<&str> = s.split_ascii_whitespace().collect();
    let index = LEVELS.iter().position(|&l| l == tokens[1]).unwrap();
    let (diff, period) = (index as i64 + 1, SLOWEST >> index);
    let beats = tokens[2].as_bytes();
    let mut log: Vec<(i64, u8)> = tokens[HEADER..]
        .chunks(2)
        .filter(|c| c.len() == 2)
        .map(|c| (c[0].parse().unwrap(), c[1].as_bytes()[0]))
        .collect();
    log.sort();
    let steps = beats.iter().filter(|&&b| b != b'N').count() as i64;
    let unit = diff * BASE_SCORE / (steps * (steps + 1) / 2); // B div S
    let mut counts = [0i64; MARKS];
    let (mut stage, mut combo_bonus, mut run, mut n, mut points) = (0i64, 0i64, 0i64, 0i64, 0i64);
    let mut went_negative = false;
    let mut k = 0; // the first logged press not before the current beat
    for (i, &beat) in beats.iter().enumerate() {
        let start = i as i64 * period;
        let end = start + period;
        while k < log.len() && log[k].0 < start {
            k += 1;
        }
        if beat == b'N' {
            continue;
        }
        n += 1;
        // only the first press within the beat counts
        let mark = if k == log.len() || log[k].0 >= end {
            BOO
        } else if log[k].1 != beat {
            MISS
        } else {
            let elapsed = log[k].0 - start;
            if TENTHS * elapsed < PERFECT_TENTHS * period {
                PERFECT
            } else if TENTHS * elapsed < GREAT_TENTHS * period {
                GREAT
            } else {
                GOOD
            }
        };
        counts[mark] += 1;
        stage += SCORE[mark] * n * unit;
        run = if mark <= GOOD { run + 1 } else { 0 };
        combo_bonus += COMBO[mark] * run;
        points += DANCE[mark];
        went_negative = went_negative || points < 0;
    }
    let most = DANCE[PERFECT] * steps;
    let bonus = if went_negative {
        0
    } else if counts[PERFECT] == steps {
        ALL_PERFECT
    } else if counts[PERFECT] + counts[GREAT] == steps {
        ALL_GREAT
    } else {
        SHARES
            .iter()
            .find(|&&(share, _)| PERCENT * points >= share * most)
            .map_or(LOW, |&(_, b)| b)
    };
    let mut out = String::new();
    for (name, c) in NAMES.iter().zip(counts.iter()) {
        out += &format!("{}: {}\n", name, c);
    }
    out += &format!("{}\n", SEPARATOR);
    out += &format!("Stage Score: {}\nCombo Bonus: {}\n", stage, combo_bonus);
    out += &format!(
        "Dance Level Bonus: {}\nTotal Score: {}\n",
        bonus,
        stage + combo_bonus + bonus
    );
    print!("{}", out);
}
