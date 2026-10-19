use std::fmt::Write;
use std::io::{self, Read};

const SECONDS_PER_MINUTE: i32 = 60;
const SECONDS_PER_HOUR: i32 = SECONDS_PER_MINUTE * SECONDS_PER_MINUTE;
const MAX_INTERVAL: i32 = 500;

fn parse_time(text: &str) -> i32 {
    text.split(':')
        .map(|part| part.parse::<i32>().unwrap())
        .fold(0, |value, part| value * SECONDS_PER_MINUTE + part)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let take_take: i32 = tokens.next().unwrap().parse().unwrap();
    let take_land: i32 = tokens.next().unwrap().parse().unwrap();
    let land_take: i32 = tokens.next().unwrap().parse().unwrap();
    let land_land: i32 = tokens.next().unwrap().parse().unwrap();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let departures: Vec<_> = (0..n).map(|_| parse_time(tokens.next().unwrap())).collect();
    let m: usize = tokens.next().unwrap().parse().unwrap();
    let landings: Vec<_> = (0..m).map(|_| parse_time(tokens.next().unwrap())).collect();
    let (mut take_index, mut land_index) = (0, 0);
    let (mut last_take, mut last_land) = (-MAX_INTERVAL, -MAX_INTERVAL);
    let (mut take_result, mut land_result) = (Vec::new(), Vec::new());
    while take_index < n || land_index < m {
        let mut ready = 0;
        if take_index < n {
            ready = departures[take_index]
                .max(last_take + take_take)
                .max(last_land + land_take);
        }
        if land_index < m && (take_index == n || landings[land_index] <= ready) {
            last_land = landings[land_index]
                .max(last_take + take_land)
                .max(last_land + land_land);
            land_result.push(last_land);
            land_index += 1;
        } else {
            last_take = ready;
            take_result.push(last_take);
            take_index += 1;
        }
    }
    let mut output = String::new();
    for seconds in take_result.into_iter().chain(land_result) {
        let hour = seconds / SECONDS_PER_HOUR;
        let minute = seconds / SECONDS_PER_MINUTE % SECONDS_PER_MINUTE;
        let second = seconds % SECONDS_PER_MINUTE;
        writeln!(output, "{hour:02}:{minute:02}:{second:02}").unwrap();
    }
    print!("{output}");
}
