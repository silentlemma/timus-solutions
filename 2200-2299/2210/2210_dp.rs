use std::io::{self, Read};

const MAX_VALUE: usize = 100;
const UNREACHABLE: i64 = -1;

#[derive(Clone, Copy)]
struct Line {
    slope: i64,
    intercept: i64,
}

impl Line {
    fn value(self, day: i64) -> i64 {
        self.slope * day + self.intercept
    }
}

struct Rich {
    day: usize,
    income: i64,
    money: i64,
}

fn make_hull(mut lines: Vec<Line>) -> Vec<Line> {
    lines.sort_unstable_by_key(|line| (line.slope, line.intercept));
    let mut hull: Vec<Line> = Vec::new();
    for line in lines {
        if hull.last().map(|last| last.slope) == Some(line.slope) {
            if hull.last().unwrap().intercept >= line.intercept {
                continue;
            }
            hull.pop();
        }
        while hull.len() >= 2 {
            let a = hull[hull.len() - 2];
            let b = hull[hull.len() - 1];
            if (a.intercept - b.intercept) * (line.slope - b.slope)
                < (b.intercept - line.intercept) * (b.slope - a.slope)
            {
                break;
            }
            hull.pop();
        }
        hull.push(line);
    }
    hull
}

fn maximum(hull: &[Line], day: i64) -> i64 {
    let mut left = 0;
    let mut right = hull.len() - 1;
    while left < right {
        let middle = (left + right) / 2;
        if hull[middle].value(day) <= hull[middle + 1].value(day) {
            left = middle + 1;
        } else {
            right = middle;
        }
    }
    hull[left].value(day)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut data = input
        .split_whitespace()
        .map(|token| token.parse::<usize>().unwrap());
    let count = data.next().unwrap();
    let mut best = [0; MAX_VALUE + 1];
    for _ in 0..count {
        let cost = data.next().unwrap();
        best[cost] = best[cost].max(data.next().unwrap());
    }
    let mut options = Vec::new();
    let mut peak = 0;
    for (cost, &income) in best.iter().enumerate().skip(1) {
        if income > peak {
            peak = income;
            options.push((cost, peak));
        }
    }
    let (cap, top_income) = *options.last().unwrap();
    let length = cap + 1;
    let state_count = cap + 2 * top_income + 1;
    let mut current = vec![UNREACHABLE; state_count];
    current[0] = 0;
    let mut work_events = Vec::new();
    let mut rich = Vec::new();
    let mut day = 0;
    while current.iter().any(|&money| money >= 0) {
        let mut following = vec![UNREACHABLE; state_count];
        let mut events = Vec::new();
        let mut greatest = UNREACHABLE;
        for income in (0..state_count).rev() {
            let money = current[income];
            if money <= greatest {
                continue;
            }
            greatest = money;
            if income >= cap && money >= cap as i64 {
                rich.push(Rich {
                    day,
                    income: income as i64,
                    money,
                });
                continue;
            }
            let slope = (income + 1) as i64;
            events.push(Line {
                slope,
                intercept: money - slope * day as i64,
            });
            // Move any affordable purchase before the next work day.
            if money < cap as i64 {
                following[income] = following[income].max(money + income as i64 + 1);
            }
            for &(cost, extra) in &options {
                if cost as i64 > money {
                    break;
                }
                let target = income + extra;
                following[target] = following[target].max(money - cost as i64 + income as i64);
            }
        }
        work_events.push(events);
        current = following;
        day += 1;
    }
    let limit = work_events.len() - 1 + length;
    let mut suffix = vec![0; limit + 1];
    for remaining in 0..limit {
        let mut gain = 1;
        for &(cost, income) in &options {
            gain = gain.max(income as i64 * remaining as i64 - cost as i64);
        }
        suffix[remaining + 1] = suffix[remaining] + gain;
    }
    let correction = suffix[length] - top_income as i64 * length as i64 * (length - 1) as i64 / 2
        + cap as i64 * length as i64;
    let mut answers = vec![0; limit + 1];
    let mut work_best: Vec<Option<i64>> = vec![None; state_count];
    for horizon in 0..=limit {
        if horizon < work_events.len() {
            for line in &work_events[horizon] {
                let previous = &mut work_best[line.slope as usize];
                if previous.map_or(true, |value| line.intercept > value) {
                    *previous = Some(line.intercept);
                }
            }
        }
        for (slope, &intercept) in work_best.iter().enumerate() {
            if let Some(intercept) = intercept {
                answers[horizon] = answers[horizon].max(slope as i64 * horizon as i64 + intercept);
            }
        }
    }
    let mut lines = Vec::new();
    for state in rich {
        for remaining in 0..=limit - state.day {
            let horizon = state.day + remaining;
            let candidate = state.money + state.income * remaining as i64 + suffix[remaining];
            answers[horizon] = answers[horizon].max(candidate);
        }
        let start = state.day as i64;
        let slope = state.income - top_income as i64 * start;
        let intercept =
            state.money - state.income * start + top_income as i64 * start * (start + 1) / 2;
        lines.push(Line {
            slope,
            intercept: intercept + cap as i64 * start + correction,
        });
    }
    let rich_hull = make_hull(lines);
    let work_hull = make_hull(
        work_best
            .iter()
            .enumerate()
            .filter_map(|(slope, &intercept)| {
                intercept.map(|intercept| Line {
                    slope: slope as i64,
                    intercept,
                })
            })
            .collect(),
    );
    let count = data.next().unwrap();
    let mut output = String::new();
    for _ in 0..count {
        let horizon = data.next().unwrap() as i64;
        let answer = if horizon <= limit as i64 {
            answers[horizon as usize]
        } else {
            let common = top_income as i64 * horizon * (horizon - 1) / 2 - cap as i64 * horizon;
            maximum(&work_hull, horizon).max(common + maximum(&rich_hull, horizon))
        };
        output.push_str(&answer.to_string());
        output.push('\n');
    }
    print!("{output}");
}
