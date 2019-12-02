# The CGIPath is the URL to your Movable Type directory
CGIPath /cgi-bin/mt/

# simply remove it or comment out the line by prepending a "#".
StaticWebPath /mt-static

#================ DATABASE SETTINGS ==================
#   CHANGE setting below that refer to databases
#   you will be using.

##### MYSQL #####
ObjectDriver DBI::mysql
DBSocket /var/lib/mysql/mysql.sock
Database movabletype
DBUser movabletype
DBPassword movabletype
DBHost mysql

## Change setting to language that you want to using.
DefaultLanguage ja

## Debug Mode
DebugMode 1

#======== MAIL =======================
EmailAddressMain mt-user@example.com
MailTransfer smtp
SMTPServer mailhog
SMTPPort 1025
MailEncoding UTF-8

#======== Memcached ==================
MemcachedDriver Cache::Memcached
MemcachedNamespace MT
MemcachedServers memcached: 11211
