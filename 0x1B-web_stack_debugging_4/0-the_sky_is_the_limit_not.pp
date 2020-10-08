# setting server to deal with many requests

exec {'fixing-nginx':
    command => "sed -i 's/15/1000/g' /etc/default/nginx",
    path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}

exec {'restarting-nginx':
    command => 'service nginx restart',
    path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}
