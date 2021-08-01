#!/usr/bin/perl

# referenced https://www.server-world.info/query?os=Ubuntu_16.04&p=httpd&f=15

use strict;
use warnings;

require HTTP::Request;

print "Content-type: text/html\n\n";
print "<html>\n<body>\n";
print "<div style=\"width:100%; font-size:40px; font-weight:bold; text-align:center;\">";

my $a = 0;
&number();

&date();

print "</div>\n</body>\n</html>";

sub number {
    $a++;
    print "number \$a = $a<br>\n";
}

sub date {
    my ($second, $minute, $hour, $mday, $month, $year) = localtime;
    printf "%02d:%02d:%02d<br>\n",$hour,$minute,$second;
}

sub request_test {
    my $request = HTTP::Request->new(GET => 'http://www.example.com/');

}
