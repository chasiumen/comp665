#!/usr/bin/perl
#Author: Ryosuke Morino
#Description: Calculator

if (@ARGV != 3)
{
	die "Error! Usage: ./calc.pl NUM OPERATION NUM\n";
}

$num1 = $ARGV[0]; 
$num2 = $ARGV[2];
$op = $ARGV[1];

if ($op eq "plus")
{
	$result = $num1 + $num2;
	#print "$num1 + $num2 = $result\n";
	print "$num1 plus $num2 is $result\n";
}
elsif ($op eq "minus")
{
	$result = $num1 - $num2;
	#print "$num1 - $num2 = $result\n";
	print "$num1 minus $num2 is $result\n";	
}
elsif ($op eq "times")
{
	$result = $num1 * $num2;
	#print "$num1 * $num2 = $result\n";
	print "$num1 times $num2 is $result\n";
	
}
elsif ($op eq "over")
{
	$result = $num1 / $num2;
	#print "$num1 / $num2 = $result\n";
	print "$num1 over $num2 is $result\n";
}
elsif ($op eq "pow")
{
	$result = $num1 ** $num2;
	#print "$num1 ^ $num2 = $result\n";
	print "$num1 pow $num2 is $result\n";

}
else
{
	die "unacceptable operation!\n"
}

#print "done!\n";

