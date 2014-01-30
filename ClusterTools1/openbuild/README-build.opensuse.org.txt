
Build files for build.opensuse.org are placed
beyond
~/private/build_opensuse_de/home:fmherschel/wow

If you update the package here copy the tar-archive and
spec file to the above location and run

osc ci -m "<comment>" wow.spec wow-XXX.tgz

You can control the build results using

osc results

For both osc commands you should be in the directory
metioned above
