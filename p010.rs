
fn sum_primes_below_n(n: usize) -> usize {
    let mut primes = vec![true; n];
    primes[0] = false;
    primes[1] = false;
    let mut ind = 0;
    let mut prod = 0;
    while ind < primes.len() {
        if primes[ind] == true {
            let mut i = ind * ind;
            while i < primes.len() {
                primes[i] = false;
                i += ind;
            }
            prod += ind;
        }
        ind += 1;
    }
    prod
}

fn main() {
    println!("{}", sum_primes_below_n(2000000));
}
