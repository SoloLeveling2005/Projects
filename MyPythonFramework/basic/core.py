import inspect
import os
import sys
import importlib.util
from router import Router

sys.path.append(os.environ.get('BASE_DIR') + "/django_app")
sys.path.append(os.environ.get('BASE_DIR') + "/basic")
sys.path.append(os.environ.get('BASE_DIR'))


class Core:

    def __init__(self):
        self.apps = os.environ.get('APPS').split(" ")
        self.base_dir = os.environ.get('BASE_DIR')
        self.mass_routers = []
        self.mass_var = []

    def new_controller(self):
        for app in self.apps:
            spec = importlib.util.spec_from_file_location(f"{app}.router", self.base_dir + f"{app}/router.py")
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            self.mass_var = vars(module).values()

            # Iterate through the classes defined in the module
            for obj in inspect.getmembers(module, inspect.isclass):
                if obj[1].__subclasses__():
                    class_ = obj[1].__subclasses__()[0]
                    my_class = getattr(module, class_.__name__)
                    class_new = my_class()
                    # print(class_new.data)  # [{'index': {'path': '/'}}]
                    # class_new.index()

                    func_name = class_new.data[0].keys()
                    print(class_new.data)
                    self.mass_routers = class_new.data

                    for route in self.mass_routers:
                        print(route)
                        for key, values in route.items():
                            print(key)
                            method = getattr(class_new, key)
                            method()


main_core = Core()
main_core.new_controller()
