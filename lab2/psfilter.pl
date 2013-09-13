#!/usr/bin/perl
#Author: Ryosuke Morino
#Description: ps filter

use warnings;
use strict;

if (@ARGV == 1)
{
	while (my $input = <STDIN>)
	{
		if ($input =~ /^$ARGV[0]/)
		{
			my @words = split(/\s+/, $input);
			print "$words[1]";
            		my $num = @words-1;
          		for ( my $i=7; $i<=$num; $i++ )
			{
				print " $words[$i]";
				if ($i == $num)
				{
					print "\n";	
				}
			}
		}
	}
}
elsif (@ARGV == 0)
{
	while (my $input = <STDIN>)
        {
		if($input =~ /^morinor/ )
		{
                        my @words = split(/\s+/, $input);
                        print "$words[1]";
			my $num = @words-1;
                        for ( my $i=7; $i<=$num; $i++ )
                        {
                                print " $words[$i]";
                                if ($i == $num)
                                {
                                        print "\n";
                                }
                        }


		}
        }
}

else
{
	die "Error! Usage: psfilter.pl [username]\n";
}

