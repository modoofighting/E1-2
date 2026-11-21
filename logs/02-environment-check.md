# Python·Git과 작업 폴더 확인

기록일: 2026-11-11 (KST) · 실행 위치: Windows PowerShell, `C:\all in one\e1-2`

## Python 버전 확인

<pre style="border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; background: #f6f8fa;"><code># Python 버전 확인
<span style="color: #0969da;">python --version</span></code></pre>

```text
Python 3.11.9
```

`--version`은 실행되는 Python의 버전을 표시합니다. 과제의 Python 3.10 이상 조건을 충족합니다.

## Git 버전 확인

<pre style="border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; background: #f6f8fa;"><code># Git 버전 확인
<span style="color: #0969da;">git --version</span></code></pre>

```text
git version 2.55.0.windows.1
```

Git 명령이 실행되고 설치된 버전이 표시됐습니다.

## 작업 폴더 존재 여부 확인

<pre style="border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; background: #f6f8fa;"><code># E1-2 폴더 존재 여부 확인
<span style="color: #0969da;">test-path "C:\all in one\e1-2"</span></code></pre>

```text
True
```

`Test-Path`의 `True`는 지정한 경로가 존재한다는 뜻입니다.

## 작업 폴더 이동 및 위치 확인

<pre style="border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; background: #f6f8fa;"><code># E1-2 폴더로 이동
<span style="color: #0969da;">set-location "C:\all in one\e1-2"</span>
# 현재 작업 위치 확인
<span style="color: #0969da;">Get-Location</span></code></pre>

```text
Path
----
C:\all in one\e1-2
```

`Set-Location`은 작업 위치를 변경하며, 성공 시 별도 출력을 표시하지 않을 수 있습니다. `Get-Location`으로 E1-2 폴더에 있음을 확인했습니다.

## 숨김 항목을 포함한 폴더 목록 확인

<pre style="border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; background: #f6f8fa;"><code># 숨김 항목을 포함해 현재 폴더의 파일과 디렉터리 확인
<span style="color: #0969da;">Get-ChildItem -Force</span></code></pre>

```text
    디렉터리: C:\all in one\e1-2

Mode                 LastWriteTime Length
----                 ------------- ------
d--h--      2026-11-11   오후 7:28
d-----      2026-11-11   오후 7:08
d-----      2026-11-11   오후 7:03
-a----      2026-11-10   오후 1:06   8261
-a----      2026-11-10  오후 12:32   9013
-a----      2026-11-10  오후 12:32  14655
-a----      2026-11-11   오후 7:44  63610
-a----      2026-11-11  오후 10:09  68781
```

`Get-ChildItem`은 항목 목록을 표시하고 `-Force`는 숨김 항목도 포함합니다. 제공된 출력에는 항목 이름 열이 보이지 않아 위에 보이는 내용만 기록했습니다. 날짜와 길이는 해당 실행 시점의 값입니다.