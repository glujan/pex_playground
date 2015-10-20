import os
import sys


def activate_pex():
    entry_point = os.environ.get('UWSGI_PEX')
    if not entry_point:
        sys.stderr.write('[pex] Could not determine pex from UWSGI_PEX.\n')
        sys.exit(1)

    sys.stderr.write('[pex] entry_point={}\n'.format('.bootstrap'))
    sys.path[0] = os.path.abspath(sys.path[0])
    sys.path.insert(0, entry_point)
    sys.path.insert(0, os.path.abspath(os.path.join(entry_point, '.bootstrap')))

    from _pex import pex_bootstrapper
    pex_bootstrapper.bootstrap_pex_env(entry_point)
    sys.stderr.write('[pex] Bootstrapping succeeded.\n')


activate_pex()
