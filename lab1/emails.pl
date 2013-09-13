#!/usr/bin/perl
#Author: Ryosuke Morino

#delimiter set
$d = ';';

if (@ARGV != 1)
{
	die "Error! Usage: ./emails.pl email_list\n"	
}

$file = $ARGV[0];

open($IN, "<$file") or die "couldn't open $file\n";

while($line = <$IN>)
{
	@contact = $line;
	
#	print "@contact";
	chomp($line);
	@contact= split(/$d/, $line);
	$str = join(" ", "\"$contact[2] $contact[1]\" <$contact[0]>");

	print "$str\n";

}
close ($IN);
