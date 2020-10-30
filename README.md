msmtp-setup
=========

Ansible role to install and configure [_msmtp_](https://marlam.de/msmtp/) 
on __Debian__, __CentOS__, __Ubuntu__, __Alpine__ and __Archlinux__.


Requirements
------------

None

Role Variables
--------------

<table border="1" cellpadding="4" cellspacing="0">
<thead><tr><th align="left">Key</th><th align="left">Value</th></tr></thead>
<tbody>
<tr valign="top">
<td>msmtp_global_tls_trustfile</td>
<td align="left">location of ca-certificates</td>
</tr>
<tr valign="top">
<td>msmtp_global_auth</td>
<td align="left">enable authentification for all accounts</td>
</tr>
<tr valign="top">
<td>msmtp_global_tls</td>
<td align="left">enable tls for all accounts</td>
</tr>
<tr valign="top">
<td>msmtp_global_starttls</td>
<td align="left">enable startls for all accounts</td>
</tr>
<tr valign="top">
<td>msmtp_global_log</td>
<td align="left">This can be either set to syslog (default) or to file</td>
</tr>
<tr valign="top">
<td>msmtp_global_logfile</td>
<td align="left">If logging is set to file mode, set here the location of the outputfile</td>
</tr>
<tr valign="top">
<td>msmtp_domain</td>
<td align="left">Set the argument of the SMTP EHLO (or LMTP LHLO) command</td>
</tr>
<tr valign="top">
<td>msmtp_default_account</td>
<td align="left">If no other account is specified, set the default account to be used</td>
</tr>
<tr valign="top">
<td>msmtp_alias_default</td>
<td align="left">Set the default account to be used with nonmapped usernames (see aliases)</td>
</tr>
<tr valign="top">
<td>msmtp_aliases</td>
<td align="left">The location of the aliases file (typically /etc/aliases)</td>
</tr>
</tbody>
</table>

__Account Settings__

Multiple Accounts can be configured under the _accounts_ key (see example)

<table border="1" cellpadding="4" cellspacing="0">
<thead><tr><th align="left">Key</th><th align="left">Value</th></tr></thead>
<tbody>
<tr valign="top">
<td>msmtp_account.account</td>
<td align="left">Sets the name of the account</td>
</tr>
<tr valign="top">
<td>msmtp_account.host</td>
<td align="left">Sets the name of the smtp server to be used</td>
</tr>
<tr valign="top">
<td>msmtp_account.port</td>
<td align="left">Sets the port of the smtp server to be used</td>
</tr>
<tr valign="top">
<td>msmtp_account.auth</td>
<td align="left">Enables ("on) or disables ("off") authentication. Be aware 
that the value should be quoted</td>
</tr>
<tr valign="top">
<td>msmtp_account.from</td>
<td align="left">Sets the sender e-mail address</td>
</tr>
<tr valign="top">
<td>msmtp_account.user</td>
<td align="left">Sets the username for the smtp server</td>
</tr>
<tr valign="top">
<td>msmtp_account.user</td>
<td align="left">Sets the password for the smtp server</td>
</tr>
</tbody>
</table>

__Alias Settings__

The aliases file maps Linux accounts to e-mail addresses. 
These mappings can be specified under the _aliases_ key (see example) 

<table border="1" cellpadding="4" cellspacing="0">
<thead><tr><th align="left">Key</th><th align="left">Value</th></tr></thead>
<tbody>
<tr valign="top">
<td>user</td>
<td align="left">Sets the Linux username (e.g. root)</td>
</tr>
<tr>
<td>mail</td>
<td align="left">Sets the mail account to be used with that username</td>
</tr>
</tbody>
</table>






Dependencies
------------


None

Example Playbook
----------------

Below is an example playbook. Do note that due to increased default security
for gmail, you will need to create an [application password](https://support.google.com/accounts/answer/185833?hl=en)
for usage with msmtp and also allow less secure apps.

It should be noted that gmail and icloud can change their policies 
at any time, so this is not guaranteed to work indefinitely.

```
- hosts: localhost
  remote_user: root
  roles:
    - fauch922.ansible_msmtp_setup
  vars:
    msmtp_global_tls_trustfile:
    msmtp_global_auth: "on"
    msmtp_global_tls: "on"
    msmtp_global_starttls: "on"
    msmtp_global_log: syslog
    msmtp_domain: localhost
    msmtp_default_account: gmail
    accounts:
      - account: gmail
        host: smtp.gmail.com
        port: 587
        auth: "on"
        from: example@gmail.com
        user: example@gmail.com
        password: "app-password"
      - account: icloud
        host: smtp.mail.me.com
        port: 587
        auth: "on"
        from: example@icloud.com
        user: example@icloud.com
        password: "icloud-password"
    aliases:
      - user: root
        mail: root@gmail.com
      - user: cron
        mail: cron@gmail.com
      - user: www-data
        mail: apache@gmail.com

```

License
-------

BSD

Author Information
------------------

Martin Schmid, [mscbiz@akaritech.com](mailto:mscbiz@akaritech.com)
