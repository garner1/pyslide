# -*- coding: utf-8 -*-

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration('contour', parent_package, top_path)

    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(maintainer='Pingjun Chen',
          maintainer_email='chenpingjun@gmx.com',
          description='Contour utilities in whole slide image',
          url='https://github.com/PingjunChen/pyslide',
          license='MIT',
          **(configuration(top_path='').todict())
          )
