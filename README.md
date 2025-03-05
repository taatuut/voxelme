# voxelme
voxelme

## Repo
`git clone https://github.com/taatuut/voxelme.git`

## Context
Testing https://github.com/iosefa/PyForestScan after getting link to post https://www.linkedin.com/posts/gregcocks_gis-spatial-mapping-activity-7295959387251060737-H8bd from Hugo

Developed on macOS.

## Prerequisites

### Environment
If not done, copy `sample.env` to `.env` and edit the variables to contain relevant values.

Open a terminal and source environment variables if any.

```
source .env
```

### Python
Use `Python 3.10+`.

To create and source a Python virtual environment like  `~/.venv` in the Terminal run:

```
mkdir -p ~/.venv
python3 -m venv ~/.venv
source ~/.venv/bin/activate
```

Using the Terminal install Python modules (optional: update `pip`) adn source the environment variables.

To install module `pyforestscan` requires additional modules like `rasterio`, `gdal`, `pdal` and others.

Install gdal and pdal first:

```
brew install gdal
brew install pdal
```

```
python3 -m pip install --upgrade pip
python3 -m pip install pyforestscan
```

## Steps

Download AHN LAZ data van [L1]

Test with example code from [L2]

Run script `python3 ezlaz.py`

### Issues
- The output geotiff cannot be opened in macOS Preview, can *sometimes* with [L3] and *sometimes* see raster but *sometimes* problem and extents seem to small?
- The script does visualize output with plot_metric, but this (matplotlib?) plot blocks script from further processing.
- The process was automatically killed with message `zsh: killed     python3 ezlaz.py`, assume because memory usage got too high with more than 135GB. Running `codesign --sign - --force PATH_TO_YOUR_ISSUE_BINARY` is not the solution for this issue. Try in `bash` instead on `zsh`.

## Useful commands

`sudo find / -type f -name "*.mmap" 2>/dev/null` where `2>/dev/null` suppresses permission denied errors.

`find /var/folders -type f -name "*.mmap" 2>/dev/null`

`find /var/folders -type f -name "*.mmap" 2>/dev/null -delete`

## Links

[L1] https://www.ahn.nl/dataroom

[L2] https://github.com/iosefa/PyForestScan

[L3] https://app.geotiff.io/

## Appendices

### Appendix pyforestscan

1) Fail without `gdal` and/or `pdal` installed.

```
python3 -m pip install pyforestscan
Collecting pyforestscan
  Downloading pyforestscan-0.2.2-py3-none-any.whl.metadata (5.7 kB)
Collecting rasterio>=1.3.11 (from pyforestscan)
  Downloading rasterio-1.4.3-cp313-cp313-macosx_10_15_x86_64.whl.metadata (9.1 kB)
Collecting pdal>=3.4.5 (from pyforestscan)
  Downloading pdal-3.4.5.tar.gz (89 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting geopandas>=1.0.1 (from pyforestscan)
  Downloading geopandas-1.0.1-py3-none-any.whl.metadata (2.2 kB)
Collecting pyproj>=3.6.1 (from pyforestscan)
  Downloading pyproj-3.7.1-cp313-cp313-macosx_13_0_x86_64.whl.metadata (31 kB)
Requirement already satisfied: shapely>=2.0.6 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from pyforestscan) (2.0.7)
Requirement already satisfied: pandas>=2.2.2 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from pyforestscan) (2.2.3)
Requirement already satisfied: numpy>=2.1.1 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from pyforestscan) (2.2.2)
Collecting matplotlib>=3.9.2 (from pyforestscan)
  Using cached matplotlib-3.10.0-cp313-cp313-macosx_10_13_x86_64.whl.metadata (11 kB)
Requirement already satisfied: scipy>=1.14.1 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from pyforestscan) (1.15.1)
Collecting pyogrio>=0.7.2 (from geopandas>=1.0.1->pyforestscan)
  Downloading pyogrio-0.10.0-cp313-cp313-macosx_12_0_x86_64.whl.metadata (5.5 kB)
Requirement already satisfied: packaging in /Users/emilzegers/.venv/lib/python3.13/site-packages (from geopandas>=1.0.1->pyforestscan) (24.2)
Requirement already satisfied: contourpy>=1.0.1 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from matplotlib>=3.9.2->pyforestscan) (1.3.1)
Requirement already satisfied: cycler>=0.10 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from matplotlib>=3.9.2->pyforestscan) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from matplotlib>=3.9.2->pyforestscan) (4.56.0)
Requirement already satisfied: kiwisolver>=1.3.1 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from matplotlib>=3.9.2->pyforestscan) (1.4.8)
Requirement already satisfied: pillow>=8 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from matplotlib>=3.9.2->pyforestscan) (11.1.0)
Requirement already satisfied: pyparsing>=2.3.1 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from matplotlib>=3.9.2->pyforestscan) (3.2.1)
Requirement already satisfied: python-dateutil>=2.7 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from matplotlib>=3.9.2->pyforestscan) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from pandas>=2.2.2->pyforestscan) (2025.1)
Requirement already satisfied: tzdata>=2022.7 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from pandas>=2.2.2->pyforestscan) (2025.1)
Requirement already satisfied: certifi in /Users/emilzegers/.venv/lib/python3.13/site-packages (from pyproj>=3.6.1->pyforestscan) (2024.12.14)
Collecting affine (from rasterio>=1.3.11->pyforestscan)
  Downloading affine-2.4.0-py3-none-any.whl.metadata (4.0 kB)
Requirement already satisfied: attrs in /Users/emilzegers/.venv/lib/python3.13/site-packages (from rasterio>=1.3.11->pyforestscan) (25.1.0)
Requirement already satisfied: click>=4.0 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from rasterio>=1.3.11->pyforestscan) (8.1.8)
Collecting cligj>=0.5 (from rasterio>=1.3.11->pyforestscan)
  Downloading cligj-0.7.2-py3-none-any.whl.metadata (5.0 kB)
Collecting click-plugins (from rasterio>=1.3.11->pyforestscan)
  Downloading click_plugins-1.1.1-py2.py3-none-any.whl.metadata (6.4 kB)
Requirement already satisfied: six>=1.5 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from python-dateutil>=2.7->matplotlib>=3.9.2->pyforestscan) (1.17.0)
Downloading pyforestscan-0.2.2-py3-none-any.whl (25 kB)
Downloading geopandas-1.0.1-py3-none-any.whl (323 kB)
Using cached matplotlib-3.10.0-cp313-cp313-macosx_10_13_x86_64.whl (8.2 MB)
Downloading pyproj-3.7.1-cp313-cp313-macosx_13_0_x86_64.whl (6.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.3/6.3 MB 4.9 MB/s eta 0:00:00
Downloading rasterio-1.4.3-cp313-cp313-macosx_10_15_x86_64.whl (21.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 21.5/21.5 MB 4.6 MB/s eta 0:00:00
Downloading cligj-0.7.2-py3-none-any.whl (7.1 kB)
Downloading pyogrio-0.10.0-cp313-cp313-macosx_12_0_x86_64.whl (16.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.4/16.4 MB 6.4 MB/s eta 0:00:00
Downloading affine-2.4.0-py3-none-any.whl (15 kB)
Downloading click_plugins-1.1.1-py2.py3-none-any.whl (7.5 kB)
Building wheels for collected packages: pdal
  Building wheel for pdal (pyproject.toml) ... error
  error: subprocess-exited-with-error
  
  × Building wheel for pdal (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [38 lines of output]
      WARNING: Minimum CMake version set as 'CMakeLists.txt' is less than 3.15. This is not supported by scikit-build-core; set manually or increase to avoid this warning.
      WARNING: Use build.verbose instead of cmake.verbose for scikit-build-core >= 0.10
      *** scikit-build-core 0.10.7 using CMake 3.31.5 (wheel)
      *** Configuring CMake...
      loading initial cache file build/cp313-cp313-macosx_15_0_x86_64/CMakeInit.txt
      -- The C compiler identification is AppleClang 16.0.0.16000026
      -- The CXX compiler identification is AppleClang 16.0.0.16000026
      -- Detecting C compiler ABI info
      -- Detecting C compiler ABI info - done
      -- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang - skipped
      -- Detecting C compile features
      -- Detecting C compile features - done
      -- Detecting CXX compiler ABI info
      -- Detecting CXX compiler ABI info - done
      -- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ - skipped
      -- Detecting CXX compile features
      -- Detecting CXX compile features - done
      -- Found Python3: /Users/emilzegers/.venv/bin/python3 (found version "3.13.2") found components: Interpreter Development NumPy Development.Module Development.Embed
      CMake Error at CMakeLists.txt:28 (find_package):
        By not providing "FindPDAL.cmake" in CMAKE_MODULE_PATH this project has
        asked CMake to find a package configuration file provided by "PDAL", but
        CMake did not find one.
      
        Could not find a package configuration file provided by "PDAL" (requested
        version 2.6) with any of the following names:
      
          PDALConfig.cmake
          pdal-config.cmake
      
        Add the installation prefix of "PDAL" to CMAKE_PREFIX_PATH or set
        "PDAL_DIR" to a directory containing one of the above files.  If "PDAL"
        provides a separate development package or SDK, be sure it has been
        installed.
      
      
      -- Configuring incomplete, errors occurred!
      
      *** CMake configuration failed
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for pdal
Failed to build pdal
ERROR: Failed to build installable wheels for some pyproject.toml based projects (pdal)
```

2) Success with `gdal` and `pdal` installed (use `brew`).

```
python3 -m pip install pyforestscan
Collecting pyforestscan
  Using cached pyforestscan-0.2.2-py3-none-any.whl.metadata (5.7 kB)
Collecting rasterio>=1.3.11 (from pyforestscan)
  Using cached rasterio-1.4.3-cp313-cp313-macosx_10_15_x86_64.whl.metadata (9.1 kB)
Collecting pdal>=3.4.5 (from pyforestscan)
  Using cached pdal-3.4.5.tar.gz (89 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting geopandas>=1.0.1 (from pyforestscan)
  Using cached geopandas-1.0.1-py3-none-any.whl.metadata (2.2 kB)
Collecting pyproj>=3.6.1 (from pyforestscan)
  Using cached pyproj-3.7.1-cp313-cp313-macosx_13_0_x86_64.whl.metadata (31 kB)
Requirement already satisfied: shapely>=2.0.6 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from pyforestscan) (2.0.7)
Requirement already satisfied: pandas>=2.2.2 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from pyforestscan) (2.2.3)
Requirement already satisfied: numpy>=2.1.1 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from pyforestscan) (2.2.2)
Collecting matplotlib>=3.9.2 (from pyforestscan)
  Using cached matplotlib-3.10.0-cp313-cp313-macosx_10_13_x86_64.whl.metadata (11 kB)
Requirement already satisfied: scipy>=1.14.1 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from pyforestscan) (1.15.1)
Collecting pyogrio>=0.7.2 (from geopandas>=1.0.1->pyforestscan)
  Using cached pyogrio-0.10.0-cp313-cp313-macosx_12_0_x86_64.whl.metadata (5.5 kB)
Requirement already satisfied: packaging in /Users/emilzegers/.venv/lib/python3.13/site-packages (from geopandas>=1.0.1->pyforestscan) (24.2)
Requirement already satisfied: contourpy>=1.0.1 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from matplotlib>=3.9.2->pyforestscan) (1.3.1)
Requirement already satisfied: cycler>=0.10 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from matplotlib>=3.9.2->pyforestscan) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from matplotlib>=3.9.2->pyforestscan) (4.56.0)
Requirement already satisfied: kiwisolver>=1.3.1 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from matplotlib>=3.9.2->pyforestscan) (1.4.8)
Requirement already satisfied: pillow>=8 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from matplotlib>=3.9.2->pyforestscan) (11.1.0)
Requirement already satisfied: pyparsing>=2.3.1 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from matplotlib>=3.9.2->pyforestscan) (3.2.1)
Requirement already satisfied: python-dateutil>=2.7 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from matplotlib>=3.9.2->pyforestscan) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from pandas>=2.2.2->pyforestscan) (2025.1)
Requirement already satisfied: tzdata>=2022.7 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from pandas>=2.2.2->pyforestscan) (2025.1)
Requirement already satisfied: certifi in /Users/emilzegers/.venv/lib/python3.13/site-packages (from pyproj>=3.6.1->pyforestscan) (2024.12.14)
Collecting affine (from rasterio>=1.3.11->pyforestscan)
  Using cached affine-2.4.0-py3-none-any.whl.metadata (4.0 kB)
Requirement already satisfied: attrs in /Users/emilzegers/.venv/lib/python3.13/site-packages (from rasterio>=1.3.11->pyforestscan) (25.1.0)
Requirement already satisfied: click>=4.0 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from rasterio>=1.3.11->pyforestscan) (8.1.8)
Collecting cligj>=0.5 (from rasterio>=1.3.11->pyforestscan)
  Using cached cligj-0.7.2-py3-none-any.whl.metadata (5.0 kB)
Collecting click-plugins (from rasterio>=1.3.11->pyforestscan)
  Using cached click_plugins-1.1.1-py2.py3-none-any.whl.metadata (6.4 kB)
Requirement already satisfied: six>=1.5 in /Users/emilzegers/.venv/lib/python3.13/site-packages (from python-dateutil>=2.7->matplotlib>=3.9.2->pyforestscan) (1.17.0)
Using cached pyforestscan-0.2.2-py3-none-any.whl (25 kB)
Using cached geopandas-1.0.1-py3-none-any.whl (323 kB)
Using cached matplotlib-3.10.0-cp313-cp313-macosx_10_13_x86_64.whl (8.2 MB)
Using cached pyproj-3.7.1-cp313-cp313-macosx_13_0_x86_64.whl (6.3 MB)
Using cached rasterio-1.4.3-cp313-cp313-macosx_10_15_x86_64.whl (21.5 MB)
Using cached cligj-0.7.2-py3-none-any.whl (7.1 kB)
Using cached pyogrio-0.10.0-cp313-cp313-macosx_12_0_x86_64.whl (16.4 MB)
Using cached affine-2.4.0-py3-none-any.whl (15 kB)
Using cached click_plugins-1.1.1-py2.py3-none-any.whl (7.5 kB)
Building wheels for collected packages: pdal
  Building wheel for pdal (pyproject.toml) ... done
  Created wheel for pdal: filename=pdal-3.4.5-cp313-cp313-macosx_15_0_x86_64.whl size=159135 sha256=166e9d3eab78be631479559e227b10109a96dad758025dd81649749d78998791
  Stored in directory: /Users/emilzegers/Library/Caches/pip/wheels/9b/79/72/fa6873b3297eba153b084e252e81cfe4b7e7d96778f96691ff
Successfully built pdal
Installing collected packages: pyproj, pyogrio, pdal, cligj, click-plugins, affine, rasterio, matplotlib, geopandas, pyforestscan
Successfully installed affine-2.4.0 click-plugins-1.1.1 cligj-0.7.2 geopandas-1.0.1 matplotlib-3.10.0 pdal-3.4.5 pyforestscan-0.2.2 pyogrio-0.10.0 pyproj-3.7.1 rasterio-1.4.3
```

## Appendix pdal

```
brew install pdal
==> Auto-updating Homebrew...
Adjust how often this is run with HOMEBREW_AUTO_UPDATE_SECS or disable with
HOMEBREW_NO_AUTO_UPDATE. Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
==> Auto-updated Homebrew!
Updated 4 taps (homebrew/services, anchore/syft, homebrew/core and homebrew/cask).
==> New Formulae
cspell           dbg-macro        dtsroll          dyff             foundry          infisical        sv2v             taskflow         visidata         xk6              zns
==> New Casks
font-boldonse                                                                                    font-bytesized
==> Deleted Installed Formulae
node@14 ✘

You have 29 outdated formulae and 2 outdated casks installed.

==> Downloading https://ghcr.io/v2/homebrew/core/pdal/manifests/2.8.3
######################################################################################################################################################################################### 100.0%
==> Fetching dependencies for pdal: aws-c-io and laszip
==> Downloading https://ghcr.io/v2/homebrew/core/aws-c-io/manifests/0.16.0
######################################################################################################################################################################################### 100.0%
==> Fetching aws-c-io
==> Downloading https://ghcr.io/v2/homebrew/core/aws-c-io/blobs/sha256:b5b20e55c91ce0038a220b8d477fa939e4154414024489328677a84f23315e1b
######################################################################################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/laszip/manifests/3.4.4
######################################################################################################################################################################################### 100.0%
==> Fetching laszip
==> Downloading https://ghcr.io/v2/homebrew/core/laszip/blobs/sha256:1eeb4c8027b05035f4fb2bb3b0fdbb3acd4b6c9844f879dc4395ab5ca0020860
######################################################################################################################################################################################### 100.0%
==> Fetching pdal
==> Downloading https://ghcr.io/v2/homebrew/core/pdal/blobs/sha256:325e064a1414f52472476b7d2e2995a0d1ce9aec1837bbb566d457e57350f1dd
######################################################################################################################################################################################### 100.0%
==> Installing dependencies for pdal: aws-c-io and laszip
==> Installing pdal dependency: aws-c-io
==> Downloading https://ghcr.io/v2/homebrew/core/aws-c-io/manifests/0.16.0
Already downloaded: /Users/emilzegers/Library/Caches/Homebrew/downloads/622d942c84dd5e2203c11ab4efb909d83e8e32485925f5e83d28b4509b375df8--aws-c-io-0.16.0.bottle_manifest.json
==> Pouring aws-c-io--0.16.0.sonoma.bottle.tar.gz
🍺  /usr/local/Cellar/aws-c-io/0.16.0: 36 files, 542.7KB
==> Installing pdal dependency: laszip
==> Downloading https://ghcr.io/v2/homebrew/core/laszip/manifests/3.4.4
Already downloaded: /Users/emilzegers/Library/Caches/Homebrew/downloads/98fe67dbb286f860f0e7bd8b9f2eb2e1770b5f799ef7ff0788e81438573ef155--laszip-3.4.4.bottle_manifest.json
==> Pouring laszip--3.4.4.sonoma.bottle.tar.gz
🍺  /usr/local/Cellar/laszip/3.4.4: 22 files, 601.7KB
==> Installing pdal
==> Pouring pdal--2.8.3.sonoma.bottle.tar.gz
🍺  /usr/local/Cellar/pdal/2.8.3: 832 files, 139.5MB
==> Running `brew cleanup pdal`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
==> Upgrading 1 dependent of upgraded formulae:
Disable this behaviour by setting HOMEBREW_NO_INSTALLED_DEPENDENTS_CHECK.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
aws-sdk-cpp 1.11.495 -> 1.11.510
==> Downloading https://ghcr.io/v2/homebrew/core/aws-sdk-cpp/manifests/1.11.510
######################################################################################################################################################################################### 100.0%
==> Checking for dependents of upgraded formulae...
==> No broken dependents found!
```