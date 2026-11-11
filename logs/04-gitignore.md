# .gitignore 작성 및 상태 확인

실행 위치: Windows PowerShell, `C:\all in one\e1-2`

## VS Code에서 파일 생성 및 저장

1. VS Code 탐색기에서 `e1-2` 폴더의 새 파일을 선택했습니다.
2. 파일 이름을 `.gitignore`로 지정했습니다. 처음에 쉼표로 시작한 이름을 점으로 고쳤으며, 최종 저장 경로는 `C:\all in one\e1-2\.gitignore`입니다.
3. 아래 규칙을 입력하고 저장했습니다. 다음 내용은 터미널 명령이 아니라 `.gitignore` 파일의 내용입니다.
4. 이후 PowerShell에서 `git status -sb`로 `?? .gitignore`를 확인했습니다.

**저장한 파일의 실제 내용:**

```gitignore
__pycache__/
*.py[cod]

.venv/
venv/

.DS_Store
Thumbs.db
```

`__pycache__/`와 `*.py[cod]`는 Python 캐시 및 관련 확장자를, `.venv/`와 `venv/`는 가상환경 폴더를 제외하는 규칙입니다. `.DS_Store`와 `Thumbs.db`는 운영체제 임시 파일입니다. `*.py[cod]`에는 `.pyd`도 포함되며, 직접 배포할 `.pyd`가 필요한 경우 규칙을 검토해야 합니다.

<pre style="border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; background: #f6f8fa;"><code># PowerShell에서 실행
# 현재 브랜치와 추적되지 않은 파일 확인
<span style="color: #0969da;">git status -sb</span></code></pre>

```text
## No commits yet on main
?? .gitignore
```

