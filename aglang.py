#!/usr/bin/env python3.6

# TODO: use grep if ag not available
# TODO: python 2.7, 3.0

import argparse
import os.path
import subprocess
from typing import List


def get_dirs(lang: str) -> List[List[str]]:
    # TODO: make wrapper.  preserve dirss as class variable.
    if False:  # Just for consistency of `elif`
        raise RuntimeError('Unreachable.')
    elif lang == 'bmake':
        dirss = [
            [  # 0
            ],
            [  # 1
                '~/src/netbsd/src/Makefile',
            ],
            [  # 2
                # recently updated Makefiles in netbsd-src
                '~/src/netbsd/src/crypto/external/bsd/openssh/bin/ssh/Makefile',
                '~/src/netbsd/src/crypto/external/bsd/openssh/lib/Makefile',
                '~/src/netbsd/src/crypto/external/bsd/openssh/lib/Makefile',
                '~/src/netbsd/src/distrib/amd64/installimage/Makefile',
                '~/src/netbsd/src/distrib/amd64/uefi-installimage/Makefile',
                '~/src/netbsd/src/distrib/evbarm/instkernel/ramdisk/Makefile',
                '~/src/netbsd/src/distrib/i386/installimage/Makefile',
                '~/src/netbsd/src/distrib/sparc64/cdroms/installcd/Makefile',
                '~/src/netbsd/src/etc/mtree/Makefile',
                '~/src/netbsd/src/external/bsd/acpica/bin/iasl/Makefile',
                '~/src/netbsd/src/external/bsd/dhcpcd/dist/src/Makefile',
                '~/src/netbsd/src/external/bsd/dhcpcd/dist/tests/crypt/Makefile',
                '~/src/netbsd/src/external/bsd/dhcpcd/sbin/dhcpcd/Makefile',
                '~/src/netbsd/src/external/bsd/dhcpcd/sbin/dhcpcd/Makefile',
                '~/src/netbsd/src/external/bsd/libproc/lib/Makefile',
                '~/src/netbsd/src/external/cddl/dtracetoolkit/dist/Makefile',
                '~/src/netbsd/src/external/cddl/dtracetoolkit/Makefile',
                '~/src/netbsd/src/external/cddl/Makefile',
                '~/src/netbsd/src/external/gpl3/gcc.old/lib/libstdc++-v3/Makefile',
                '~/src/netbsd/src/external/gpl3/gcc.old/usr.bin/backend/Makefile',
                '~/src/netbsd/src/external/gpl3/gcc.old/usr.bin/include/Makefile',
                '~/src/netbsd/src/external/gpl3/gcc.old/usr.bin/include/Makefile',
                '~/src/netbsd/src/external/gpl3/gcc/usr.bin/backend/Makefile',
                '~/src/netbsd/src/external/gpl3/gcc/usr.bin/backend/Makefile',
                '~/src/netbsd/src/external/gpl3/gcc/usr.bin/include/Makefile',
                '~/src/netbsd/src/external/lgpl3/gmp/dist/mini-gmp/tests/Makefile',
                '~/src/netbsd/src/external/lgpl3/gmp/lib/libgmp/Makefile',
                '~/src/netbsd/src/external/lgpl3/gmp/lib/libgmp/Makefile',
                '~/src/netbsd/src/external/lgpl3/mpc/lib/libmpc/Makefile',
                '~/src/netbsd/src/external/lgpl3/mpfr/lib/libmpfr/Makefile',
                '~/src/netbsd/src/external/mit/xorg/lib/fontconfig/etc/conf.avail/Makefile',
                '~/src/netbsd/src/external/mit/xorg/lib/fontconfig/etc/conf.d/Makefile',
                '~/src/netbsd/src/external/mit/xorg/lib/fontconfig/etc/conf.d/Makefile',
                '~/src/netbsd/src/external/mit/xorg/lib/fontconfig/etc/Makefile',
                '~/src/netbsd/src/external/mit/xorg/lib/fontconfig/src/Makefile',
                '~/src/netbsd/src/external/mit/xorg/lib/libdrm_amdgpu/Makefile',
                '~/src/netbsd/src/external/mit/xorg/lib/libglapi/Makefile',
                '~/src/netbsd/src/external/mit/xorg/lib/xkeyboard-config/geometry/Makefile',
                '~/src/netbsd/src/external/mit/xorg/lib/xkeyboard-config/symbols/Makefile',
                '~/src/netbsd/src/external/mit/xorg/server/drivers/xf86-video-openchrome/Makefile',
                '~/src/netbsd/src/external/mit/xorg/server/xorg-server/Makefile',
                '~/src/netbsd/src/external/mit/xorg/tools/fc-cache/Makefile',
                '~/src/netbsd/src/lib/libm/Makefile',
                '~/src/netbsd/src/lib/libm/Makefile',
                '~/src/netbsd/src/lib/libm/Makefile',
                '~/src/netbsd/src/lib/libm/Makefile',
                '~/src/netbsd/src/lib/libm/Makefile',
                '~/src/netbsd/src/lib/libm/Makefile',
                '~/src/netbsd/src/lib/libm/Makefile',
                '~/src/netbsd/src/lib/Makefile',
                '~/src/netbsd/src/Makefile',
                '~/src/netbsd/src/regress/sys/arch/i386/Makefile',
                '~/src/netbsd/src/rescue/Makefile',
                '~/src/netbsd/src/share/man/man4/Makefile',
                '~/src/netbsd/src/share/man/man4/Makefile',
                '~/src/netbsd/src/sys/arch/evbmips/Makefile',
                '~/src/netbsd/src/sys/arch/evbmips/stand/Makefile',
                '~/src/netbsd/src/sys/arch/i386/include/Makefile',
                '~/src/netbsd/src/sys/modules/if_ppp/Makefile',
                '~/src/netbsd/src/sys/modules/procfs/Makefile',
                '~/src/netbsd/src/tests/include/sys/Makefile',
                '~/src/netbsd/src/tests/lib/libc/locale/Makefile',
                '~/src/netbsd/src/tests/net/route/Makefile',
                '~/src/netbsd/src/tests/rump/kernspace/Makefile',
                '~/src/netbsd/src/tests/rump/rumpkern/Makefile',
                '~/src/netbsd/src/tools/gcc/Makefile',
                '~/src/netbsd/src/tools/gcc/Makefile',
                '~/src/netbsd/src/tools/lex/Makefile',
                '~/src/netbsd/src/tools/mandoc/Makefile',
                '~/src/netbsd/src/usr.bin/tail/Makefile',
                '~/src/netbsd/src/usr.sbin/rpcbind/Makefile',
                '~/src/netbsd/src/usr.sbin/rpcbind/Makefile',
            ],
        ]
    elif lang == 'c':
        dirss = [
            [  # 0
            ],
            [  # 1
                '~/src/lldpd/',
                '~/src/xl2tpd/',
            ],
            [  # 2
                '~/src/git/',
                '~/src/gcc/',
            ],
        ]
    elif lang == 'cmake':
        dirss = [
            [  # 0
                '~/src/tes/cpp/CMakeLists.txt',
                '~/src/tes/cpp/CMakeLists_sub.cmake',
                '~/src/tes/cpp/CMakeLists_autotools.cmake',
                '~/src/tes/cpp/sub/CMakeLists.txt',
            ],
            [  # 1
            ],
            [  # 2
            ],
        ]
    elif lang == 'fish':
        dirss = [
            [  # 0
                '~/.config/fish/functions/',
            ],
            [  # 1
                '/usr/share/fish/functions/',
            ],
            [  # 2
            ],
        ]
    elif lang == 'python':
        dirss = [
            [  # 0
                '~/src/ema-scanner/',
                '~/src/instr/',
                '~/src/forecaster/',
                '~/usr/bin/aglang',
                '~/usr/bin/hsync',
            ],
            [  # 1
                '~/src/geopandas/',
            ],
            [  # 2
                '~/src/cpython/Doc/',
                '~/src/cpython/Grammar/',
                '~/src/cpython/Include/',
                '~/src/cpython/Lib/',
                '~/src/cpython/Mac/',
                '~/src/cpython/Misc/',
                '~/src/cpython/Modules/',
                '~/src/cpython/Objects/',
                '~/src/cpython/Parser/',
                '~/src/cpython/PC/',
                '~/src/cpython/PCbuild/',
                '~/src/cpython/Programs/',
                '~/src/cpython/Python/',
                '~/src/cpython/Tools/',
                '~/src/cpython/setup.py',
            ],
        ]
    else:
        raise RuntimeError(f'{lang}: Unknown language.')
    dirss = [[os.path.expanduser(d) for d in dirs] for dirs in dirss]
    return dirss


if __name__ == '__main__':
    """
    aglang python -vv argparse -C1
    """
    # TODO: dirs_my, dirs_pub, apo -> aglang -n
    # TODO: --list -> list directories
    #       aglang --list python
    parser = argparse.ArgumentParser(description='description here')
    parser.add_argument('-v', '--verbose', action='count', default=1,
                        help='no v: code what I well understand (default), '
                             '-v: project I little understand, '
                             '-vv: etc')
    # TODO: sync choices with get_dirs()
    parser.add_argument('LANG', choices=['bmake', 'cmake', 'fish', 'python'])
    parser.add_argument('PATTERN')
    parser.add_argument('ag-OPTION', nargs='*')
    args, ag_opts = parser.parse_known_args()
    dirss = get_dirs(args.LANG)
    dirss = dirss[:args.verbose]
    dirs = sum(dirss, [])

    args_call = ['ag'] + ag_opts + [args.PATTERN] + dirs
    # TODO: raise an error if pattern is empty
    subprocess.call(args_call)
