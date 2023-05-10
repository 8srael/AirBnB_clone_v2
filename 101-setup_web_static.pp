# Do Task 0 using puppet

# Update and upgrade packages
exec { 'update packages':
  command => 'apt-get -y update',
}

exec { 'upgrade packages':
  command => 'apt-get -y upgrade',
}

# Install Nginx
package {'nginx':
  ensure => installed,
}

# Create directories and index file
file { '/data/web_static/releases/test':
  ensure => 'directory',
  mode   => '0755',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/shared':
  ensure => 'directory',
  mode   => '0755',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => 'This is a test\n',
  mode    => '0644',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Create symbolic link and set ownership

file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => [
    File['/data/web_static/releases/test'],
    File['/data/web_static/shared'],
    File['/data/web_static/releases/test/index.html'],
  ],
}

# Configure Ngin

file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => "
    server {
	listen 80 default_server;
	listen [::]:80 default_server;
	location /hbnb_static/ {
	    alias /data/web_static/current/;
	}
    }
  ",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Restart Nginx

service {'nginx':
  ensure  => running,
  enable  => true,
  require => [
    File['/etc/nginx/sites-available/default'],
    File['/data/web_static/current'],
  ],
}
