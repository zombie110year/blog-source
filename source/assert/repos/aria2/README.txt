<div id="aria2-the-ultra-fast-download-utility" class="document">

<div id="disclaimer" class="section">

Disclaimer
==========

This program comes with no warranty. You must use this program at your
own risk.

</div>

<div id="introduction" class="section">

Introduction
============

aria2 is a utility for downloading files. The supported protocols are
HTTP(S), FTP, SFTP, BitTorrent, and Metalink. aria2 can download a file
from multiple sources/protocols and tries to utilize your maximum
download bandwidth. It supports downloading a file from HTTP(S)/FTP/SFTP
and BitTorrent at the same time, while the data downloaded from
HTTP(S)/FTP/SFTP is uploaded to the BitTorrent swarm. Using Metalink's
chunk checksums, aria2 automatically validates chunks of data while
downloading a file like BitTorrent.

The project page is located at <https://aria2.github.io/>.

See [aria2 Online
Manual](https://aria2.github.io/manual/en/html/){.reference .external}
([Russian
translation](https://aria2.github.io/manual/ru/html/){.reference
.external}, [Portuguese
translation](https://aria2.github.io/manual/pt/html/){.reference
.external}) to learn how to use aria2.

</div>

<div id="features" class="section">

Features
========

Here is a list of features:

-   Command-line interface
-   Download files through HTTP(S)/FTP/SFTP/BitTorrent
-   Segmented downloading
-   Metalink version 4 (RFC 5854) support(HTTP/FTP/SFTP/BitTorrent)
-   Metalink version 3.0 support(HTTP/FTP/SFTP/BitTorrent)
-   Metalink/HTTP (RFC 6249) support
-   HTTP/1.1 implementation
-   HTTP Proxy support
-   HTTP BASIC authentication support
-   HTTP Proxy authentication support
-   Well-known environment variables for proxy: `http_proxy`{.docutils
    .literal}, `https_proxy`{.docutils .literal}, `ftp_proxy`{.docutils
    .literal}, `all_proxy`{.docutils .literal} and `no_proxy`{.docutils
    .literal}
-   HTTP gzip, deflate content encoding support
-   Verify peer using given trusted CA certificate in HTTPS
-   Client certificate authentication in HTTPS
-   Chunked transfer encoding support
-   Load Cookies from file using the Firefox3 format, Chromium/Google
    Chrome and the Mozilla/Firefox (1.x/2.x)/Netscape format.
-   Save Cookies in the Mozilla/Firefox (1.x/2.x)/Netscape format.
-   Custom HTTP Header support
-   Persistent Connections support
-   FTP/SFTP through HTTP Proxy
-   Download/Upload speed throttling
-   BitTorrent extensions: Fast extension, DHT, PEX, MSE/PSE,
    Multi-Tracker, UDP tracker
-   BitTorrent
    [WEB-Seeding](http://getright.com/seedtorrent.html){.reference
    .external}. aria2 requests chunks more than piece size to reduce the
    request overhead. It also supports pipelined requests with piece
    size.
-   BitTorrent Local Peer Discovery
-   Rename/change the directory structure of BitTorrent downloads
    completely
-   JSON-RPC (over HTTP and WebSocket)/XML-RPC interface
-   Run as a daemon process
-   Selective download in multi-file torrent/Metalink
-   Chunk checksum validation in Metalink
-   Can disable segmented downloading in Metalink
-   Netrc support
-   Configuration file support
-   Download URIs found in a text file or stdin and the destination
    directory and output file name can be specified optionally
-   Parameterized URI support
-   IPv6 support with Happy Eyeballs
-   Disk cache to reduce disk activity

</div>

<div id="versioning-and-release-schedule" class="section">

Versioning and release schedule
===============================

We use 3 numbers for aria2 version: MAJOR.MINOR.PATCH. We will ship
MINOR update on 15th of every month. We may skip a release if we have no
changes since the last release. The feature and documentation freeze
happens 10 days before the release day (5th day of the month) for
translation teams. We will raise an issue about the upcoming release
around that day.

We may release PATCH releases between regular releases if we have
security issues.

MAJOR version will stay at 1 for the time being.

</div>

<div id="how-to-get-source-code" class="section">

How to get source code
======================

We maintain the source code at Github: <https://github.com/aria2/aria2>

To get the latest source code, run following command:

``` {.literal-block}
$ git clone https://github.com/aria2/aria2.git
```

This will create aria2 directory in your current directory and source
files are stored there.

</div>

<div id="dependency" class="section">

Dependency
==========

  ------------------------------------------------------------------------
  features                  dependency
  ------------------------- ----------------------------------------------
  HTTPS                     OSX or GnuTLS or OpenSSL or Windows

  SFTP                      libssh2

  BitTorrent                None. Optional: libnettle+libgmp or libgcrypt
                            or OpenSSL (see note)

  Metalink                  libxml2 or Expat.

  Checksum                  None. Optional: OSX or libnettle or libgcrypt
                            or OpenSSL or Windows (see note)

  gzip, deflate in HTTP     zlib

  Async DNS                 C-Ares

  Firefox3/Chromium cookie  libsqlite3

  XML-RPC                   libxml2 or Expat.

  JSON-RPC over WebSocket   libnettle or libgcrypt or OpenSSL
  ------------------------------------------------------------------------

<div class="admonition note">

Note

libxml2 has precedence over Expat if both libraries are installed. If
you prefer Expat, run configure with `--without-libxml2`{.docutils
.literal}.

</div>

<div class="admonition note">

Note

On Apple OSX the OS-level SSL/TLS support will be preferred. Hence
neither GnuTLS nor OpenSSL are required on that platform. If you'd like
to disable this behavior, run configure with
`--without-appletls`{.docutils .literal}.

GnuTLS has precedence over OpenSSL if both libraries are installed. If
you prefer OpenSSL, run configure with `--without-gnutls`{.docutils
.literal} `--with-openssl`{.docutils .literal}.

On Windows there is SSL implementation available that is based on the
native Windows SSL capabilities (Schannel) and it will be preferred.
Hence neither GnuTLS nor OpenSSL are required on that platform. If you'd
like to disable this behavior, run configure with
`--without-wintls`{.docutils .literal}.

</div>

<div class="admonition note">

Note

On Apple OSX the OS-level checksum support will be preferred, unless
aria2 is configured with `--without-appletls`{.docutils .literal}.

libnettle has precedence over libgcrypt if both libraries are installed.
If you prefer libgcrypt, run configure with
`--without-libnettle --with-libgcrypt`{.docutils .literal}. If OpenSSL
is selected over GnuTLS, neither libnettle nor libgcrypt will be used.

If none of the optional dependencies are installed, an internal
implementation that only supports md5 and sha1 will be used.

On Windows there is SSL implementation available that is based on the
native Windows capabilities and it will be preferred, unless aria2 is
configured with `--without-wintls`{.docutils .literal}.

</div>

A user can have one of the following configurations for SSL and crypto
libraries:

-   OpenSSL
-   GnuTLS + libgcrypt
-   GnuTLS + libnettle
-   Apple TLS (OSX only)
-   Windows TLS (Windows only)

You can disable BitTorrent and Metalink support by providing
`--disable-bittorrent`{.docutils .literal} and
`--disable-metalink`{.docutils .literal} to the configure script
respectively.

In order to enable async DNS support, you need c-ares.

-   c-ares: <http://c-ares.haxx.se/>

</div>

<div id="how-to-build" class="section">

How to build
============

aria2 is primarily written in C++. Initially it was written based on
C++98/C++03 standard features. We are now migrating aria2 to C++11
standard. The current source code requires C++11 aware compiler. For
well-known compilers, such as g++ and clang, the `-std=c++11`{.docutils
.literal} or `-std=c++0x`{.docutils .literal} flag must be supported.

In order to build aria2 from the source package, you need following
development packages (package name may vary depending on the
distribution you use):

-   libgnutls-dev (Required for HTTPS, BitTorrent, Checksum support)
-   nettle-dev (Required for BitTorrent, Checksum support)
-   libgmp-dev (Required for BitTorrent)
-   libssh2-1-dev (Required for SFTP support)
-   libc-ares-dev (Required for async DNS support)
-   libxml2-dev (Required for Metalink support)
-   zlib1g-dev (Required for gzip, deflate decoding support in HTTP)
-   libsqlite3-dev (Required for Firefox3/Chromium cookie support)
-   pkg-config (Required to detect installed libraries)

You can use libgcrypt-dev instead of nettle-dev and libgmp-dev:

-   libgpg-error-dev (Required for BitTorrent, Checksum support)
-   libgcrypt-dev (Required for BitTorrent, Checksum support)

You can use libssl-dev instead of libgnutls-dev, nettle-dev, libgmp-dev,
libgpg-error-dev and libgcrypt-dev:

-   libssl-dev (Required for HTTPS, BitTorrent, Checksum support)

You can use libexpat1-dev instead of libxml2-dev:

-   libexpat1-dev (Required for Metalink support)

On Fedora you need the following packages: gcc, gcc-c++, kernel-devel,
libgcrypt-devel, libxml2-devel, openssl-devel, gettext-devel, cppunit

If you downloaded source code from git repository, you have to install
following packages to get autoconf macros:

-   libxml2-dev
-   libcppunit-dev
-   autoconf
-   automake
-   autotools-dev
-   autopoint
-   libtool

And run following command to generate configure script and other files
necessary to build the program:

``` {.literal-block}
$ autoreconf -i
```

Also you need [Sphinx](http://sphinx-doc.org/){.reference .external} to
build man page.

If you are building aria2 for Mac OS X, take a look at the
make-release-os.mk GNU Make makefile.

The quickest way to build aria2 is first run configure script:

``` {.literal-block}
$ ./configure
```

To build statically linked aria2, use `ARIA2_STATIC=yes`{.docutils
.literal} command-line option:

``` {.literal-block}
$ ./configure ARIA2_STATIC=yes
```

After configuration is done, run `make`{.docutils .literal} to compile
the program:

``` {.literal-block}
$ make
```

See [Cross-compiling Windows
binary](#cross-compiling-windows-binary){.reference .internal} to create
a Windows binary. See [Cross-compiling Android
binary](#cross-compiling-android-binary){.reference .internal} to create
an Android binary.

The configure script checks available libraries and enables as many
features as possible except for experimental features not enabled by
default.

Since 1.1.0, aria2 checks the certificate of HTTPS servers by default.
If you build with OpenSSL or the recent version of GnuTLS which has
`gnutls_certificate_set_x509_system_trust()`{.docutils .literal}
function and the library is properly configured to locate the
system-wide CA certificates store, aria2 will automatically load those
certificates at the startup. If it is not the case, I recommend to
supply the path to the CA bundle file. For example, in Debian the path
to CA bundle file is '/etc/ssl/certs/ca-certificates.crt' (in
ca-certificates package). This may vary depending on your distribution.
You can give it to configure script using
`--with-ca-bundle option`{.docutils .literal}:

``` {.literal-block}
$ ./configure --with-ca-bundle='/etc/ssl/certs/ca-certificates.crt'
$ make
```

Without `--with-ca-bundle`{.docutils .literal} option, you will
encounter the error when accessing HTTPS servers because the certificate
cannot be verified without CA bundle. In such case, you can specify the
CA bundle file using aria2's `--ca-certificate`{.docutils .literal}
option. If you don't have CA bundle file installed, then the last resort
is disable the certificate validation using
`--check-certificate=false`{.docutils .literal}.

Using the native OSX (AppleTLS) and/or Windows (WinTLS) implementation
will automatically use the system certificate store, so
`--with-ca-bundle`{.docutils .literal} is not necessary and will be
ignored when using these implementations.

By default, the bash\_completion file named `aria2c`{.docutils .literal}
is installed to the directory
`$prefix/share/doc/aria2/bash_completion`{.docutils .literal}. To change
the install directory of the file, use
`--with-bashcompletiondir                     `{.docutils .literal}
option.

After a `make`{.docutils .literal} the executable is located at
`src/aria2c`{.docutils .literal}.

aria2 uses CppUnit for automated unit testing. To run the unit test:

``` {.literal-block}
$ make check
```

</div>

<div id="cross-compiling-windows-binary" class="section">

Cross-compiling Windows binary
==============================

In this section, we describe how to build a Windows binary using a
mingw-w64 (<http://mingw-w64.org/doku.php>) cross-compiler on Debian
Linux. The MinGW (<http://www.mingw.org/>) may not be able to build
aria2.

The easiest way to build Windows binary is use Dockerfile.mingw. See
Dockerfile.mingw how to build binary. If you cannot use Dockerfile, then
continue to read following paragraphs.

Basically, after compiling and installing depended libraries, you can do
cross-compile just passing appropriate `--host`{.docutils .literal}
option and specifying `CPPFLAGS`{.docutils .literal},
`LDFLAGS`{.docutils .literal} and `PKG_CONFIG_LIBDIR`{.docutils
.literal} variables to configure. For convenience and lowering our own
development cost, we provide easier way to configure the build settings.

`mingw-config`{.docutils .literal} script is a configure script wrapper
for mingw-w64. We use it to create official Windows build. This script
assumes following libraries have been built for cross-compile:

-   c-ares
-   expat
-   sqlite3
-   zlib
-   libssh2
-   cppunit

Some environment variables can be adjusted to change build settings:

`HOST`{.docutils .literal}
:   cross-compile to build programs to run on `HOST`{.docutils
    .literal}. It defaults to `i686-w64-mingw32`{.docutils .literal}. To
    build 64bit binary, specify `x86_64-w64-mingw32`{.docutils
    .literal}.

`PREFIX`{.docutils .literal}
:   Prefix to the directory where dependent libraries are installed. It
    defaults to `/usr/local/$HOST`{.docutils .literal}.
    `-I$PREFIX/include`{.docutils .literal} will be added to
    `CPPFLAGS`{.docutils .literal}. `-L$PREFIX/lib`{.docutils .literal}
    will be added to `LDFLAGS`{.docutils .literal}.
    `$PREFIX/lib/pkgconfig`{.docutils .literal} will be set to
    `PKG_CONFIG_LIBDIR`{.docutils .literal}.

For example, to build 64bit binary do this:

``` {.literal-block}
$ HOST=x86_64-w64-mingw32 ./mingw-config
```

If you want libaria2 dll with `--enable-libaria2`{.docutils .literal},
then don't use `ARIA2_STATIC=yes`{.docutils .literal} and prepare the
DLL version of external libraries.

</div>

<div id="cross-compiling-android-binary" class="section">

Cross-compiling Android binary
==============================

In this section, we describe how to build Android binary using Android
NDK cross-compiler on Debian Linux.

At the time of this writing, android-ndk-r14b should compile aria2
without errors.

`android-config`{.docutils .literal} script is a configure script
wrapper for Android build. We use it to create official Android build.
This script assumes the following libraries have been built for
cross-compile:

-   c-ares
-   openssl
-   expat
-   zlib
-   libssh2

When building the above libraries, make sure that disable shared library
and enable only static library. We are going to link those libraries
statically.

We use zlib which comes with Android NDK, so we don't have to build it
by ourselves.

`android-config`{.docutils .literal} assumes the existence of
`$ANDROID_HOME`{.docutils .literal} environment variable which must
fulfill the following conditions:

-   Android NDK toolchain is installed under
    `$ANDROID_HOME/toolchain`{.docutils .literal}. Refer to [Standalone
    Toolchain](https://developer.android.com/ndk/guides/standalone_toolchain.html){.reference
    .external} for more details, but it is a bit out of date.

    To install toolchain under `$ANDROID_HOME/toolchain`{.docutils
    .literal}, do this:

    ``` {.code .text .literal-block}
    $NDK/build/tools/make_standalone_toolchain.py \
       --arch arm --api 16 --stl=gnustl \
       --install-dir $ANDROID_HOME/toolchain
    ```

-   The dependent libraries must be installed under
    `$ANDROID_HOME/usr/local`{.docutils .literal}.

Before running `android-config`{.docutils .literal} and
`android-make`{.docutils .literal}, `$ANDROID_HOME`{.docutils .literal}
environment variable must be set to point to the correct path.

After `android-config`{.docutils .literal}, run `android-make`{.docutils
.literal} to compile sources.

</div>

<div id="building-documentation" class="section">

Building documentation
======================

[Sphinx](http://sphinx-doc.org/){.reference .external} is used to build
the documentation. aria2 man pages will be build when you run
`make`{.docutils .literal} if they are not up-to-date. You can also
build HTML version of aria2 man page by `make html`{.docutils .literal}.
The HTML version manual is also available at
[online](https://aria2.github.io/manual/en/html/){.reference .external}
([Russian
translation](https://aria2.github.io/manual/ru/html/){.reference
.external}, [Portuguese
translation](https://aria2.github.io/manual/pt/html/){.reference
.external}).

</div>

<div id="bittorrent" class="section">

BitTorrent
==========

<div id="about-file-names" class="section">

About file names
----------------

The file name of the downloaded file is determined as follows:

single-file mode
:   If "name" key is present in .torrent file, file name is the value of
    "name" key. Otherwise, file name is the base name of .torrent file
    appended by ".file". For example, .torrent file is "test.torrent",
    then file name is "test.torrent.file". The directory to store the
    downloaded file can be specified by -d option.

multi-file mode
:   The complete directory/file structure mentioned in .torrent file is
    created. The directory to store the top directory of downloaded
    files can be specified by -d option.

Before download starts, a complete directory structure is created if
needed. By default, aria2 opens at most 100 files mentioned in .torrent
file, and directly writes to and reads from these files. The number of
files to open simultaneously can be controlled by
`--bt-max-open-files`{.docutils .literal} option.

</div>

<div id="dht" class="section">

DHT
---

aria2 supports mainline compatible DHT. By default, the routing table
for IPv4 DHT is saved to `$XDG_CACHE_HOME/aria2/dht.dat`{.docutils
.literal} and the routing table for IPv6 DHT is saved to
`$XDG_CACHE_HOME/aria2/dht6.dat`{.docutils .literal} unless files exist
at `$HOME/.aria2/dht.dat`{.docutils .literal} or
`$HOME/.aria2/dht6.dat`{.docutils .literal}. aria2 uses same port number
to listen on for both IPv4 and IPv6 DHT.

</div>

<div id="udp-tracker" class="section">

UDP tracker
-----------

UDP tracker support is enabled when IPv4 DHT is enabled. The port number
of UDP tracker is shared with DHT. Use `--dht-listen-port`{.docutils
.literal} option to change the port number.

</div>

<div id="other-things-should-be-noted" class="section">

Other things should be noted
----------------------------

-   `-o`{.docutils .literal} option is used to change the file name of
    .torrent file itself, not a file name of a file in .torrent file.
    For this purpose, use `--index-out`{.docutils .literal} option
    instead.
-   The port numbers that aria2 uses by default are 6881-6999 for TCP
    and UDP.
-   aria2 doesn't configure port-forwarding automatically. Please
    configure your router or firewall manually.
-   The maximum number of peers is 55. This limit may be exceeded when
    download rate is low. This download rate can be adjusted using
    `--bt-request-peer-speed-limit`{.docutils .literal} option.
-   As of release 0.10.0, aria2 stops sending request message after
    selective download completes.

</div>

</div>

<div id="metalink" class="section">

Metalink
========

The current implementation supports HTTP(S)/FTP/SFTP/BitTorrent. The
other P2P protocols are ignored. Both Metalink4 (RFC 5854) and Metalink
version 3.0 documents are supported.

For checksum verification, md5, sha-1, sha-224, sha-256, sha-384 and
sha-512 are supported. If multiple hash algorithms are provided, aria2
uses stronger one. If whole file checksum verification fails, aria2
doesn't retry the download and just exits with non-zero return code.

The supported user preferences are version, language, location, protocol
and os.

If chunk checksums are provided in Metalink file, aria2 automatically
validates chunks of data during download. This behavior can be turned
off by a command-line option.

If signature is included in a Metalink file, aria2 saves it as a file
after the completion of the download. The file name is download file
name + ".sig". If same file already exists, the signature file is not
saved.

In Metalink4, multi-file torrent could appear in metalink:metaurl
element. Since aria2 cannot download 2 same torrents at the same time,
aria2 groups files in metalink:file element which has same BitTorrent
metaurl and downloads them from a single BitTorrent swarm. This is
basically multi-file torrent download with file selection, so the
adjacent files which is not in Metalink document but shares same piece
with selected file are also created.

If relative URI is specified in metalink:url or metalink:metaurl
element, aria2 uses the URI of Metalink file as base URI to resolve the
relative URI. If relative URI is found in Metalink file which is read
from local disk, aria2 uses the value of `--metalink-base-uri`{.docutils
.literal} option as base URI. If this option is not specified, the
relative URI will be ignored.

</div>

<div id="metalink-http" class="section">

Metalink/HTTP
=============

The current implementation only uses rel=duplicate links only. aria2
understands Digest header fields and check whether it matches the digest
value from other sources. If it differs, drop connection. aria2 also
uses this digest value to perform checksum verification after download
finished. aria2 recognizes geo value. To tell aria2 which location you
prefer, you can use `--metalink-location`{.docutils .literal} option.

</div>

<div id="netrc" class="section">

netrc
=====

netrc support is enabled by default for HTTP(S)/FTP/SFTP. To disable
netrc support, specify -n command-line option. Your .netrc file should
have correct permissions(600).

</div>

<div id="websocket" class="section">

WebSocket
=========

The WebSocket server embedded in aria2 implements the specification
defined in RFC 6455. The supported protocol version is 13.

</div>

<div id="libaria2" class="section">

libaria2
========

The libaria2 is a C++ library which offers aria2 functionality to the
client code. Currently, libaria2 is not built by default. To enable
libaria2, use `--enable-libaria2`{.docutils .literal} configure option.
By default, only the shared library is built. To build static library,
use `--enable-static`{.docutils .literal} configure option as well. See
libaria2 documentation to know how to use API.

</div>

<div id="references" class="section">

References
==========

-   [aria2 Online
    Manual](https://aria2.github.io/manual/en/html/){.reference
    .external}
-   <https://aria2.github.io/>
-   [RFC 959 FILE TRANSFER PROTOCOL
    (FTP)](http://tools.ietf.org/html/rfc959){.reference .external}
-   [RFC 1738 Uniform Resource Locators
    (URL)](http://tools.ietf.org/html/rfc1738){.reference .external}
-   [RFC 2428 FTP Extensions for IPv6 and
    NATs](http://tools.ietf.org/html/rfc2428){.reference .external}
-   [RFC 2616 Hypertext Transfer Protocol --
    HTTP/1.1](http://tools.ietf.org/html/rfc2616){.reference .external}
-   [RFC 3659 Extensions to
    FTP](http://tools.ietf.org/html/rfc3659){.reference .external}
-   [RFC 3986 Uniform Resource Identifier (URI): Generic
    Syntax](http://tools.ietf.org/html/rfc3986){.reference .external}
-   [RFC 4038 Application Aspects of IPv6
    Transition](http://tools.ietf.org/html/rfc4038){.reference
    .external}
-   [RFC 5854 The Metalink Download Description
    Format](http://tools.ietf.org/html/rfc5854){.reference .external}
-   [RFC 6249 Metalink/HTTP: Mirrors and
    Hashes](http://tools.ietf.org/html/rfc6249){.reference .external}
-   [RFC 6265 HTTP State Management
    Mechanism](http://tools.ietf.org/html/rfc6265){.reference .external}
-   [RFC 6266 Use of the Content-Disposition Header Field in the
    Hypertext Transfer Protocol
    (HTTP)](http://tools.ietf.org/html/rfc6266){.reference .external}
-   [RFC 6455 The WebSocket
    Protocol](http://tools.ietf.org/html/rfc6455){.reference .external}
-   [RFC 6555 Happy Eyeballs: Success with Dual-Stack
    Hosts](http://tools.ietf.org/html/rfc6555){.reference .external}
-   [The BitTorrent Protocol
    Specification](http://www.bittorrent.org/beps/bep_0003.html){.reference
    .external}
-   [BitTorrent: DHT
    Protocol](http://www.bittorrent.org/beps/bep_0005.html){.reference
    .external}
-   [BitTorrent: Fast
    Extension](http://www.bittorrent.org/beps/bep_0006.html){.reference
    .external}
-   [BitTorrent: IPv6 Tracker
    Extension](http://www.bittorrent.org/beps/bep_0007.html){.reference
    .external}
-   [BitTorrent: Extension for Peers to Send Metadata
    Files](http://www.bittorrent.org/beps/bep_0009.html){.reference
    .external}
-   [BitTorrent: Extension
    Protocol](http://www.bittorrent.org/beps/bep_0010.html){.reference
    .external}
-   [BitTorrent: Multitracker Metadata
    Extension](http://www.bittorrent.org/beps/bep_0012.html){.reference
    .external}
-   [BitTorrent: UDP Tracker Protocol for
    BitTorrent](http://www.bittorrent.org/beps/bep_0015.html){.reference
    .external} and [BitTorrent udp-tracker protocol
    specification](http://www.rasterbar.com/products/libtorrent/udp_tracker_protocol.html){.reference
    .external}.
-   [BitTorrent: WebSeed - HTTP/FTP Seeding (GetRight
    style)](http://www.bittorrent.org/beps/bep_0019.html){.reference
    .external}
-   [BitTorrent: Private
    Torrents](http://www.bittorrent.org/beps/bep_0027.html){.reference
    .external}
-   [BitTorrent: BitTorrent DHT Extensions for
    IPv6](http://www.bittorrent.org/beps/bep_0032.html){.reference
    .external}
-   [BitTorrent: Message Stream
    Encryption](http://wiki.vuze.com/w/Message_Stream_Encryption){.reference
    .external}
-   [Kademlia: A Peer-to-peer Information System Based on the XOR
    Metric](https://pdos.csail.mit.edu/~petar/papers/maymounkov-kademlia-lncs.pdf){.reference
    .external}

</div>

</div>
