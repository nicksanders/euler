
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

fn main() {

    let mut result = [0, 0, 0];
    let sieve = prime_sieve(100000);
    let mut a: isize = -999;

    while a < 1000 {
        let mut b: isize = -999;
        while b < 1000 {
            let mut n = 0;
            loop {
                let p = ((n * n) + (a * n) + b).abs() as usize;
                if sieve[p] == false {
                    break;
                }
                if n > result[0] {
                    result = [n, a, b];
                }
                n += 1;
            }
            b += 1;
        }
        a += 1;
    }

    println!("{:?} {}", result, result[1] * result[2]);

}
