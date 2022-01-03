from django import template

register = template.Library()


@register.filter(name="testCut")
def testCut(value, args):
    """
    This cuts out all values of "args" from the string!
    """

    return value.replace(args, '')


# register.filter('testCut', testCut)
