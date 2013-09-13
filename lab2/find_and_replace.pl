#!/usr/bin/perl
#Author: Ryosuke Morino
#find_and_replace.pl

use warnings;


$infile = $ARGV[0];
$outfile = $ARGV[1];

if (@ARGV == 4)
{
open($IN, "<$infile") or die "couldn't open $infile";
open($OUT, ">$outfile") or die "couldn't open $outfile";

	while($line = <$IN>)
	{
		#s/REGEX/REPLACEMENT/MOD
		if( $line =~ s/$ARGV[2]/$ARGV[3]/gi )
		{
			#print "$line";
			print $OUT "$line";
		}
	}
close($OUT);
close($IN);	
}
else
{
	die "usage: find_and_replace.pl input_file output_file current new\n";
}
