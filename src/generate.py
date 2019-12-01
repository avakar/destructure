#!/usr/bin/env python3

import argparse
import os
import sys

_templ = '''\
	else if constexpr (has_n_members_v<T, {i}>)
	{{
		auto && [{m}] = std::forward<T>(t);
		return std::tie({m});
	}}
'''

def _main():
    top, _ = os.path.split(__file__)

    ap = argparse.ArgumentParser()
    ap.add_argument('--output', '-o', type=argparse.FileType('w'), default='-')
    ap.add_argument('--count', '-n', type=int, default=64)
    ap.add_argument('--input', type=argparse.FileType('r'),
        default=os.path.join(top, 'destructure.h.in'))
    ap.add_argument('--inline', action='store_true')
    args = ap.parse_args()

    input = args.input.read()
    out_chunks = []
    for i in range(args.count - 1, 0, -1):
        chunk = _templ.format(i=i, m=', '.join(f'm{x}' for x in range(i)))
        out_chunks.append(chunk)

    args.output.write(input
        .replace('${inline}', 'inline ' if args.inline else '')
        .replace('${count}', str(args.count))
        .replace('${here}', ''.join(out_chunks))
        )
    return 0

if __name__ == '__main__':
    sys.exit(_main())
