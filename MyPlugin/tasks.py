from cloudify import ctx
from cloudify.decorators import operation

@operation
def start(params, **kwargs) :
    pod_name = ctx.node.properties['pod_name']
    ctx.logger.info('the params is : ' .format(params))
    ctx.logger.info('The pod name is : ' .format(pod_name))

    ctx.instance.runtime_properties['pod_prop1'] = 'This should be updated now'
    ctx.instance.update()
