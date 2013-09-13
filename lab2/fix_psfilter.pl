#!/usr/bin/perl
#Author: Ryosuke Morino
#Description: ps filter

use strict;
use warnings;


my $reg = "$ARGV[0]";
if (@ARGV == 1)
{

	while (my $input = <STDIN>)
	{
		if ($input =~ /^$reg/)
		{
			my @words = split(/\s+/, $input);
			print "$words[1] $words[7]\n";
		}
	}

}
elsif (@ARGV == 0)
{
	while (my $input = <STDIN>)
        {
                        my @words = split(/\s+/, $input);
                        print "$words[1] $words[7]\n";
        }

}

else
{
	die "Error! Usage: psfilter.pl [username]\n";
}
