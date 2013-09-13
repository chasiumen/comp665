#!/usr/bin/perl
#validate

use strict;
use warnings;

my $input;
if (@ARGV == 0)
{
	print "First name: ";
	$input = <STDIN>;
	&chkname("Firs name", $input);

	print "Last name: ";
	$input = <STDIN>;
	&chkname("Last name", $input);

	print "Zip code: ";
	$input = <STDIN>;
	&chkzip("Zip code", $input);
	
	print "Email Address:";
	$input = <STDIN>;
	&chkadd("Email Address", $input);
}

else
{
	die "usage: ./validate.pl \n";
}


sub chkname {
	if ($_[1] =~ /^[A-Z]([a-z]|[A-Z]|-)+$/ ){
		#&out;
        }
	else{
		&nerror("$_[0]");
	}
}

sub chkzip {
	if ($_[1] =~ /^(\d){5}$/){
		#&out;	
	}	
	else{
		die "$_[0] must be exactly 5 digits!\n";
	}
}

sub chkadd {
	if ($_[1] =~ /^(\d|\w|\.|-)+@(\d|\w|\.|-)+.(\d|\w|\.|-)+$/){
		#&out;
		print "Valiated!\n";
	}
	else{
		print "$_[0] must be USER\@DOMAIN, where both USER and DOMAIN must be only letters, numbers, dots, underscores, and hyphens!\n";
	}
}

sub nerror {
        die "$_[0] must start with a capital letter and contain only letters and hypens!\n";
}

#sub out{
#       print "$_[0]: $_[1]";
#}
