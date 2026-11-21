## 7. Git·GitHub 작업 및 README 최종 푸시
<a id="git-commands"></a>
### 7.1 과제 필수 Git 명령어

| 명령어 | 의미 | 언제 사용하는가 |
|---|---|---|
| `git init` | 현재 폴더의 Git 관리 시작 | **처음 저장소를 만들 때만** |
| `git add` | 다음 커밋에 기록할 변경 선택 | 기능 작성·검증 후 |
| `git commit` | 선택한 변경을 로컬 이력에 기록 | **의미 있는 작업 단위**마다 |
| `git push` | 로컬 커밋을 GitHub에 업로드 | 기능·README 제출 |
| `git checkout` | 브랜치 만들기·전환 | `main` 이외 기능 브랜치에서 작업 |
| `git merge` | 기능 브랜치 결과를 `main`에 합치기 | 기능 구현·테스트 후 |
| `git clone` | GitHub 저장소를 새 폴더로 복제 | 게임 제작 후 별도 폴더 실습 |
| `git pull` | 원격의 새 변경을 로컬에 받아 반영 | 복제본 변경을 원본에 동기화 |
| `git log --oneline --graph` | 커밋·분기 이력을 그래프로 보기 | 필수 증빙 스크린샷 촬영 |

과제에 명시된 **7개 기본 명령**은 `init/add/commit/push/pull/checkout/clone`이며, 브랜치 병합에는 `merge`도 반드시 사용한다.

<a id="git-commit-flow"></a>
### 7.2 처음부터 커밋을 남기는 흐름

**기존 E1-2 저장소에 이미 `.git`이 있다면 `git init`·원격 등록을 반복하지 않는다.** 새 저장소를 만들 때 아래 준비 절차를 수행하고, 기존 저장소에서는 상태 확인부터 시작한다.

```powershell
# 작업 폴더로 이동
Set-Location "C:\all in one\e1-2"

# 현재 브랜치·변경 파일·원격 주소 확인
git status -sb
git remote -v

# 완전히 새 폴더를 Git 저장소로 만들 때만(기존 저장소에서는 실행하지 않음)
# git init -b main

# 기능 구현·검증 후 관련 파일만 스테이징
git add main.py
# 다음 커밋에 들어갈 실제 내용을 검토
git diff --cached
# 실제 변경이 준비된 경우에만 커밋
git commit -m "feat: implement quiz model"
# 적절한 시점에 원격에 업로드
git push origin main
```

`git add`는 **준비**, `git commit`은 **로컬 이력 기록**, `git push`는 **GitHub 업로드**다. 세 단계는 서로 다른 작업이다.
<a id="git-branch-merge"></a>
### 7.3 기능 브랜치 생성·병합 (`checkout`·`merge`)

작업 중 다른 변경이 섞이지 않도록 현재 상태를 확인한 뒤 기능 브랜치를 만든다. **브랜치의 실제 코드 변경을 커밋**하고 나서 `main`으로 돌아와 병합한다.

```powershell
# 기존 미커밋 변경이 없는지 확인
git status -sb

# main에서 새 브랜치를 만들고 동시에 이동
git checkout main
git checkout -b feature/quiz-play

# 여기서 퀴즈 풀이 기능 구현·실제 테스트 수행 후
git add main.py
git commit -m "feat: implement quiz play and scoring"

# main으로 돌아가 병합
git checkout main
git merge --no-ff feature/quiz-play -m "merge: integrate quiz play"

# 브랜치 병합이 보이는지 확인
git log --oneline --graph --all --decorate

# 병합 후 main 업로드
git push origin main
```

`--no-ff`는 가능한 경우에도 **별도 병합 커밋을 남겨** 병합 사실을 그래프에서 쉽게 보여준다. `git status`에서 미커밋 변경이 있다면 먼저 보존·정리해야 하며, 위 명령을 무조건 연속 실행하지 않는다.

**의미 있는 커밋 10개 이상**을 위해 다음과 같이 실질적 작업을 나눌 수 있다.

| 작업 단위 | 커밋 내용 예시 |
|---:|---|
| 1 | README·`.gitignore`·프로젝트 설정 |
| 2 | `Quiz` 클래스 속성 정의 |
| 3 | `Quiz.show()`·`Quiz.check()` |
| 4 | 기본 퀴즈 5문제 |
| 5 | `QuizGame` 메뉴·입력 검증 |
| 6 | 브랜치에서 풀이·정답 판정 |
| 7 | 점수·최고 점수 관리 |
| 8 | 새 문제 입력·등록 |
| 9 | 퀴즈 목록·빈 목록 처리 |
| 10 | JSON 저장·불러오기 |
| 11 | 파일·입력 중단 오류 처리 |
| 12 | 테스트·README·실행 증빙 정리 |

이는 **계획 예시**다. 커밋 수를 채우려고 내용 없는 커밋을 만들지 않고, 실제 변경과 메시지가 일치하도록 기록한다.
<a id="clone-pull"></a>
<a id="git-clone-pull"></a>
### 7.4 `clone`과 `pull` 실습

**게임 제작 완료 후**, 원본 프로젝트와 **다른 폴더**에서 다음 과정을 수행한다.

```powershell
# 원본 폴더와 구분되는 곳에서 복제
Set-Location "C:\all in one"
# 아래 폴더가 아직 없을 때 실행
git clone https://github.com/modoofighting/E1-2.git e1-2-clone-check
Set-Location "C:\all in one\e1-2-clone-check"

# 복제본 README에 실제 실습 내용 한 줄을 추가하고 저장한 다음
git status -sb
git add README.md
git commit -m "docs: verify clone and sync workflow"
git push origin main

# 원본 프로젝트 폴더로 이동해 변경을 받아오기
Set-Location "C:\all in one\e1-2"
git status -sb
# 원본에 미커밋 변경이 없고 main 브랜치일 때 진행
git checkout main
git pull --ff-only origin main

# 원본에도 방금 복제본의 커밋·README 변경이 보이는지 확인
git log -5 --oneline
```

<a id="git-actual-clone"></a>
### 7.4.1 다른 PC에서 sky 복제와 실행

다른 Windows PC의 PowerShell에서 바탕화면으로 이동해 GitHub의 `sky` 브랜치를 복제했다. 실제로 입력한 주소는 `http`였고, Git이 `https`로 리디렉션해 복제를 완료했다.

```powershell
cd "$HOME\Desktop"
git clone -b sky http://github.com/modoofighting/E1-2.git
cd E1-2
git status -sb
```

확인된 출력:

```text
## sky...origin/sky
```

복제한 폴더를 VS Code로 열고 프로그램을 실행했다.

```powershell
code .
python main.py
```

실제 실행 결과에서 저장된 퀴즈 6개를 불러오고 메뉴가 표시됐다.

```text
저장된 퀴즈 6개를 불러왔습니다.
퀴즈 개수: 6
```

#### 두 PC에서 작업 내용 주고받기

한 PC에서 README나 코드를 수정한 뒤 `git status -sb`로 변경 파일을 확인하고, 필요한 파일을 `git add`, `git commit`, `git push` 순서로 원격 `sky`에 올린다. 다른 PC에서는 해당 저장소의 브랜치와 변경 사항을 먼저 확인한 뒤, `sky`에 있고 미커밋 변경이 없다면 다음 명령으로 가져온다.

```powershell
git pull --ff-only origin sky
```

다른 PC에서 실제로 `git pull --ff-only origin sky`를 실행한 결과:

```text
94507a8..60c96e7  sky -> origin/sky
Updating 94507a8..60c96e7
Fast-forward
README.md | 41 +++++++++++++++++++++++++++++++++++++++++
1 file changed, 41 insertions(+)
```

`sky`의 새 커밋을 가져와 다른 PC의 README가 갱신된 것을 확인했다.

<a id="git-evidence"></a>
### 7.5 증빙 이미지와 테스트 결과 정리

실제 실행 후에만 이미지를 만들고, **해당 기능 설명 옆**에 연결한다. 아래 파일명은 권장 경로이며, 없는 이미지를 완료 증빙처럼 링크하지 않는다.

| 과제 제출 증빙                    | 저장 위치 예시                               |
| --------------------------- | -------------------------------------- |
| Python 버전·VS Code·Git 환경    | `docs/screenshots/01-environment.png`  |
| 메뉴 실행                       | `docs/screenshots/02-menu.png`         |
| 퀴즈 풀이·채점                    | `docs/screenshots/03-play.png`         |
| 새 퀴즈 추가                     | `docs/screenshots/04-add.png`          |
| 퀴즈 목록                       | `docs/screenshots/05-list.png`         |
| 최고 점수                       | `docs/screenshots/06-best-score.png`   |
| 종료·재실행 후 복원                 | `docs/screenshots/07-restart.png`      |
| 잘못된 입력 처리                   | `docs/screenshots/08-input-errors.png` |
| `git log --oneline --graph` | `docs/screenshots/09-git-graph.png`    |
| clone·pull 수행               | `docs/screenshots/10-clone-pull.png`   |
<a id="git-readme-final-push"></a>
### 7.6 README 작성 후 최종 푸시

`main.py` 실행, JSON 복원, 필수 Git 명령 실습, 이미지 링크를 검수한 다음 **README 최종본을 커밋하고 push**한다.

```powershell
# 실제 프로젝트 폴더에서
Set-Location "C:\all in one\e1-2"
git checkout main

# 제출 전 현재 상태와 변경 파일 확인
git status -sb
git diff -- README.md

# 실제 수정이 있는 README와 존재하는 증빙 파일만 선택
git add README.md
# 스크린샷을 실제로 만든 경우에만 추가
# git add docs/screenshots/

git diff --cached --name-only
git diff --cached

# README 내용·링크와 변경사항을 확인한 후
git commit -m "docs: finalize E1-2 README and evidence"
git push origin main

# 제출용 이력 확인
git log --oneline --graph --all --decorate
git rev-list --count HEAD
```

<a id="git-checklist"></a>
### 7.7 최종 제출 점검표

- [ ] Python 3.10 이상, 외부 라이브러리 없이 `python main.py` 실행
- [ ] 메뉴 5개, 직접 작성한 기본 퀴즈 5개 이상·4지선다
- [ ] `Quiz`·`QuizGame` 두 클래스와 역할별 메서드 구현
- [ ] 정답·오답·최종 점수·최고 점수·빈 문제 목록 처리
- [ ] 문제 추가·목록 확인·종료·재실행 후 데이터 유지
- [ ] `state.json` 루트 경로, UTF-8, `quizzes`·`best_score` 스키마 일치
- [ ] 공백·문자·범위 밖·빈 입력·Ctrl+C·EOF·파일 없음·손상·입출력 오류 대응
- [ ] `git init/add/commit/push/pull/checkout/clone` 실제 수행 흔적
- [ ] 기능 브랜치 생성·`merge`·`git log --oneline --graph` 증빙
- [ ] 의미 있는 커밋 **10개 이상**과 개발 환경·게임 실행 스크린샷
- [ ] **README 최종 검수 후 `git add` → `git commit` → `git push`**
- [ ] 공개된 [E1-2 GitHub 저장소](https://github.com/modoofighting/E1-2)에서 실제 파일·문서 링크 확인

---
