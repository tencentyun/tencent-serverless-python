import os
import io
import setuptools

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', os.linesep)
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

def read_requirements(req='requirements.txt'):
    content = read(os.path.join(req))
    return [line for line in content.split(os.linesep)
            if not line.strip().startswith('#')]

setuptools.setup(
    name='tencentserverless',
    version='0.1.3',
    keywords='scf',
    description='This is callFunction for SCF.',
    long_description_content_type='text/markdown',
    long_description=io.open(
        os.path.join(
            os.path.dirname(__file__),
            'README.md'
        ), encoding='utf-8'
    ).read(),
    author='Tencent Cloud',
    author_email='qcloud_middleware@qq.com',
    url='https://github.com/alanoluo/tencent-serverless-python.git',
    packages=setuptools.find_packages(),
    install_requires=read_requirements('requirements.txt'),
    license='Apache License 2.0'
)