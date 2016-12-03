import argparse
import sys
# print(sys.argv)
from optparse import OptionParser

def optParserWay() :
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
    parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

    (options, args) = parser.parse_args()

    print(options)
    # print(args)

optParserWay()


def getOptWay() :
    import getopt
    args = '-a -b -cfoo -d bar a1 a2'.split()

    args
    ['-a', '-b', '-cfoo', '-d', 'bar', 'a1', 'a2']

    optlist, args = getopt.getopt(args, 'abc:d:')
    [('-a', ''), ('-b', ''), ('-c', 'foo'), ('-d', 'bar')]






def not_sure() :
    parser = argparse.ArgumentParser(description='Application description')
    parser.add_argument("somearg")
    # parser.add_argument('-c', help='Perform crawling process', required=False)
    args = vars(parser.parse_args())

    print(args)


