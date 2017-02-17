from setuptools import setup

setup(name="cwl2zshcomp",
      version="0.1",
      description='Generating ZSH completionos from CWL tool descriptions',
      author='Fabian Klötzl',
      author_email='fabian-cwl2zshcomp@kloetzl.info',
      url='https://github.com/kloetzl/cwl2zshcomp',
      install_requires=['jinja2', 'pyyaml'],
      entry_points={
          'console_scripts': [
              'cwl2zshcomp = cwl2zshcomp.main:main'
          ]
      },
      packages=['cwl2zshcomp'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Operating System :: POSIX',
          'Intended Audience :: Developers',
          'Environment :: Console',
          'License :: OSI Approved :: Apache Software License',
      ],
      include_package_data=True,
      )
