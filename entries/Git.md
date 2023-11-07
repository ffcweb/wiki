![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Git-logo.svg/200px-Git-logo.svg.png "Logo Title Text 1")
___
# Git

Git is a version control tool that can be used to keep track of versions of a software project.

# GitHub

- GitHub is an online service for hosting git repositories.

- Git (/ɡɪt/)[8] is a distributed version control system[9] that tracks changes in any set of computer files, usually used for coordinating work among programmers who are collaboratively developing source code during software development. Its goals include speed, data integrity, and support for distributed, non-linear workflows (thousands of parallel branches running on different computers).[10][11][12]

- Git was originally authored by Linus Torvalds in 2005 for development of the Linux kernel, with other kernel developers contributing to its initial development.[13] Since 2005, Junio Hamano has been the core maintainer. As with most other distributed version control systems, and unlike most client–server systems, every Git directory on every computer is a full-fledged repository with complete history and full version-tracking abilities, independent of network access or a central server.[14] Git is free and open-source software shared under the GPL-2.0-only license.

- Since its creation, Git has become the most popular distributed version control system, with nearly 95% of developers reporting it as their primary version control system as of 2022.[15] There are many popular offerings of Git repository services, including GitHub, SourceForge, Bitbucket and GitLab.[16][17][18][19][20]

##  History
- Git development was started by Torvalds in April 2005 when the proprietary source-control management (SCM) system used for Linux kernel development since 2002, BitKeeper, revoked its free license for Linux development.[21][22] The copyright holder of BitKeeper, Larry McVoy, claimed that Andrew Tridgell had created SourcePuller by reverse engineering the BitKeeper protocols.[23] The same incident also spurred the creation of another version-control system, Mercurial.

- Torvalds wanted a distributed system that he could use like BitKeeper, but none of the available free systems met his needs. He cited an example of a source-control management system needing 30 seconds to apply a patch and update all associated metadata, and noted that this would not scale to the needs of Linux kernel development, where synchronizing with fellow maintainers could require 250 such actions at once. For his design criterion, he specified that patching should take no more than three seconds, and added three more goals:[10]

- Take the Concurrent Versions System (CVS) as an example of what not to do; if in doubt, make the exact opposite decision.[12]
Support a distributed, BitKeeper-like workflow.[12]
Include very strong safeguards against corruption, either accidental or malicious.[11]
These criteria eliminated every version-control system in use at the time, so immediately after the 2.6.12-rc2 Linux kernel development release, Torvalds set out to write his own.[12]

- The development of Git began on 3 April 2005.[24] Torvalds announced the project on 6 April and became self-hosting the next day.[24][25] The first merge of multiple branches took place on 18 April.[26] Torvalds achieved his performance goals; on 29 April, the nascent Git was benchmarked recording patches to the Linux kernel tree at a rate of 6.7 patches per second.[27] On 16 June, Git managed the kernel 2.6.12 release.[28]

- Torvalds turned over maintenance on 26 July 2005 to Junio Hamano, a major contributor to the project.[29] Hamano was responsible for the 1.0 release on 21 December 2005.[30]

##  Naming
- Torvalds sarcastically quipped about the name git (which means "unpleasant person" in British English slang): "I'm an egotistical bastard, and I name all my projects after myself. First 'Linux', now 'git'."[31][32] The man page describes Git as "the stupid content tracker".[33]

- The read-me file of the source code elaborates further:[34]

- "git" can mean anything, depending on your mood.

- Random three-letter combination that is pronounceable, and not actually used by any common UNIX command. The fact that it is a mispronunciation of "get" may or may not be relevant.
- Stupid. Contemptible and despicable. Simple. Take your pick from the dictionary of slang.
"Global information tracker": you're in a good mood, and it actually works for you. Angels sing, and a light suddenly fills the room.
- "Goddamn idiotic truckload of sh*t": when it breaks.
- The source code for Git refers to the program as "the information manager from hell".