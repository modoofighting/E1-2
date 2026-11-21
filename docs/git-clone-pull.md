## STEP 6. Git clone·pull 실습

**목적:** 개발 완료된 원격 저장소를 별도 디렉터리에 복제하고, 복제본에서 수정한 사항을 GitHub에 올린 뒤, **원래 폴더에서 pull로 받는 과정**을 실제 증명한다. 과제에서 clone과 pull은 **둘 다 필수**다.
### 6. Git 작업 3단계 — `clone`과 `pull` 실습 (과제 필수)

> **중요:** 이 실습은 게임 개발 완료 후 진행합니다. 원래 E1-2 작업 폴더와 **별개의 폴더**를 사용합니다. 원본 `C:\all in one\e1-2`를 덮어쓰지 않습니다.

#### 6.1 별도 폴더에 GitHub 저장소 복제

```powershell
# 원본이 아닌 상위 폴더로 이동합니다.
Set-Location "C:\all in one"

# 복제본이 이미 있는지 확인합니다.
Test-Path "C:\all in one\e1-2-clone-check"

# clone = 원격 저장소를 새 로컬 폴더로 복사 [필수 명령 6]
# 복제 대상 e1-2-clone-check가 아직 없을 때만 실행합니다.
# URL은 실제 E1-2 GitHub 저장소로 바꿉니다.
git clone https://github.com/본인아이디/e1-2-quiz-game.git "e1-2-clone-check"

# 복제본 폴더에서 작업 시작
Set-Location "C:\all in one\e1-2-clone-check"
git status -sb
git remote -v
```

#### 6.2 복제본의 README에 변경 1건 추가하고 push

1. VS Code에서 **복제본** `C:\all in one\e1-2-clone-check\README.md`를 엽니다.
2. `## 복제·동기화 확인`이라는 짧은 단락과 실제 실습 날짜를 추가해 저장합니다.
3. 복제본에서 변경을 확인하고 커밋·푸시합니다.

```powershell
# 현재 폴더가 복제본인지 확인합니다.
Get-Location

# README 변경이 생겼는지 확인
git status -sb
git diff -- README.md

# 복제본 README 변경만 커밋·push
git add README.md
git commit -m "docs: verify clone and remote sync"
git push origin main
```

#### 6.3 원본 폴더에서 `pull`로 변경 가져오기

```powershell
# 원래 프로젝트 폴더로 돌아옵니다.
Set-Location "C:\all in one\e1-2"

# pull 전에 작업 중인 변경이 없는지 확인합니다.
git status -sb

# pull = 원격 변경을 가져와 현재 브랜치와 통합 [필수 명령 7]
# 원본이 main 브랜치이고 미커밋 변경이 없을 때 실행합니다.
git checkout main
git pull origin main

# clone 폴더에서 추가한 README 단락이 반영됐는지 확인합니다.
git log -3 --oneline
git status -sb
```

**증빙 기준:** 복제본에서 발생한 커밋이 원본의 `git log`에서도 확인되고, 수정한 README 단락이 원본에서 보이면 `clone → commit → push → pull` 과정을 완료한 것입니다.

---
