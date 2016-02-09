from qiime.sdk.plugin import Plugin

from helloworld.functionality import hello
from helloworld.artifact_types.strang import Strang
import helloworld

plugin = Plugin(name="hello-world",
                version=helloworld.__version__,
                website="www.example.com",
                package="helloworld")

plugin.register_function("hello",
                         hello, {'name': Strang}, [('result', Strang)])
plugin.register_workflow("workflows/greetings.md")
