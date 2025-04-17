"""
static methods

methods that don't use the self parameter(work at class level)

decorators allow us to wrap another function in order to extend the behiavor
 of the wrapped function, without permanently modifying it
"""
class student:
  @staticmethod
  def college():
    print("ABC College")

