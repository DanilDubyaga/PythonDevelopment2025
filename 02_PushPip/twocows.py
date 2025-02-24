from cowsay import cowsay, list_cows
import argparse


def get_preset(args):
    return (
            args.y or args.w or args.t or args.s
            or args.p or args.g or args.d or args.b
    )


parser = argparse.ArgumentParser(
    description="Generates an ASCII image of a cow saying the given text",
)

parser.add_argument(
    "-e",
    type=str,
    help="An eye string. This is ignored if a preset mode is given",
    dest="eyes1",
    default="oo",
    metavar="eye_string1",
)

parser.add_argument(
    "-E",
    type=str,
    help="An eye string. This is ignored if a preset mode is given",
    dest="eyes2",
    default="oo",
    metavar="eye_string2",
)

parser.add_argument(
    "-f", type=str, metavar="cowfile1",
    help="Either the name of a cow specified in the COWPATH, "
         "or a path to a cowfile (if provided as a path, the path must "
         "contain at least one path separator)",
)

parser.add_argument(
    "-F", type=str, metavar="cowfile2",
    help="Either the name of a cow specified in the COWPATH, "
         "or a path to a cowfile (if provided as a path, the path must "
         "contain at least one path separator)",
)

parser.add_argument(
    "-l", action="store_true",
    help="Lists all cows in the cow path and exits"
)
parser.add_argument(
    "-n", action="store_false",
    help="If given, text in the speech bubble of cow1 will not be wrapped"
)
parser.add_argument(
    "-N", action="store_false",
    help="If given, text in the speech bubble of cow2 will not be wrapped"
)
parser.add_argument(
    "-T", type=str, dest="tongue",
    help="A tongue string. This is ignored if a preset mode is given",
    default="  ", metavar="tongue_string"
)
parser.add_argument(
    "-W", type=int, default=40, dest="width", metavar="column",
    help="Width in characters to wrap the speech bubble (default 40)",
)

group = parser.add_argument_group(
    title="Mode",
    description="There are several out of the box modes "
                "which change the appearance of the cow. "
                "If multiple modes are given, the one furthest "
                "down this list is selected"
)
group.add_argument("-b", action="store_const", const="b", help="Borg")
group.add_argument("-d", action="store_const", const="d", help="dead")
group.add_argument("-g", action="store_const", const="g", help="greedy")
group.add_argument("-p", action="store_const", const="p", help="paranoid")
group.add_argument("-s", action="store_const", const="s", help="stoned")
group.add_argument("-t", action="store_const", const="t", help="tired")
group.add_argument("-w", action="store_const", const="w", help="wired")
group.add_argument("-y", action="store_const", const="y", help="young")

parser.add_argument(
    "--random", action="store_true",
    help="If provided, picks a random cow from the COWPATH. "
         "Is superseded by the -f option",
)

parser.add_argument(
    "message1", default=None, nargs='?',
    help="The message to include in the speech bubble of cow1. "
         "If not given, stdin is used instead."
)
parser.add_argument(
    "message2", default=None, nargs='?',
    help="The message to include in the speech bubble of cow2. "
         "If not given, stdin is used instead."
)
args = parser.parse_args()

if args.l:
    print("\n".join(list_cows()))
else:

    cow1 = cowsay(message=args.message1,
                  cow=args.f or "default",
                  preset=get_preset(args),
                  eyes=args.eyes1,
                  tongue=args.tongue,
                  width=args.width,
                  wrap_text=args.n)

    cow2 = cowsay(message=args.message2,
                  cow=args.F or "default",
                  preset=get_preset(args),
                  eyes=args.eyes2,
                  tongue=args.tongue,
                  width=args.width,
                  wrap_text=args.N)

    cow1 = cow1.split('\n')
    cow2 = cow2.split('\n')
    l1 = len(cow1)
    l2 = len(cow2)
    width = max([len(s) for s in cow1])

    if l1 < l2:
        cow1 = ["" for i in range(l2-l1)] + cow1
    else:
        cow2 = ["" for i in range(l1 - l2)] + cow2
    ans = "\n".join([cow1[i]+" "*(width-len(cow1[i])) + cow2[i] for i in range(max(l1, l2))])
    print(ans)