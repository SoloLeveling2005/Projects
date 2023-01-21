import functools
import inspect
import os


class Router():
    def __init__(self):
        self.base_dir = os.environ.get('BASE_DIR')
        self.frontend_dir = os.environ.get('FRONTEND_DIR')
        self.data = []

    def method(self, path: str, name: str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                self.data.append(func.__name__)

                return result

            return wrapper
        return decorator

    def create_rout(self, name: str, path: str, **kwargs):
        self.data.append({f'{name}': {
            'path': path,
            # 'url_file': url_file,
        }})

    def pattern(self, url_file: str):
        print("pattern")
        last_func_name = inspect.stack()[1][3]
        if url_file[0] == "\\" or url_file[0] == "/":
            url_file = url_file[1:]
        for i in self.data:

            for key, values in i.items():
                # print(key, values)
                # print(last_func_name)
                if key == last_func_name:
                    # print(key)
                    i[key]['url_file'] = url_file
        return self.frontend_dir + url_file

    def get_urls(self):
        return self.data

# router = Router()


# rou.create_rout(url_name="index", path="/", url_file="index.html", id=0)
# rou.create_rout(url_name="main", path="/main", url_file="main.html", id=1)
# rou.create_rout(url_name="index", path="/", url_file="index.html", id=0)

# print(rou.get_urls())


# for url in rou.get_urls():
#     try:
#         if url[f'{give_me}']:
#             print(url)
#     except:
#         pass
