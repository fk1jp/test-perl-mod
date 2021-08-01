#!/usr/bin/perl

# referenced https://neos21.net/blog/2019/02/02-01.html
# referenced https://stackoverflow.com/questions/15653419/parsing-json-file-using-perl/15653474

use strict;
use warnings;

use lib qw( ..);

use JSON qw( );

require HTTP::Request;

my @queryPairs = split('&', $ENV{'QUERY_STRING'});
my %formData;
my $code = '';

foreach my $queryPair (@queryPairs) {
  my ($name, $value) = split('=', $queryPair);
  $value =~ tr/+/ /;
  $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
  if ( $name eq 'code')
  {
    $code = $value;
  }
  $formData{$name} = $value;
}

print "Content-type: text/html\n\n";
print "<html>\n<body>\n";
print "<div style=\"width:100%; font-size:40px; font-weight:bold; text-align:center;\">";


&cities();

print "</div>\n</body>\n</html>";

sub cities {
    #my $filename = './country-list.json';
    my $filename = '/var/www/perl/country-list.json';
    my $json_text = do {
	open(my $json_fh, "<:encoding(UTF-8)", $filename)
	    or die("Can't open \$filename\": $!\n");
	local $/;
	<$json_fh>
    };

    my $json = JSON->new;
    my $data = $json->decode($json_text);

    my $counter = 0;
    for ( @$data )
    {
        if ( $code eq $_->{Code} )
        {
            print "country code \"".$_->{Code}."\" is ".$_->{Name}."\n";
	    $counter++;
        }
    }
    if ( $counter == 0 )
    {
        print "Not match country code $code<BR>";
        print "use query string like \"/open-file.cgi?code=JP\"<BR>";
        print "this is sample of country code<BR>";
	print "<table>";
	print "<tr><td>Code</td><td>Name</td></tr>";
	for ( @$data )
	{
		print "<tr><td>".$_->{Code}."</td><td>".$_->{Name}."</td></tr>"
	}
        print "</table>";
    }
}
