#!/usr/bin/perl

#use warnings;
#use strict;
my @save;
while (chomp(my $in = <STDIN>)){
	
	print "Original: $in\n";
	push(@save, $in);

}

print "@save [end] [$#save+1]\n";

