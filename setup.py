from setuptools import setup

setup(
    name = 'my-test-plugin',
    version = '1.0',
    description = 'just for test the flow of write a cloudify plugin',

    author = 'xiyuqianxing',
    author_email = 'yuanguangyu1221@163.com',

    license = 'Apache License',

    packages = ['MyPlugin'],
    zip_safe = False,

    install_requires = [
        "cloudify-plugins-common",
	"cloudify-plugins-common>=3.2.1"
    ]
)



