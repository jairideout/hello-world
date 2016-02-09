from setuptools import find_packages, setup

setup(name='helloworld',
      version='0.0.1',
      packages=find_packages(),
      install_requires=[
          'qiime >= 2.0.0'
      ],
      package_data={
          'helloworld': ['workflows/*.md']
      },
      entry_points={
        'qiime.plugin': ['helloworld=helloworld.plugin_setup:plugin']
      })
