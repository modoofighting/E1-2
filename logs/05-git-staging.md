# 첫 커밋 대상 준비

실행 위치: Windows PowerShell, `C:\all in one\e1-2` · 사용자 제공 실행 내용

## README와 .gitignore 준비

<pre style="border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; background: #f6f8fa;"><code># 다음 커밋에 포함할 README와 .gitignore 선택
<span style="color: #0969da;">git add README.md .gitignore</span></code></pre>

```text
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
```

Git이 줄바꿈 방식에 대해 표시한 경고입니다. LF와 CRLF는 줄 끝을 표현하는 방식입니다. 경고만 표시됐으며, 어떤 내용이 스테이징됐는지는 `git diff --cached --name-only`로 별도 확인합니다. 이 기록은 아직 커밋이 생성됐다는 뜻이 아닙니다.
## 로그 추가와 스테이징 목록 확인

<pre style="border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; background: #f6f8fa;"><code># 로그 파일을 다음 커밋 대상으로 선택
<span style="color: #0969da;">git add logs/</span></code></pre>

**실제 출력:** 사용자 PowerShell에서 `02-environment-check.md`, `03-git-local-config.md`, `04-gitignore.md`, `05-git-staging.md`, `progress.md` 각각에 대해 LF가 나중에 CRLF로 바뀔 수 있다는 경고가 표시됐습니다. 일부 줄은 터미널 표시에서 공백 없이 이어져 보였습니다.

<pre style="border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; background: #f6f8fa;"><code># 스테이징된 파일 이름만 확인
<span style="color: #0969da;">git diff --cached --name-only</span></code></pre>

```text
.gitignore
README.md
logs/02-environment-check.md
logs/03-git-local-config.md
logs/04-gitignore.md
logs/05-git-staging.md
logs/progress.md
```

`--cached`는 커밋을 위해 준비한 내용을, `--name-only`는 파일 이름만 표시. 이 목록은 사용자 명령 실행 당시의 상태. 이후 이 로그와 README가 수정됐으므로, 최신 내용을 같은 커밋에 포함하려면 두 파일을 다시 `git add`필요. 아직 커밋은 확인되지 않았다.