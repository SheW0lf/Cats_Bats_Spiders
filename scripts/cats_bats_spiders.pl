#!/usr/bin/perl

use strict;
use warnings;

for my $i (1 .. 100){
    
    if($i % 3 == 0){
        print "spiders\n" if($i % 5 == 0);
        print "cats\n";
    }
    elsif($i % 5 == 0){
        print "bats\n";
    }
    else{
        print "$i\n";
    }
}