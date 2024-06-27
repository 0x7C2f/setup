# Installing pihole
# https://wiki.archlinux.org/title/Pi-hole?useskin=timeless#Failed_to_start_Pi-hole_FTLDNS_engine

# install:
pi-hole-server

nano /etc/systemd/resolved.conf.d/pi-hole.conf

```
[Resolve]
DNSStubListener=no
```
sudo pacman -S php-sqlite

nano /etc/php/php.ini

[...]
extension=pdo_sqlite
[...]
extension=sockets
[...]
extension=sqlite3
[...]


Install lighttpd and php-cgi.

cp /usr/share/pihole/configs/lighttpd.example.conf /etc/lighttpd/lighttpd.conf

Enable lighttpd.service and start it.



# Optimize for SSD
/etc/pihole/pihole-FTL.conf

...

## Database Interval
## How often do we store queries in FTL's database -minutes-?
## See: https://docs.pi-hole.net/ftldns/database/
## Options: number of minutes
DBINTERVAL=60.0

...

