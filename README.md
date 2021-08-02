# test-perl-mod

country-list.jsonは以下から取得
```
curl -L -s https://datahub.io/core/country-list/r/data.json
```

mod_perl.conf
```
PerlSwitches -w
PerlSwitches -T

Alias /perl /var/www/perl
<Directory /var/www/perl>
    AddHandler perl-script .cgi .pl
    PerlResponseHandler ModPerl::PerlRun
    #PerlResponseHandler ModPerl::Registry
    PerlOptions +ParseHeaders
    Options +ExecCGI
</Directory>
```
