1  pascal -ret16 Ctl3dGetVer() Ctl3dGetVer16
2  pascal -ret16 Ctl3dSubclassDlg(word word) Ctl3dSubclassDlg16
3  pascal -ret16 Ctl3dSubclassCtl(word) Ctl3dSubclassCtl16
4  pascal -ret16 Ctl3dCtlColor(word long) Ctl3dCtlColor16
5  pascal -ret16 Ctl3dEnabled() Ctl3dEnabled16
6  pascal -ret16 Ctl3dColorChange() Ctl3dColorChange16
7  pascal BtnWndProc3d(word word word long) BtnWndProc3d16
8  pascal EditWndProc3d(word word word long) EditWndProc3d16
9  pascal ListWndProc3d(word word word long) ListWndProc3d16
10 pascal ComboWndProc3d(word word word long) ComboWndProc3d16
11 pascal StaticWndProc3d(word word word long) StaticWndProc3d16
12 pascal -ret16 Ctl3dRegister(word) Ctl3dRegister16
13 pascal -ret16 Ctl3dUnregister(word) Ctl3dUnregister16
16 pascal -ret16 Ctl3dAutoSubclass(word) Ctl3dAutoSubclass16
17 pascal Ctl3dDlgProc(word word word long) Ctl3dDlgProc16
18 pascal -ret16 Ctl3dCtlColorEx(word word long) Ctl3dCtlColorEx16
19 pascal -ret16 Ctl3dSetStyle(word long word) Ctl3dSetStyle16
20 pascal Ctl3dDlgFramePaint(word word word long) Ctl3dDlgFramePaint16
21 pascal -ret16 Ctl3dSubclassDlgEx(word long) Ctl3dSubclassDlgEx16
22 pascal -ret16 Ctl3dWinIniChange() Ctl3dWinIniChange16
23 pascal -ret16 Ctl3dIsAutoSubclass() Ctl3dIsAutoSubclass16
24 pascal -ret16 Ctl3dUnAutoSubclass() Ctl3dUnAutoSubclass16
25 pascal -ret16 Ctl3dSubclassCtlEx(word word) Ctl3dSubclassCtlEx16
26 pascal -ret16 Ctl3dUnsubclassCtl(word) Ctl3dUnsubclassCtl16
27 pascal -ret16 Ctl3dAutoSubclassEx(word long) Ctl3dAutoSubclassEx16

@ stdcall -arch=win32 Ctl3dGetVer16()
@ stdcall -arch=win32 Ctl3dSubclassDlg16(long long)
@ stdcall -arch=win32 Ctl3dSubclassCtl16(long)
@ stdcall -arch=win32 Ctl3dCtlColor16(long long)
@ stdcall -arch=win32 Ctl3dEnabled16()
@ stdcall -arch=win32 Ctl3dColorChange16()
@ stdcall -arch=win32 BtnWndProc3d16(long long long long)
@ stdcall -arch=win32 EditWndProc3d16(long long long long)
@ stdcall -arch=win32 ListWndProc3d16(long long long long)
@ stdcall -arch=win32 ComboWndProc3d16(long long long long)
@ stdcall -arch=win32 StaticWndProc3d16(long long long long)
@ stdcall -arch=win32 Ctl3dRegister16(long)
@ stdcall -arch=win32 Ctl3dUnregister16(long)
@ stdcall -arch=win32 Ctl3dAutoSubclass16(long)
@ stdcall -arch=win32 Ctl3dDlgProc16(long long long long)
@ stdcall -arch=win32 Ctl3dCtlColorEx16(long long long)
@ stdcall -arch=win32 Ctl3dSetStyle16(long long long)
@ stdcall -arch=win32 Ctl3dDlgFramePaint16(long long long long)
@ stdcall -arch=win32 Ctl3dSubclassDlgEx16(long long)
@ stdcall -arch=win32 Ctl3dWinIniChange16()
@ stdcall -arch=win32 Ctl3dIsAutoSubclass16()
@ stdcall -arch=win32 Ctl3dUnAutoSubclass16()
@ stdcall -arch=win32 Ctl3dSubclassCtlEx16(long long)
@ stdcall -arch=win32 Ctl3dUnsubclassCtl16(long)
@ stdcall -arch=win32 Ctl3dAutoSubclassEx16(long long)
