%global pkg_name plexus-i18n
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

# Copyright (c) 2000-2007, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define parent plexus
%define subname i18n

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.0
Release:        0.6.b10.4.12%{?dist}
Summary:        Plexus I18N Component
License:        ASL 2.0
URL:            http://plexus.codehaus.org/plexus-components/plexus-i18n
Source0:        plexus-i18n-1.0-beta-10-src.tar.bz2
# svn export http://svn.codehaus.org/plexus/plexus-components/tags/plexus-i18n-1.0-beta-10/
# tar cjf plexus-i18n-1.0-beta-10-src.tar.bz2 plexus-i18n-1.0-beta-10/

BuildArch:      noarch
BuildRequires:  %{?scl_prefix_java_common}javapackages-tools
BuildRequires:  %{?scl_prefix_java_common}ant >= 0:1.6
BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  maven30-maven-resources-plugin
BuildRequires:  maven30-maven-doxia-sitetools
BuildRequires:  maven30-plexus-containers-component-metadata
BuildRequires:  maven30-plexus-classworlds >= 0:1.1
BuildRequires:  maven30-plexus-containers-container-default
BuildRequires:  maven30-plexus-utils

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.


%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
Javadoc for %{pkg_name}.


%prep
%setup -q -n plexus-i18n-1.0-beta-10
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%pom_add_dep org.codehaus.plexus:plexus-container-default:1.0-alpha-9-stable-1

# use plexus-component-metadata instead of old plugin
%pom_remove_plugin :plexus-maven-plugin
%pom_add_plugin org.codehaus.plexus:plexus-component-metadata pom.xml "
         <executions>
           <execution>
             <goals>
              <goal>generate-metadata</goal>
             </goals>
           </execution>
         </executions>
"

%mvn_file : %{parent}/%{subname}
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/plexus
%dir %{_javadir}/plexus
%files javadoc -f .mfiles-javadoc

%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.0-0.6.b10.4.12
- maven33 rebuild

* Fri Jan 16 2015 Michal Srb <msrb@redhat.com> - 1.0-0.6.b10.4.11
- Fix directory ownership

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.6.b10.4.10
- Rebuild to fix provides

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.0-0.6.b10.4.9
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.0-0.6.b10.4.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.6.b10.4.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.6.b10.4.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.6.b10.4.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.6.b10.4.4
- Remove requires on java

* Mon Feb 17 2014 Michal Srb <msrb@redhat.com> - 1.0-0.6.b10.4.3
- SCL-ize BR/R

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.6.b10.4.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.6.b10.4.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0-0.6.b10.4
- Mass rebuild 2013-12-27

* Fri Aug 16 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-0.5.b10.4
- Migrate away from mvn-rpmbuild (#997436)

* Fri Jul 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.4.b10.4
- Remove workaround for rpm bug #646523

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.4.b10.3
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.b10.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-0.3.b10.2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Nov 22 2012 Jaromir Capik <jcapik@redhat.com> - 1.0-0.2.b10.2
- Migration to plexus-containers-container-default

* Mon Nov 12 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.1.b10.2
- Fix Release tag

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.b10.2.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 06 2012 Jaromir Capik <jcapik@redhat.com> - 1.0-0.b10.2.4
- Missing plexus-container-default dependency added in the pom.xml

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.b10.2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 28 2011 Jaromir Capik <jcapik@redhat.com> - 1.0-0.b10.2.2
- Migration to maven3
- Migration from plexus-maven-plugin to plexus-containers-component-metadata
- Minor spec file changes according to the latest guidelines

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.b10.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 23 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.b10.2
- BR java-devel 1.6.0.

* Wed Dec 23 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.b10.1
- Update to beta 10.
- Drop gcj and fix BRs.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.b6.5.3.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 18 2009 Deepak Bhole <dbhole@redhat.com> - 0:1.0-0.b6.5.3.2
- Added pom.xml and components.xml to META-INF

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.b6.5.3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.0-0.b6.5.3
- drop repotag

* Wed Feb 27 2008 Deepak Bhole <dbhole@redhat.com> - 0:1.0-0.b6.5jpp.2
- Build with maven

* Tue Jan 22 2008 Permaine Cheung <pcheung@redhat.com> - 0:1.0-0.b6.5jpp.1
- Update to the same version as upstream

* Thu Apr 26 2007 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.b6.5jpp
- Reupload to fix metadata

* Sat Mar 24 2007 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.b6.4jpp
- Optionally build without maven
- Add gcj_support option

* Mon Feb 19 2007 Tania Bento <tbento@redhat.com> - 0:1.0-0.b6.3jpp.1
- Fixed %%Release tag.
- Changed the svn URL.
- Added instruction on how to tar the files extracted with svn export.
- Fixed %%BuildRoot tag.
- Removed %%post and %%postun sections for javadoc and made necessary changes.
- Added gcj support.

* Wed Oct 25 2006 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.b6.3jpp
- Fix components.xml

* Tue May 30 2006 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.b6.2jpp
- First JPP-1.7 release
- Drop maven support - waiting for maven2

* Mon Nov 07 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.b6.1jpp
- First JPackage build
