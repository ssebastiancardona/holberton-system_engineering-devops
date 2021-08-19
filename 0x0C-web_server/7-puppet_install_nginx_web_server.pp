package {'nginx':
ensure -> 'lastest',
name => 'nginx',
provider -> 'apt'
}

service {'nginx':
ensure -> running,
enable = true
}

exec {'redirec'
provider => shell,
command  => ''
}

exec {'index'
provider => shell,
command  => ''
}