python=$(which python)
if [ -z $python ]; then
    apt update; apt install -y python
fi
pip install flask
su -c "
if [ -z $(grep 'siga' /system/etc/hosts) ]; then
    mount -o remount,rw /system
    echo '127.0.0.1        m.siga.ufpe.br' >> /system/etc/hosts
fi
/data/data/com.termux/files/usr/bin/python siga.py \"$1\"
"