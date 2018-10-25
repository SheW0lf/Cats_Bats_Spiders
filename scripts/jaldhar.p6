#!/usr/bin/env perl6
#
# Author: Jaldhar H. Vyas
# Language: Perl6
# Github: https://github.com/jaldhar

for 1 .. 100 {
    say $_ % 15 ?? $_ % 5 ?? $_ % 3 ?? $_ !! "cats" !! "bats" !! "spiders";
}
