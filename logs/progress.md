# E1-2 진행 로그

기록일: 2026-11-11 (KST). 사용자 제공 출력과 Codex 재확인 결과를 각 항목에 표시합니다.

#### 3-1. Python 실행 오류 확인

<pre style="border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; background: #f6f8fa; white-space: pre-wrap; overflow-wrap: anywhere; color: #1f2328;"><code style="color: inherit;"># 작업 폴더: C:\all in one\e1-2
# Python 버전 확인
<span style="color: #0969da;">python --version</span></code></pre>

```text
error: uv trampoline failed to spawn Python child process
  Caused by: entity not found (os error 2)
```

사용자가 보낸 실제 오류입니다. 당시 `python` 명령은 uv가 만든 실행 파일을 선택했고, 이 실행 파일이 하위 Python 프로세스를 시작하지 못했습니다. 이 결과만으로 Python이 설치되지 않았다고 판단할 수는 없습니다.

#### 3-2. Python 실행 경로 조정 및 버전 확인

<pre style="border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; background: #f6f8fa; white-space: pre-wrap; overflow-wrap: anywhere; color: #1f2328;"><code style="color: inherit;"># 작업 폴더: C:\all in one\e1-2
# 앞서 임시로 등록한 python 함수 제거
<span style="color: #0969da;">Remove-Item Function:\python -ErrorAction SilentlyContinue</span>
# 정상 설치된 Python 3.11 경로를 현재 창의 PATH 맨 앞에 추가
<span style="color: #0969da;">$env:Path = &quot;$env:LOCALAPPDATA\Programs\Python\Python311;$env:Path&quot;</span>
# 실제로 실행되는 Python 버전 확인
<span style="color: #0969da;">python --version</span></code></pre>

```text
Python 3.11.9
```

사용자 PowerShell에서 위 명령과 출력을 확인했습니다. `Function:\python`은 같은 이름의 PowerShell 함수이며, 이를 제거하면 외부 실행 파일을 찾습니다. PATH는 실행 파일을 찾는 폴더 목록입니다. Python 3.11 경로를 앞에 두어 이 설치를 먼저 사용하게 했습니다. 버전 3.11.9는 과제의 Python 3.10 이상 조건을 충족합니다. 이 명령의 `$env:Path` 변경은 현재 창에 적용됩니다. 별도로 Codex가 사용자 PATH 설정도 백업 후 수정하고 Python 3.11.9 및 JSON 실행을 확인했습니다.

### 4. 로컬 Git 저장소 초기화

#### 4-1. 현재 작업 위치 확인

<pre style="border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; background: #f6f8fa; white-space: pre-wrap; overflow-wrap: anywhere; color: #1f2328;"><code style="color: inherit;"># 현재 작업 폴더 확인
<span style="color: #0969da;">Get-Location</span></code></pre>

```text
Path
----
C:\all in one\e1-2
```

`Get-Location`은 현재 PowerShell의 작업 경로를 보여줍니다. E1-1과 별개인 E1-2 폴더에서 Git 명령을 실행하고 있음을 확인했습니다.

#### 4-2. 초기화 전 Git 상태 확인

<pre style="border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; background: #f6f8fa; white-space: pre-wrap; overflow-wrap: anywhere; color: #1f2328;"><code style="color: inherit;"># 작업 폴더: C:\all in one\e1-2
# Git 저장소인지 확인
<span style="color: #0969da;"> git status -sb</span></code></pre>

```text
fatal: not a git repository (or any of the parent directories): .git
```

초기화 전에 사용자가 확인한 실제 출력입니다. 이 폴더와 상위 폴더에서 Git 저장소를 찾지 못했다는 뜻입니다. 다음 단계에서 `git init`으로 저장소를 만들었습니다.

#### 4-3. main 브랜치로 Git 저장소 초기화

<pre style="border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; background: #f6f8fa; white-space: pre-wrap; overflow-wrap: anywhere; color: #1f2328;"><code style="color: inherit;"># 작업 폴더: C:\all in one\e1-2
# 현재 폴더에 Git 저장소를 만들고 첫 브랜치를 main으로 지정
<span style="color: #0969da;">git init -b main</span></code></pre>

```text
Initialized empty Git repository in C:/all in one/e1-2/.git/
```

`git init`은 현재 폴더에 `.git`을 만들고 변경 이력 관리를 시작합니다. `-b main`은 첫 브랜치 이름을 지정합니다. 이 출력은 로컬 저장소가 만들어졌다는 뜻이며, 커밋 생성과 GitHub 업로드는 별도 작업입니다.

#### 4-4. 현재 브랜치와 추적되지 않은 파일 확인

<pre style="border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; background: #f6f8fa; white-space: pre-wrap; overflow-wrap: anywhere; color: #1f2328;"><code style="color: inherit;"># Codex가 문서 정리 시 PowerShell에서 재확인
# 작업 폴더: C:\all in one\e1-2
# 한글 파일명을 그대로 표시하고 브랜치&#183;파일 상태 확인
<span style="color: #0969da;">git -c core.quotepath=false status -sb</span></code></pre>

```text
## No commits yet on main
?? "# 🎯 과제 완전 분해 가이드.txt"
?? "# 📄 README.md 완성본.txt"
?? README.md
?? docs/
?? "e1-2 컴퓨터에게 명령 내리는 말(파이썬) 처음 배우기.txt"
?? logs/
```

사용자가 초기화 직후 보낸 출력에는 `## No commits yet on main`과 기존 파일 네 개가 표시됐습니다. 위 블록은 문서 정리 중 Codex가 다시 실행한 실제 출력으로, 새로 준비한 `docs/`와 `logs/`도 포함합니다. `-s`는 짧은 상태 표시, `-b`는 브랜치 정보 표시입니다. `??`는 아직 추적되지 않은 파일 또는 폴더입니다. `-c core.quotepath=false`는 이번 명령에서만 한글 파일명 이스케이프 표시를 끕니다. 사용자 원래 출력의 `\360`, `\352` 등은 파일명 바이트를 이스케이프해서 보여준 것이며 파일 손상을 뜻하지 않습니다.

