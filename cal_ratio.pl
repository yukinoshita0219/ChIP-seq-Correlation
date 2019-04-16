use strict;
use warnings; 
use Number::Format qw(round);
my $file=$ENV{"File_name"};

print "$file\n";

open (hand0, "$file/stats.txt") or die "cannot find mapped_reads.txt\n";
open (hand1, ">$file/ratio.txt");
 
my $scale_factor;
while (<hand0>)    {
chomp;
	if (/^\s+([0-9]+).+aligned concordantly exactly 1 time/)  {
		
		my $n = $1; 
		print "$n\n";
		$scale_factor=round(1000000/$n, 3);
		print hand1 "$scale_factor\n";

}   }
close hand0;
close hand1;

