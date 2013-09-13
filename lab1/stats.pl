#!/usr/bin/perl
#Author: Ryosuke Morino


print "Enter a positive interger>\n";
$sum = 0;
$counter=0;
while($input = <STDIN>)
{
	
	last if ($input < 0);
	$sum = $sum+$input;
	$counter++;
	#print "[NOTICE] enter a negative number to quit\n";
}
$ave = $sum/$counter;
print "sum is $sum\n";
print "average is $ave\n";
#print "done!\n";
