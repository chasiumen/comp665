#!/usr/bin/perl
#midterm takehome test 1
use warnings;
use strict;

if (@ARGV != 0){
	die "This script does not take any arugemtns\n";
}
else{

	my @array=(); #storage
	my $count = 0; #loop counter
	my $total = 0; #total wc
	my $wc =0; #word counter
	while(my $in = <STDIN>){
		#print "Original: $in \n";
		last if ($in eq "\cD");
		chomp($in);
		my @words =  split(/\s+/, $in);
		$wc += $#words + 1;
		#print $wc;	
		$count++;
	}
#print "Words:$wc  Line:$count\n";
my $ave = $wc/$count;
print "There were $wc words total.\n";
print "There was an average of $ave words per line.\n";
}#else ends
