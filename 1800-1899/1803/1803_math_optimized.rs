use std::io::{self, BufWriter, Read, Write};

const LIMB_LIMIT: usize = 1_000_000;
const BINARY_BITS: u32 = 60;
const BINARY_BASE: u64 = 1 << BINARY_BITS;

fn fibonacci_costs(base: u64, digit_sum: impl Fn(u64) -> u32, costs: &mut [u32]) {
    let (mut previous, mut current) = (vec![1u64], vec![1u64]);
    for cost in &mut costs[2..] {
        previous.resize(current.len(), 0);
        let mut carry = 0;
        let mut sum = 0;
        for (a, &b) in previous.iter_mut().zip(&current) {
            let value = *a + b + carry;
            carry = u64::from(value >= base);
            *a = value - carry * base;
            sum += digit_sum(*a);
        }
        if carry != 0 {
            previous.push(carry);
        }
        *cost = sum + carry as u32;
        std::mem::swap(&mut previous, &mut current);
    }
}

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let mut fields = input.split_ascii_whitespace();
    let radix: usize = fields.next().unwrap().parse().unwrap();
    let count: usize = fields.next().unwrap().parse().unwrap();
    let mut costs = vec![1; count];

    if radix.is_power_of_two() {
        let bits = radix.trailing_zeros();
        // A 60-bit limb contains whole digits in bases 2, 4 and 8.
        let mask = (0..BINARY_BITS)
            .step_by(bits as usize)
            .fold(0u64, |m, i| m | (1 << i));
        fibonacci_costs(
            BINARY_BASE,
            |limb| {
                let mut sum = (limb & mask).count_ones();
                for bit in 1..bits {
                    sum += ((limb >> bit) & mask).count_ones() << bit;
                }
                sum
            },
            &mut costs,
        );
    } else {
        let mut base = 1;
        while base <= LIMB_LIMIT / radix {
            base *= radix;
        }
        // Even the loose bound of 20 digits times 9 fits in one byte.
        let mut sums = vec![0u8; base];
        for i in 1..base {
            sums[i] = sums[i / radix] + (i % radix) as u8;
        }
        fibonacci_costs(
            base as u64,
            |limb| u32::from(sums[limb as usize]),
            &mut costs,
        );
    }

    let mut order: Vec<u32> = (0..count as u32).collect();
    order.sort_unstable_by_key(|&i| (costs[i as usize], i));
    let mut output = BufWriter::new(io::stdout().lock());
    for (position, index) in order.into_iter().enumerate() {
        if position != 0 {
            output.write_all(b" ")?;
        }
        write!(output, "{}", index + 1)?;
    }
    output.write_all(b"\n")?;
    output.flush()
}
