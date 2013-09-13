#!/usr/bin/perl
#Author: Ryosuke Morino
#

if (@ARGV != 3)
{
	die "usage: print_lines.pl start_line stop_line file\n";
}

$start = $ARGV[0];
$end = $ARGV[1];
$file = $ARGV[2];

if ( $end < $start )
{
	die "start_line must be <= to stop_line\n";
}

else
{
open($IN, "<$file") or die "couldn't open $file";
$count = 1;
	while($line = <$IN>)
	{
		if ($count >= $start and $count <= $end )
		{
			chomp($line);
			print "[$line]\n";
			$count++;		
		}
		else
		{
			$count++;
		}
	}
	if ($count < $start or  $count < $end)
	{
		$count = $count - 1;
		print "ran out of lines, stopping at line $count\n";
	}
close ($IN);
}

