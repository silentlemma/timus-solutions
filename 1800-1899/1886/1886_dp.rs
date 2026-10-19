use std::io::{self, Read};

const PERCENT: f64 = 100.0;
const FIELDS: usize = 6;
// positions of the fields of a flight
const DURATION: usize = 3;
const CHANCE: usize = 4;
const DELAY: usize = 5;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input.split_ascii_whitespace().map(|t| t.parse().unwrap()).collect();
    let (n, m) = (v[0] as usize, v[1] as usize);
    let mut flights: Vec<&[i64]> = v[2..2 + FIELDS * m].chunks(FIELDS).collect();
    // per airport, over the flights seen so far (latest first): departure
    // times, and the best expected arrival over the flights leaving at that
    // time or later
    let mut departs: Vec<Vec<i64>> = vec![Vec::new(); n + 1];
    let mut best: Vec<Vec<f64>> = vec![Vec::new(); n + 1];
    // the best expected arrival for someone at airport a at this time
    let expected = |departs: &Vec<Vec<i64>>, best: &Vec<Vec<f64>>, a: usize, time: i64| -> f64 {
        if a == n {
            return time as f64;
        }
        let k = departs[a].partition_point(|&t| t >= time);
        if k > 0 {
            best[a][k - 1]
        } else {
            f64::INFINITY
        }
    };
    // an arrival is always later than the departure, so taking flights from
    // the latest departure down sees every flight a connection could use
    flights.sort_by(|x, y| y[2].cmp(&x[2]));
    for x in flights {
        let (a, b, t, f) = (x[0] as usize, x[1] as usize, x[2], x[DURATION]);
        let (p, d) = (x[CHANCE] as f64, x[DELAY]);
        let on_time = expected(&departs, &best, b, t + f);
        let delayed = expected(&departs, &best, b, t + f + d);
        let mut value = ((PERCENT - p) * on_time + p * delayed) / PERCENT;
        if let Some(&last) = best[a].last() {
            value = value.min(last);
        }
        departs[a].push(t);
        best[a].push(value);
    }
    let answer = expected(&departs, &best, 1, 0);
    if answer.is_infinite() {
        println!("Fail");
    } else {
        println!("{:.6}", answer);
    }
}
