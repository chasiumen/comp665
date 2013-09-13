#!/usr/bin/perl
#Author: Ryosuke Morino
#get_external_ip

use warnings;
use strict;


my $home = $ENV{"HOME"};
my $file = "$home/perl/index.html";
my $regex = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}';


if (@ARGV == 0)
{
	#&clean("$file");
	`wget -q -P $home/perl/ "http://checkmyip.com"`;
	open(my $IN, "<$file") or die "couldn't open $file";

	while(my $line = <$IN>)
	{
		if($line =~ /$regex/ )
		{
			my @words = split(/>|</, $line);
			print "Your IP is $words[4]\n";
			&clean("$file");
			last;
		}
	}
}
else
{
	die "Usage: ./get_external_ip.pl";
}


sub clean{
	if( -e $_[0])
	{
		unlink $_[0];	
	}
}
