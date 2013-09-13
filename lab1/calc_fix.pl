#!/usr/bin/perl


print "Calculor program\n";
print "Enter a integer>";
$num1 = <STDIN>;
chomp($num1);
print "Type of operation: plus/minus/times/over/pow >";
$op = <STDIN>;
chomp($op);
print "Enter another integer>";
$num2 = <STDIN>;
chomp($num2);
print "Calculating...\n"; 


if ($op eq "plus")
{
	$result = $num1 + $num2;
	print "$num1 + $num2 = $result\n";
}
elsif ($op eq "minus")
{
	$result = $num1 - $num2;
	print "$num1 - $num2 = $result\n";
}
elsif ($op eq "times")
{
	$result = $num1 * $num2;
	print "$num1 * $num2 = $result\n";
}
elsif ($op eq "over")
{
	$result = $num1 / $num2;
	print "$num1 / $num2 = $result\n";
}
elsif ($op eq "pow")
{
	$result = $num1 ** $num2;
	print "$num1 ^ $num2 = $result\n";
}
else
{
	die "unacceptable operation!\n"
}

print "done!";

