#Author: aashbaugh16
#Language: Perl
#Github: aashbaugh16
for ($i=1; $i <= 100; $i++){
	if($i%3 eq 0 && $i%5 eq 0){
	print "spiders ";
	}
	elsif($i%3 eq 0){
	print "cats ";
	}
	elsif($i%5 eq 0){
	print "bats ";
	} 
	else{
	print "$i "
	}
}
$y =<STDIN>
