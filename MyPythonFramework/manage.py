import argparse
import os
import settings.settings


print('Для остановки приложения нажмите Ctrl+C')
parser = argparse.ArgumentParser(exit_on_error=False)
# print(parser.parse_args())
parser.add_argument("code", help="increase output verbosity")
# args = parser.parse_args()
# if args.code == "runserver":
#     os.system("color 02 & cd settings & python main.py")

args, unknown_args = parser.parse_known_args()
# print(args.code)
# print(unknown_args[0])
if args.code == "runserver":
    os.system("color 02 & cd basic & python main.py")
elif args.code == "create-app":
    os.system("color 02 & ")



# def two():
#     print('two')
#     parser = argparse.ArgumentParser(exit_on_error=False)
#     parser.add_argument('-create-app', '--blog', help="Best blog name here.")
#     # args = parser.parse_args()
#     # print(args.blog)
#     args, unknown_args = parser.parse_known_args()
#     print(args, unknown_args)


# except SystemExit as e:
#     two()
