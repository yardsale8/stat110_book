import paver
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()
import os, sys
from runestone.server import get_dburl
from sphinxcontrib import paverutils

sys.path.append(os.getcwd())

home_dir = os.getcwd()
master_url = 'http://127.0.0.1:8000'
master_app = 'runestone'
serving_dir = "./build/stat110"
dest = "../../static"

options(
    sphinx = Bunch(docroot=".",),

    build = Bunch(
        builddir="./build/stat110",
        sourcedir="_sources",
        outdir="./build/stat110",
        confdir=".",
        project_name = "stat110",
        template_args={'course_id': 'stat110',
                       'login_required':'false',
                       'appname':master_app,
                       'loglevel': 0,
                       'course_url':master_url,
                       'use_services': 'false',
                       'python3': 'true',
                       'dburl': '',
                       'basecourse': 'stat110'
                        }
    )
)

# If DBUSER etc. are in the environment override dburl
options.build.template_args['dburl'] = get_dburl(outer=locals())

from runestone import build  # build is called implicitly by the paver driver.
