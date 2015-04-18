
fn nth_prime(n: usize) -> Option<usize> {
    let mut primes = [true; 125000];
    primes[0] = false;
    primes[1] = false;
    let (mut cnt, mut ind) = (0, 0);
    while ind < primes.len() {
        if primes[ind] == true {
            let mut i = ind * ind;
            while i < primes.len() {
                primes[i] = false;
                i += ind;
            }
            cnt += 1;
        }
        if cnt == n {
            return Some(ind)
        }
        ind += 1;
    }
    None
}

fn main() {
    println!("{}", nth_prime(10001).unwrap());
}
