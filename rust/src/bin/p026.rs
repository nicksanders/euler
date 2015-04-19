
extern crate num;
use num::bigint::ToBigUint;


fn prime_sieve(mut limit: usize) -> Vec<bool> {
    if limit % 2 != 0 {
        limit += 1;
    }
    let mut sieve = vec![true; limit];
    sieve[0] = false; sieve[1] = false;
    let mut i = 0;
    while i < sieve.len() {
        if sieve[i] == true {
            let mut j = i * i;
            while j < sieve.len() {
                sieve[j] = false;
                j += i;
            }
        }
        i += 1;
    }
    sieve
}


fn primes(limit: usize) -> Vec<usize> {
    prime_sieve(limit).iter().enumerate().filter(|&(_, v)| *v == true).map(|(i, _)| i).collect()
}


fn main() {

    let mut res = 0;
    let limit = 1000;
    let mut period: usize;

    for d in primes(limit).iter().rev() {
        res = *d;
        period = 1;
        while num::pow(10.to_biguint().unwrap(), period) % d.to_biguint().unwrap() != 1.to_biguint().unwrap() {
            period += 1;
        }
        if d - 1 == period {
            break;
        }
    }

    println!("{}", res);

}
