use std::io::{self, Read};

const DIGIT_COUNT: usize = 4;
const HEX_BASE: usize = 16;
const DIGIT_BITS: usize = 4;
const DIGIT_MASK: usize = HEX_BASE - 1;
const PAIR_DOMAIN: usize = HEX_BASE * HEX_BASE;
const TRIPLE_DOMAIN: usize = PAIR_DOMAIN * HEX_BASE;
const PAIR_GROUPS: usize = DIGIT_COUNT * (DIGIT_COUNT - 1) / 2;

fn distance_histogram(numbers: &[usize]) -> [i64; DIGIT_COUNT] {
    let mut singles = vec![vec![0_i32; HEX_BASE]; DIGIT_COUNT];
    let mut pairs = vec![vec![0_i32; PAIR_DOMAIN]; PAIR_GROUPS];
    let mut triples = vec![vec![0_i32; TRIPLE_DOMAIN]; DIGIT_COUNT];
    let (mut single_pairs, mut double_pairs, mut triple_pairs) = (0_i64, 0_i64, 0_i64);
    for &number in numbers {
        let first = number >> (DIGIT_BITS * (DIGIT_COUNT - 1));
        let second = (number >> (2 * DIGIT_BITS)) & DIGIT_MASK;
        let third = (number >> DIGIT_BITS) & DIGIT_MASK;
        let fourth = number & DIGIT_MASK;
        let single_keys = [first, second, third, fourth];
        for (index, &key) in single_keys.iter().enumerate() {
            single_pairs += i64::from(singles[index][key]);
            singles[index][key] += 1;
        }
        let pair_keys = [
            number >> (2 * DIGIT_BITS),
            first * HEX_BASE + third,
            first * HEX_BASE + fourth,
            (number >> DIGIT_BITS) & (PAIR_DOMAIN - 1),
            second * HEX_BASE + fourth,
            number & (PAIR_DOMAIN - 1),
        ];
        for (index, &key) in pair_keys.iter().enumerate() {
            double_pairs += i64::from(pairs[index][key]);
            pairs[index][key] += 1;
        }
        let triple_keys = [
            number >> DIGIT_BITS,
            (number >> (2 * DIGIT_BITS)) * HEX_BASE + fourth,
            first * PAIR_DOMAIN + (number & (PAIR_DOMAIN - 1)),
            number & (TRIPLE_DOMAIN - 1),
        ];
        for (index, &key) in triple_keys.iter().enumerate() {
            triple_pairs += i64::from(triples[index][key]);
            triples[index][key] += 1;
        }
    }
    let count = numbers.len() as i64;
    let distance_one = triple_pairs;
    let distance_two = double_pairs - (DIGIT_COUNT - 1) as i64 * distance_one;
    let distance_three = single_pairs - 2 * distance_two - (DIGIT_COUNT - 1) as i64 * distance_one;
    let distance_four = count * (count - 1) / 2 - distance_one - distance_two - distance_three;
    [distance_one, distance_two, distance_three, distance_four]
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut tokens = text.split_whitespace();
    let count = tokens.next().unwrap().parse::<usize>().unwrap();
    let numbers: Vec<usize> = (0..count)
        .map(|_| usize::from_str_radix(tokens.next().unwrap(), HEX_BASE as u32).unwrap())
        .collect();
    let answer = distance_histogram(&numbers);
    println!(
        "{}",
        answer
            .iter()
            .map(|value| value.to_string())
            .collect::<Vec<_>>()
            .join(" ")
    );
}
