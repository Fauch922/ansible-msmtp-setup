from pathlib import Path

msmtrpc_filename = Path("/etc/msmtprc")
aliases_filename = Path("/etc/aliases")
ubuntu_id_filename = Path("/etc/lsb-release")
redhat_id_filename = Path("/etc/redhat-release")


def test_msmtprc():

    with open(msmtrpc_filename, 'r') as file:
        for line in file:
            if line.startswith("aliases"):
                assert ("/etc/aliases" in line)
                global aliases_filename
                aliases_filename = line.split(" ")[1]
            if line.startswith("auth"):
                assert ("on" in line)
            if line.startswith("tls "):
                assert ("on" in line)
            if line.startswith("logfile"):
                assert ("~/.msmtp.log" in line)
            if line.startswith("account") and ":" not in line:
                assert ("gmail" in line or "icloud" in line)
            if line.startswith("host"):
                assert ("smtp.gmail.com" in line or "smtp.mail.me.com")
            if line.startswith("port"):
                assert ("587" in line)
            if line.startswith("from"):
                assert ("example@icloud.com" in line or "example@gmail.com" in line)
            if line.startswith("user"):
                assert ("example@icloud.com" in line or "example@gmail.com" in line)
            if line.startswith("password"):
                assert ("app-password" in line or "icloud-password" in line)
            if line.startswith("tls_trust_file"):
                if Path(redhat_id_filename).is_file():
                    assert ("/etc/pki/tls/certs/ca-bundle.crt" in line)
                else:
                    assert ("/etc/ssl/certs/ca-certificates.crt" in line)


def test_aliases():

    with open(aliases_filename, 'r') as file:
        for line in file:
            if line.startswith("root:"):
                assert("root@gmail.com" in line)
            if line.startswith("cron"):
                assert("cron@gmail.com" in line)
            if line.startswith("www-data"):
                assert("apache@gmail.com" in line)
            if line.startswith("default"):
                assert ("exampleaccount" in line)



