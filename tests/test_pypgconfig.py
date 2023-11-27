from pytest import fixture
from pypgconfig import PgConfig, which_pgconfig, detect
from pathlib import Path


@fixture
def mock_pg_config():
    return r"""BINDIR = /Users/flo/pg_build/bin
DOCDIR = /Users/flo/pg_build/share/doc/postgresql
HTMLDIR = /Users/flo/pg_build/share/doc/postgresql
INCLUDEDIR = /Users/flo/pg_build/include
PKGINCLUDEDIR = /Users/flo/pg_build/include/postgresql
INCLUDEDIR-SERVER = /Users/flo/pg_build/include/postgresql/server
LIBDIR = /Users/flo/pg_build/lib
PKGLIBDIR = /Users/flo/pg_build/lib/postgresql
LOCALEDIR = /Users/flo/pg_build/share/locale
MANDIR = /Users/flo/pg_build/share/man
SHAREDIR = /Users/flo/pg_build/share/postgresql
SYSCONFDIR = /Users/flo/pg_build/etc/postgresql
PGXS = /Users/flo/pg_build/lib/postgresql/pgxs/src/makefiles/pgxs.mk
CONFIGURE =  '--prefix=/Users/flo/pg_build' '--enable-depend' '--enable-cassert' '--enable-debug' 'CFLAGS=-ggdb -Og -g3 -fno-omit-frame-pointer' '--without-icu' '--with-python' 'PYTHON=/opt/homebrew/bin/python3.11' '--with-libxml' 'XML2_CONFIG=/usr/local/bin/xml2-config' '--with-lz4'
CC = gcc
CPPFLAGS = -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX14.0.sdk -I/usr/local/include/libxml2 -I/opt/homebrew/Cellar/lz4/1.9.4/include
CFLAGS = -Wall -Wmissing-prototypes -Wpointer-arith -Wdeclaration-after-statement -Werror=vla -Werror=unguarded-availability-new -Wendif-labels -Wmissing-format-attribute -Wcast-function-type -Wformat-security -fno-strict-aliasing -fwrapv -Wno-unused-command-line-argument -Wno-compound-token-split-by-macro -Wno-deprecated-non-prototype -g -ggdb -Og -g3 -fno-omit-frame-pointer
CFLAGS_SL = 
LDFLAGS = -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX14.0.sdk -L/usr/local/lib -L/opt/homebrew/Cellar/xz/5.4.3/lib -L/opt/homebrew/Cellar/lz4/1.9.4/lib -Wl,-dead_strip_dylibs
LDFLAGS_EX = 
LDFLAGS_SL = 
LIBS = -lpgcommon -lpgport -llz4 -lxml2 -lz -lreadline -lm 
VERSION = PostgreSQL 15.4
"""


def test_flags():
    pass


def test_pgconfig(mock_pg_config):
    pgconf = PgConfig(mock_pg_config)

    assert pgconf.payload != None
    assert pgconf.version.__str__() == "15.4"
    assert pgconf.version.parsed_items == (15, 4)
    assert pgconf.version.major == 15
    assert pgconf.version.minor == 4
    assert pgconf.version.patch is None

    assert pgconf.libs == ["pgcommon", "pgport", "lz4", "xml2", "z", "readline", "m"]

    # Paths are parsed when it should
    assert pgconf.BINDIR == Path("/Users/flo/pg_build/bin")
    assert pgconf.CC == Path("gcc")


def test_pythonpath(mock_pg_config):
    pgconf = PgConfig(mock_pg_config)

    assert pgconf.with_python
    assert pgconf.pythonpath == Path("/opt/homebrew/bin/python3.11")
