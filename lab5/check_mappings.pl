#!/usr/bin/perl
#check DNS mapping

use warnings;
use strict;

my $foward= $ARGV[0];
my $reverse = $ARGV[1];
my @record = ();
my @domain = ();
my @addr =();
my $net;
my $IN;

if (@ARGV != 2){die "Usage: sudo ./check_mapping.pl FILE FILE"}
else {
	open($IN, "<$foward") or die "couldn't open $foward";
	while (my $line = <$IN>)
	{
		chomp($line);
		&a($line);
	}
	close($IN);


	open($IN, "<$reverse") or die "couldn't open $reverse";
	while (my $line = <$IN>)
	{
		chomp($line);
		&PTR($line);
	}
	close ($IN);
}#else ends



sub domain{
	if ($_[0] =~ /\s+SOA\s+/){
		@domain = split(/\s+/, $_[0]);
	return @domain;
	}
}

sub a {
	&domain($_[0]);
	if ($_[0] =~ /\s+A\s+/){
		@record = split(/\s+/, $_[0]);
	print "A: $record[0] $domain[0] = $record[3]\n";
	}
	#print "$_[0]\n";
}

sub addr {
    if ($_[0] =~ /\s+SOA\s+/){
        @addr = split(/\s+/, $_[0]);
		@addr = split(/\.in-addr\.arpa\./, $_[0]);
		@addr = split(/\./, $_[0]);
		$net =  join(".", reverse "$addr[0]","$addr[1]",$addr[2] ); # Hello, world
		#print "$net";
	}
}

sub PTR {
	&addr($_[0]);
	if ($_[0] =~ /\s+PTR\s+/){
		my @ptr = split(/\s+/, $_[0]);
		#print "1:$ptr[0] 2:$ptr[1] 3:$ptr[2] 4:$ptr[3]\n";
		print "$ptr[2]: $ptr[3] = $net.$ptr[0]\n";
	}

}
