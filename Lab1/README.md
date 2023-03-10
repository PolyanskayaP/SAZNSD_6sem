lab1
================
ppolina353@yandex.ru

## Quarto

Quarto enables you to weave together content and executable code into a
finished document. To learn more about Quarto see <https://quarto.org>.

## Running Code

When you click the **Render** button a document will be generated that
includes both content and the output of embedded code. You can embed
code like this:

``` bash
uname -r
```

    4.4.0-19041-Microsoft

``` bash
uname -a
```

    Linux polyanskaya 4.4.0-19041-Microsoft #2311-Microsoft Tue Nov 08 17:09:00 PST 2022 x86_64 x86_64 x86_64 GNU/Linux

``` bash
lsb_release -a
```

    No LSB modules are available.
    Distributor ID: Ubuntu
    Description:    Ubuntu 20.04 LTS
    Release:    20.04
    Codename:   focal

``` bash
cat /proc/cpuinfo | grep "model name"
```

    model name  : AMD Ryzen 5 5500U with Radeon Graphics         
    model name  : AMD Ryzen 5 5500U with Radeon Graphics         
    model name  : AMD Ryzen 5 5500U with Radeon Graphics         
    model name  : AMD Ryzen 5 5500U with Radeon Graphics         
    model name  : AMD Ryzen 5 5500U with Radeon Graphics         
    model name  : AMD Ryzen 5 5500U with Radeon Graphics         
    model name  : AMD Ryzen 5 5500U with Radeon Graphics         
    model name  : AMD Ryzen 5 5500U with Radeon Graphics         
    model name  : AMD Ryzen 5 5500U with Radeon Graphics         
    model name  : AMD Ryzen 5 5500U with Radeon Graphics         
    model name  : AMD Ryzen 5 5500U with Radeon Graphics         
    model name  : AMD Ryzen 5 5500U with Radeon Graphics         

``` bash
dmesg | tail -n 30
```

    [    0.021270]  Microsoft 4.4.0-19041.2311-Microsoft 4.4.35
    [    0.099132] <3>init: (1) ERROR: ConfigInitializeCommon:665: Failed to mount /usr/lib/wsl/drive
    [    0.099136] : 19
    [    0.099249] <3>init: (1) ERROR: ConfigInitializeCommon:665: Failed to mount /usr/lib/wsl/lib
    [    0.099252] 19
