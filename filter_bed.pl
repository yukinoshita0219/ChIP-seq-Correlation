use warnings;
use strict;

my ($sam) = @ARGV;

open (hand1, "$sam/sorted.bed") or die $!;
open (hand2, ">$sam/fragments.bed");
open (hand4, ">$sam/filtered_reads.bed");
open (hand3, ">mapped_reads.txt");

my $n;
while (<hand1>)   {

	chomp;
	
	next if /^\.\s-1/;

	my @a = split /\t/;
	my $out = "$a[0]\t$a[1]\t$a[5]\t$a[6]\t$a[7]\t$a[8]\n"; 
		if ($a[5] - $a[1] < 100 or $a[5] - $a[1] > 500 )  {
			print hand4 "$out";   }
		else {
			print hand2 "$out";
			$n ++; }
}

print hand3 "$n\n";
close hand1; close hand2;
