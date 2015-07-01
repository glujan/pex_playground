import subprocess
import os

from pybuilder.core import use_plugin, init, task, description, depends

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "pex_playground"
default_task = "generate_pex"
version = '0.1'


@init
def set_properties(project):
    project.depends_on_requirements("requirements.txt")
    project.build_depends_on_requirements("requirements-dev.txt")


@task
@depends('publish')
@description('Generates PEX file')
def generate_pex(project, logger):
    dir_dist = project.get_property('dir_dist').replace(
        '$dir_target', project.get_property('dir_target'))
    dir_build = os.path.join(dir_dist, 'dist')

    pex_args = ' '.join([
        '{name}',
        '--requirement=requirements.txt',
        '--find-links={dir_build}',
        '--entry-point={name}:main',
        '--output-file={name}.pex',
    ]).format(name=name, dir_build=dir_build)

    logger.info('Generating "%s.pex"', name)
    command = 'pex {args}'.format(args=pex_args)
    subprocess.call(command, shell=True)
