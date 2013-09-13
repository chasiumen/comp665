#!/usr/bin/perl

use warnings;
use strict;
my $file = "/etc/dhcp/dhcpd.conf";
my $regex_ip = '^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$';
my $regex_mac = '^([0-9A-F]{2}[:]){5}([0-9A-F]{2})$';
my @host =();
my @mac =();
my @ip =();

if (@ARGV != 0)
{
	die "Usage: sudo ./get_addr";
}
else
{
	open(my $IN, "<$file") or die "couldn't open $file";
	while(my $line = <$IN>)
	{
		
		chomp($line);
		&f_host($line);
		&f_macadd($line);
		&f_ipadd($line);
	}
    #check size of the array
    if ($#host != $#mac or $#mac != $#ip)
    {
        die "ERROR: Check Array size"
    }
    else
    {
        #output
    	for (my $i=0; $i<=($#host); $i++ )
    	{
    		print "$host[$i] $mac[$i] $ip[$i] \n";
    	}
    }   
}


#find hostname
sub f_host{
	if($_[0] =~ /host/i)
	{
		#print $_[0];
		my @words = split(/host/i, $_[0]);
		@words = split(/{/, $words[1] );
		&chopper($words[0]);
	#	print "$words[0] ";
		push(@host, $words[0]);
		return @host;
	}
	

}
#find MAC address
sub f_macadd{
	if($_[0] =~ /hardware ethernet/i)
	{
	#	print "$_[0]\n";
		my @words = split(/hardware\s+ethernet/i, $_[0]);
        #       print "slashed: $words[1]\n";
		@words = split(/;/, $words[1] );
		&chopper($words[0]);
		#check mac reguex
		if ($words[0] =~ /$regex_mac/i)
		{
			#print "$words[0] ";
			push(@mac, $words[0]);
			return @mac;
		}
		else
		{
			print "Not Valid MAC address\n";
		}
	}
}
#find IP address
sub f_ipadd{
	if($_[0] =~ /fixed-address/i)
	{
		my @words = split(/fixed-address/i, $_[0]);
		@words = split(/;/, $words[1] );
		&chopper($words[0]);
	        
		if ($words[0] =~ /$regex_ip/)
                {
                        #print "$words[0] ";
			push(@ip, $words[0]);
			return @ip;
                }
                else
                {
                        print "Not Valid IP address\n";
                }
	}
}

#take out all space
sub chopper{
	        $_[0] =~ s/^\s*//;
                $_[0] =~ s/\s*$//;
	}

