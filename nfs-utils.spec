%global rpc_uid         29
%global nfsnobody_uid   65534
%global _statdpath /var/lib/nfs/statd

Name:    nfs-utils
Version: 2.3.3
Release: 4
Epoch:   1
Summary: The Linux NFS userland utility package
License: MIT and GPLv2 and GPLv2+ and BSD
URL:     http://sourceforge.net/projects/nfs/

Source0: https://www.kernel.org/pub/linux/utils/nfs-utils/%{version}/%{name}-%{version}.tar.xz
Source1: id_resolver.conf
Source2: nfs.sysconfig
Source3: nfs-utils_env.sh
Source4: lockd.conf
Source5: 24-nfs-server.conf

Patch0:     0000-nfs-utils-1.2.1-statdpath-man.patch
Patch1:     0001-nfs-utils-1.2.1-exp-subtree-warn-off.patch
Patch2:     0002-nfs-utils-1.2.5-idmap-errmsg.patch
Patch3:     0003-nfs-utils-2.1.1-nfs-config.patch
Patch4:     0004-nfs-utils-2.3.1-systemd-gssproxy-restart.patch

Patch6000:  6000-bugfix-fail-disable-major-NFS-version-4.patch
Patch6001:  6001-ignore-EBUSY-when-a-filesystem-is-already-mount.patch
Patch6002:  6002-fix-quoting-in-configure-ac.patch
Patch6003:  6003-harden-configure-ac-checks-for-libxml2.patch
Patch6004:  6004-finish-port-of-junction-support-to-nfs-util.patch
Patch6005:  6005-add-IgnoreOnIsolate-yes-in-rpc-statd-service.patch
Patch6006:  6006-improve-error-msg-when-mount-fail-with-EBUSY.patch
Patch6007:  6007-fix-with-rpcgen-internal-nottaking-effect.patch
Patch6008:  6008-do-not-fatalize-Wstrict-prototypes-with-internal-rpcgen.patch
Patch6009:  6009-run-statd-notify-even-when-nfs-client-isnot-enabled.patch
Patch6010:  6010-honour-with-pluginpath-for-instalation.patch
Patch6011:  6011-update-the-path-of-libnfs.a.patch
Patch6012:  6012-removed-new-error-format-overflow-2-errors-in-nfs-utils.patch
Patch6013:  6013-fixed-manage-gids-option-typo-in-nfs.conf.patch
Patch6014:  6014-more-carefully-detect-availability-of-res_querydomain.patch
Patch6015:  6015-fix-use-of-undefined-macro-HAVE_GETRPCBYNUMBER_R.patch
Patch6016:  6016-provide-the-UID-GID-name-for-which-mapping-fails.patch
Patch6017:  6017-add-miss-cast-to-getsockname.patch
Patch6018:  6018-add-miss-libgen-header-in-idmapd.patch
Patch6019:  6019-remove-resource-leaks-from-junction-path.c.patch
Patch6020:  6020-remove-resource-leaks-from-nfs-exports.c.patch
Patch6021:  6021-remove-a-resource-leak-from-nfs-mydaemon.c.patch
Patch6022:  6022-remove-a-resource-leak-from-nfs-rpcmisc.c.patch
Patch6023:  6023-remove-a-resource-leak-from-nfs-svc_socket.c.patch
Patch6024:  6024-remove-bad-frees-from-nfs-xcommon.c.patch
Patch6025:  6025-remove-resource-leaks-from-nfs-xlog.c.patch
Patch6026:  6026-remove-resource-leaks-from-libnfsidmap.c.patch
Patch6027:  6027-remove-resource-leaks-from-nfsidmap-static.c.patch
Patch6028:  6028-remove-a-resource-leak-from-nsm-file.c.patch
Patch6029:  6029-remove-resource-leaks-from-rpc-pipefs-generator.c.patch
Patch6030:  6030-remove-resource-leaks-from-device-discovery.patch
Patch6031:  6031-remove-resource-leaks-from-krb5_util.c.patch
Patch6032:  6032-remove-a-resource-leak-from-mount-configfile.patch
Patch6033:  6033-remove-a-resource-leak-from-mount-nfsmount.c.patch
Patch6034:  6034-remove-a-resource-leak-from-mount-stropts.c.patch
Patch6035:  6035-remove-resource-leaks-from-mountd-cache.c.patch
Patch6036:  6036-remove-a-resource-leak-from-mountd-fsloc.c.patch
Patch6037:  6037-remove-a-resource-leak-from-nfsdcltrack-sqlite.c.patch
Patch6038:  6038-report-correct-error-in-the-fall_back-cases.patch
Patch6039:  6039-fix-e_hostname-and-e_uuid-leaks-in-rpc.mountd.patch
Patch6040:  6040-donot-share-cache-file-descriptors-among-processes.patch

Patch9000:  9000-systemd-idmapd-require-rpc-pipefs.patch

BuildRequires: libevent-devel,libcap-devel, libtirpc-devel libblkid-devel
BuildRequires: krb5-libs >= 1.4 autoconf >= 2.57 openldap-devel >= 2.2
BuildRequires: automake, libtool, gcc, device-mapper-devel
BuildRequires: krb5-devel, libmount-devel
BuildRequires: sqlite-devel, python3-devel
BuildRequires: systemd, pkgconfig, rpcgen


Requires:         rpcbind, sed, gawk, grep, kmod, keyutils, quota
Requires:         libevent libblkid libcap libmount
Requires:         libtirpc >= 0.2.3-1 gssproxy => 0.7.0-3
Requires(pre):    shadow-utils >= 4.0.3-25
Requires(pre):    util-linux
Requires(pre):    coreutils
Requires(pre):    glibc
Requires(preun):  coreutils
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
Requires(postun): glibc
Requires:         openldap


Provides:  exportfs    = %{epoch}:%{version}-%{release}
Provides:  nfsstat     = %{epoch}:%{version}-%{release}
Provides:  showmount   = %{epoch}:%{version}-%{release}
Provides:  rpcdebug    = %{epoch}:%{version}-%{release}
Provides:  rpc.idmapd  = %{epoch}:%{version}-%{release}
Provides:  rpc.mountd  = %{epoch}:%{version}-%{release}
Provides:  rpc.nfsd    = %{epoch}:%{version}-%{release}
Provides:  rpc.statd   = %{epoch}:%{version}-%{release}
Provides:  rpc.gssd    = %{epoch}:%{version}-%{release}
Provides:  mount.nfs   = %{epoch}:%{version}-%{release}
Provides:  mount.nfs4  = %{epoch}:%{version}-%{release}
Provides:  umount.nfs  = %{epoch}:%{version}-%{release}
Provides:  umount.nfs4 = %{epoch}:%{version}-%{release}
Provides:  sm-notify   = %{epoch}:%{version}-%{release}
Provides:  start-statd = %{epoch}:%{version}-%{release}
Provides:  libnfsidmap = %{epoch}:%{version}-%{release}
Provides:  libnfsidmap%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes: libnfsidmap


%description
This is he nfs-utils tools package.
It contains the showmount,mount.nfs,umount.nfs and libnfsidmap

%package   devel
Summary:   Including header files and library for the developing of libnfsidmap library
Requires:  nfs-utils%{?_isa} = %{epoch}:%{version}-%{release}
Requires:  pkgconfig
Provides:  libnfsidmap-devel = %{epoch}:%{version}-%{release}
Provides:  libnfsidmap-devel%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes: libnfsidmap-devel

%description devel
This contains dynamic libraries and header files for the developing of
the libnfsidmap library.


%package   help
Summary:   Including man files for nfs-utils
Requires:  man

%description  help
This contains man files for the using of nfs-utils.

%prep
%autosetup -n %{name}-%{version} -p1
find -name \*.py -exec sed -r -i '1s|^#!\s*/usr/bin.*python.*|#!%{__python3}|' {} \;

%build
sh -x autogen.sh
%configure \
    CFLAGS="%{build_cflags} -D_FILE_OFFSET_BITS=64" \
    LDFLAGS="%{build_ldflags}" \
    --enable-mountconfig \
    --enable-ipv6 \
    --with-statdpath=%{_statdpath} \
    --enable-libmount-mount \
    --with-systemd \
    --without-tcp-wrappers \
    --with-pluginpath=%{_libdir}/libnfsidmap

%make_build all

%install
%make_install


install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/request-key.d/id_resolver.conf
install -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/nfs

install -s -m 755 tools/rpcdebug/rpcdebug $RPM_BUILD_ROOT%{_sbindir}
install -m 644 utils/mount/nfsmount.conf  $RPM_BUILD_ROOT%{_sysconfdir}
install -m 644 nfs.conf  $RPM_BUILD_ROOT%{_sysconfdir}
install -m 644 support/nfsidmap/idmapd.conf $RPM_BUILD_ROOT%{_sysconfdir}

install -D -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{_libexecdir}/nfs-utils/nfs-utils_env.sh
install -D -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d/lockd.conf
install -D -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/gssproxy/24-nfs-server.conf


touch $RPM_BUILD_ROOT%{_sharedstatedir}/nfs/rmtab
mv $RPM_BUILD_ROOT%{_sbindir}/rpc.statd $RPM_BUILD_ROOT/sbin

mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/nfs/rpc_pipefs
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/nfs/v4recovery
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/exports.d

cd $RPM_BUILD_ROOT%{_unitdir}
ln -s rpc-statd.service nfs-lock.service
ln -s rpc-gssd.service nfs-secure.service
ln -s nfs-server.service nfs.service
ln -s nfs-idmapd.service  nfs-idmap.service

rm -rf $RPM_BUILD_ROOT%{_libdir}/{*.a,*.la}
rm -rf $RPM_BUILD_ROOT%{_libdir}/libnfsidmap/{*.a,*.la}

%pre
if [ -f /var/lock/subsys/rpc.gssd ]; then
    mv /var/lock/subsys/rpc.gssd /var/lock/subsys/rpcgssd
fi

if [ -f /var/lock/subsys/rpc.idmapd ]; then
    mv /var/lock/subsys/rpc.idmapd /var/lock/subsys/rpcidmapd
fi

cat /etc/group | cut -d':' -f 1 | grep rpcuser &> /dev/null
if [ "$?" -ne 0 ]; then
    /usr/sbin/groupadd -g %{rpc_uid} rpcuser &> /dev/null || :
else
    /usr/sbin/groupmod -g %{rpc_uid} rpcuser &> /dev/null || :
fi

cat /etc/passwd | cut -d':' -f 1 | grep rpcuser &> /dev/null
if [ "$?" -ne 0 ]; then
    /usr/sbin/useradd -l -c "RPC Service User" -r -g %{rpc_uid} \
        -s /sbin/nologin -u %{rpc_uid} -d /var/lib/nfs rpcuser &> /dev/null || :
else
 /usr/sbin/usermod -u %{rpc_uid} -g %{rpc_uid} rpcuser &> /dev/null || :
fi



cat /etc/group | cut -d':' -f 3 | grep %{nfsnobody_uid} &> /dev/null
if [ "$?" -ne 0 ]; then
    /usr/sbin/groupadd -g %{nfsnobody_uid} nfsnobody &> /dev/null || :
fi

cat /etc/passwd | cut -d':' -f 3 | grep %{nfsnobody_uid} &> /dev/null
if [ $? -ne 0 ]; then
    /usr/sbin/useradd -l -c "Anonymous NFS User" -r -g %{nfsnobody_uid} \
    -s /sbin/nologin -u %{nfsnobody_uid} -d /var/lib/nfs nfsnobody &> /dev/null || :
fi

%post
if [ $1 -eq 1 ] ; then
    /bin/systemctl enable nfs-client.target &> /dev/null  || :
    /bin/systemctl start nfs-client.target  &> /dev/null  || :
fi

%systemd_post nfs-config
%systemd_post nfs-server
/bin/systemctl try-restart gssproxy  &> /dev/null || :

%preun
if [ $1 -eq 0 ]; then
    %systemd_preun nfs-client.target
    %systemd_preun nfs-server.server
fi

%postun
%systemd_postun_with_restart  nfs-client.target
%systemd_postun_with_restart  nfs-server

/bin/systemctl --system daemon-reload &> /dev/null  || :


%files
%doc support/nfsidmap/AUTHORS linux-nfs/README linux-nfs/THANKS
%license support/nfsidmap/COPYING
%config(noreplace) /etc/sysconfig/nfs
%config(noreplace) /etc/nfsmount.conf
%config(noreplace) %{_sharedstatedir}/nfs/etab
%config(noreplace) %{_sharedstatedir}/nfs/rmtab
%config(noreplace) %{_sysconfdir}/idmapd.conf
%config(noreplace) %{_sysconfdir}/request-key.d/id_resolver.conf
%config(noreplace) %{_sysconfdir}/modprobe.d/lockd.conf
%config(noreplace) %{_sysconfdir}/nfs.conf
%dir %{_sysconfdir}/exports.d
%dir %{_sharedstatedir}/nfs
%dir %{_sharedstatedir}/nfs/v4recovery
%dir %{_sharedstatedir}/nfs/rpc_pipefs
%dir %{_libexecdir}/nfs-utils
%dir %attr(700,rpcuser,rpcuser) %{_sharedstatedir}/nfs/statd
%dir %attr(700,rpcuser,rpcuser) %{_sharedstatedir}/nfs/statd/sm
%dir %attr(700,rpcuser,rpcuser) %{_sharedstatedir}/nfs/statd/sm.bak
%ghost %attr(644,rpcuser,rpcuser) %{_statdpath}/state
%attr(0600,root,root) %config(noreplace) /%{_sysconfdir}/gssproxy/24-nfs-server.conf
%attr(4755,root,root) /sbin/mount.nfs
%attr(755,root,root) %{_libexecdir}/nfs-utils/nfs-utils_env.sh
/sbin/{rpc.statd,nfsdcltrack,osd_login,mount.nfs4,umount.*}
%{_sbindir}/*
%{_prefix}/lib/systemd/*/*
%{_libdir}/libnfsidmap.so.*
%{_libdir}/libnfsidmap/*.so

%files devel
%{_includedir}/nfsidmap.h
%{_includedir}/nfsidmap_plugin.h
%{_libdir}/pkgconfig/libnfsidmap.pc
%{_libdir}/libnfsidmap.so

%files help
%{_mandir}/*/*

%changelog
* Sun Sep 29 2019 zhanghaibo <ted.zhang@huawei.com> - 2.3.3-4
- Remove some comments

* Tue Sep 05 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.3.3-3
- Package init
