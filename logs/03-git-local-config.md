# 로컬 Git 저장소 및 작성자 설정

실행 위치: Windows PowerShell, `C:\all in one\e1-2` · 사용자 제공 실행 내용

## 저장소 초기화 상태 확인

<pre style="border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; background: #f6f8fa;"><code># PowerShell에서 실행
# 현재 폴더의 Git 저장소 초기화
git init</code></pre>

```text
Reinitialized existing Git repository in C:/all in one/e1-2/.git/
```

이미 `git init -b main`으로 만든 로컬 저장소가 있어 Git이 기존 저장소를 다시 초기화했다고 표시했습니다. 이 출력은 커밋을 만들었다는 의미는 아닙니다.

## 이 저장소의 커밋 작성자 설정

<pre style="border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; background: #f6f8fa;"><code># PowerShell에서 실행
# 현재 저장소에 커밋 작성자 이름을 지정
git config --local user.name "modoofighting"
# 현재 저장소에 커밋 작성자 이메일을 지정
git config --local user.email "&lt;이메일 비공개&gt;"</code></pre>

**실제 출력:** 없음.

사용자가 입력한 이메일 주소는 로그에서 비공개로 표시했습니다. 위 이메일은 가림 처리한 표기이므로 그대로 실행하는 명령이 아닙니다. `--local`은 현재 저장소에만 설정하며 GitHub 인증과는 별개입니다. 실제 커밋에 포함될 값은 설정 조회 후 확인해야 합니다.
## 작성자 설정과 브랜치 상태 확인

<pre style="border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; background: #f6f8fa;"><code># PowerShell에서 실행: C:\all in one\e1-2
# 이 저장소의 작성자 이름 확인
<span style="color: #0969da;">git config --local --get user.name</span></code></pre>

```text
modoofighting
```

이름은 사용자가 PowerShell에서 확인한 실제 출력입니다. `--get` 뒤에는 값이 아니라 설정 항목 이름을 적습니다.

<pre style="border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; background: #f6f8fa;"><code># PowerShell에서 실행
# 이 저장소의 작성자 이메일 확인
<span style="color: #0969da;">git config --local --get user.email</span></code></pre>

사용자 PowerShell에서 설정한 이메일이 조회됐습니다. 로그에는 주소를 공개하지 않기 위해 실제 출력을 생략합니다. Git 커밋에는 설정된 이메일이 포함됩니다.

<pre style="border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; background: #f6f8fa;"><code># PowerShell에서 실행
# 현재 브랜치와 파일 상태를 간단히 확인
<span style="color: #0969da;">git status -sb</span></code></pre>

```text
## No commits yet on main
```

위는 사용자 제공 출력 중 브랜치 상태 한 줄입니다. 이어서 추적되지 않은 파일·폴더가 `??`로 표시됐습니다. `-s`는 짧은 형식, `-b`는 브랜치 정보 표시입니다. 한글 파일명 일부는 Git의 이스케이프 표기로 보였습니다.

`--local` 설정은 현재 Git 저장소에 적용됩니다. 저장소 안에서 하위 폴더로 이동해도 같은 저장소 설정을 사용합니다. 별도 저장소에서는 그 저장소의 설정 또는 전역 설정을 사용합니다.
## 전역 설정과 로컬 설정

`--local`은 현재 저장소에 적용되고, `--global`은 현재 Windows 사용자의 Git 저장소에 적용되는 기본값입니다. 같은 항목에 로컬 값이 있으면 전역 값보다 우선합니다. 저장소의 하위 폴더로 이동할 때마다 다시 설정할 필요는 없습니다.

<pre style="border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; background: #f6f8fa;"><code># PowerShell에서 실행 예정: 전역 작성자 정보 확인
<span style="color: #0969da;">git config --global --get user.name</span>
<span style="color: #0969da;">git config --global --get user.email</span></code></pre>

**실제 출력:** 아직 확인하지 않았습니다. 설정된 값이 없으면 출력이 없습니다. 확인 후 실제 결과를 기록합니다.