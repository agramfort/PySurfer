# Author: Alexandre Gramfort <gramfort@nmr.mgh.harvard.edu>
# License: BSD Style.

import os
import os.path as op


def get_subjects_dir(path='.'):
    """Get path to local copy of fsaverage reconstruction

    If SUBJECTS_DIR environment variable is not set, the
    fsaverage data are automatically downloaded.

    Parameters
    ----------
    path : string
        Location of where to look for the fsaverage dataset.
        If not set. The data will be automatically downloaded in
        the local folder.
    """
    if 'SUBJECTS_DIR' in os.environ:
        print "Looking for subjects in: %s" % os.environ['SUBJECTS_DIR']
        return os.environ['SUBJECTS_DIR']

    archive_name = "fsaverage.tar.gz"
    url = "https://surfer.nmr.mgh.harvard.edu/ftp/data/" + archive_name
    folder_name = "fsaverage"

    if not os.path.exists(op.join(path, folder_name)):
        if not os.path.exists(archive_name):
            import urllib
            print "Downloading data, please Wait (140 MB)..."
            print url
            opener = urllib.urlopen(url)
            open(archive_name, 'wb').write(opener.read())
            print

        import tarfile
        print "Decompressiong the archive: " + archive_name
        tarfile.open(archive_name, "r:gz").extractall(path=path)
        print

    os.environ['SUBJECTS_DIR'] = path
    print "Looking for subjects in: %s" % os.environ['SUBJECTS_DIR']
    return path
