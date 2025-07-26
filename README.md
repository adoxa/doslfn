# DOSLFN

Provide the long file name (LFN) API for DOS programs.

## Requirements

* DOS 4+ (tested)
* 386+ (assumed)

## Build

You will need TASM (IDEAL mode); I use v4.1, along with TLINK v7.1.30.1.
I have not updated the `makefile`, using a Windows batch file to build
"manually", equivalent to:

    tasm -m5 -t doslfn.asm,doslfn%1.obj,doslfn%1.lst
    tlink /3 /t doslfn%1.obj

The argument is `ms` for the MS-DOS build (equates modified manually) and
nothing otherwise.
