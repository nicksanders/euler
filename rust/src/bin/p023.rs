
fn sum_proper_divisors(n: usize) -> usize {
    let mut s = 1;
    let end = (n as f64).sqrt() as usize;
    for i in (2..end + 1) {
        if n % i == 0 {
            s += i;
            if i != n / i {s += n / i;}
        }
    }
    s
}

fn get_abundants(max: usize) -> Vec<usize> {
    let mut abundants = vec![];
    for i in (12..max + 1) {
        if i < sum_proper_divisors(i) {
            abundants.push(i)
        }
    }
    abundants
}

fn main() {

    let limit = 28123;
    let mut sieve = vec![false; limit];

    let abundants = get_abundants(limit);

    for i in (0..abundants.len()) {
        for j in (i..abundants.len()) {
            if abundants[i] + abundants[j] >= limit {
                break;
            }
            sieve[abundants[i] + abundants[j]] = true;
        }
    }

    println!("{}", sieve.iter().enumerate().filter(|&(_, v)| *v == false).fold(0, |acc, (i, _)| acc + i));

}
