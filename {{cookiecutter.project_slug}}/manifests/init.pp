# Installation of initial dependencies and baseplate application
# for {{ cookiecutter.project_name }} in a development environment.
# Please add additional dependencies and env setup code as needed.
class {{ cookiecutter.project_slug }} {
  $project_path = '/home/vagrant/{{ cookiecutter.project_slug }}'

  group { 'puppet':
    ensure => 'present',
  }

  Exec { path => [ '/usr/bin', '/usr/sbin', '/bin', '/usr/local/bin' ] }

  # Add reddit package apt-repo
  exec { 'reddit-repo-add':
    command => 'sudo add-apt-repository ppa:reddit/ppa -y',
    unless  => 'apt-cache policy | grep reddit',
    notify => Exec['update-apt'],
  }

  # Update apt
  exec { 'update-apt':
    command => 'sudo apt-get update',
    refreshonly => true,
  }

  # Install the dependencies
  package {
    ['python',
     'python-dev',
     'python-pip',
     'python-gevent',
     'python-baseplate',
     'einhorn',
     {% if cookiecutter.server_type == 'pyramid' %}
     'python-pyramid',
     {% elif cookiecutter.server_type == 'thrift' %}
     'thrift',
     {%- endif %}
    ]:
      ensure  => installed,
      require => [
        Exec['reddit-repo-add'], # add reddit repo for baseplate and einhorn
        Exec['update-apt'],      # The system update needs to run
      ],
      notify  => Exec['install-app'],
  }

  # Set up the app
  exec { 'install-app':
    cwd     => $project_path,
    command => 'python setup.py develop',
  }
}

include {{ cookiecutter.project_slug }}
