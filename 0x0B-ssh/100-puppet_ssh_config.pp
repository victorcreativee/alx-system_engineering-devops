# Ensure the SSH client configuration file exists and has the correct content
file { '/home/ubuntu/.ssh/config':
  ensure  => 'file',
  mode    => '0600',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => "
  Host *
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}

# Disable password authentication in the SSH server configuration
file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/sshd_config',
  line    => 'PasswordAuthentication no',
  match   => '^#PasswordAuthentication',
  notify  => Service['ssh'],
}

# Ensure SSH service is restarted after changes
service { 'ssh':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/home/ubuntu/.ssh/config'],
}

