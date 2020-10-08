# setting server to deal with many requests

exec {'fix--for-nginx':
    command => "sed -i 's/15/1000/g' /etc/default/nginx",
    path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}

exec {'arestart-nginx':
    command => 'service nginx restart',
    path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}
