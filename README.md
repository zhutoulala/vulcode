# vulcode
vulnerability source code patch collection

This repo is used to collect c++ source code that introduced or fixed known CVEs. The source code will be analyzed and feeded to [vulnscan](http://vulnscan.us)

This repo also contains a simple python script get_cve_patch.py, that could be used to download source code patches for all known CVEs, if the patches are available on github.

Usage of the script:
`python get_cve_patch.py [output folder]`

The outputs can be found under [unclassified](unclassified) folder as well.