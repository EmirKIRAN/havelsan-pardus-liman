import subprocess
import argparse

parser = argparse.ArgumentParser(description="Packege process")
parser.add_argument("pname", help="Package name you want to search", type=str)
parser.add_argument("-c","--count", help="number of packages installed on the system", action="store_true", default=False)

def packageCount():

    output  = subprocess.Popen(["apt","list"], stdout=subprocess.PIPE)
    data = str(list(output.communicate())[0]).split('\\n')[1:-1]
    return str(len(data)) + " packages installed on the system ..."

def isAvailablePackage(package_name):

    output = subprocess.Popen(["apt", "list"], stdout=subprocess.PIPE)

    data = str(list(output.communicate())[0]).split('\\n')[1:]
    packages = [x.split('/')[0] for x in data]
    flag = False

    for pack in packages:
        for item in pack.split('-'):
            if item == package_name:
                flag=True

    if flag:
        return 'The package installed on the system !'
    else:
        return 'The package is not installed on the system !'


if __name__ == '__main__':

    outputs = list()

    args = parser.parse_args()
    outputs.append(isAvailablePackage(args.pname))
    if args.count:
        outputs.append(packageCount())


    for o in outputs:
        print(o)

