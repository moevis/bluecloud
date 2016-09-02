chcp 65001

echo OFF
SET SERVER={server}
SET PASSWD={password}
SET METHOD={method}
SET PORT={port}
SET RATIO={ratio}

echo %date%
echo         SERVER: %SERVER%
echo         METHOD: %METHOD%
echo     LOCAL PORT: 1080
echo BANDWITH RATIO: %RATIO%
{extra}
echo ===================================

sslocal -s %SERVER% -p %PORT% -l 1080 -k %PASSWD% -m %METHOD%